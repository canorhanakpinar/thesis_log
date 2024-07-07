import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import re
import pandas as pd

class ResmiGazeteScraper:
    def __init__(self, year):
        self.base_url = 'https://www.resmigazete.gov.tr/eskiler'
        self.year = str(year)
        self.months = [f"{month:02d}" for month in range(1, 13)]
        self.days = [f"{day:02d}" for day in range(1, 32)]
        self.content = ""
        self.last_url = None
        self.last_xpath = None
        self.data = []
        self.df = pd.DataFrame()  # Initialize an empty DataFrame

    def get_xpath(self, element):
        components = []
        child = element if element.name else element.parent
        while child is not None and child.name != '[document]':
            siblings = list(child.parent.children) if child.parent else []
            count = 1 + sum(1 for sib in siblings[:siblings.index(child)] if sib.name == child.name)
            components.append(f"{child.name}[{count}]")
            child = child.parent
        components.reverse()
        return '/' + '/'.join(components)

    def scrape(self, tags=None):
        self.tags = tags or 'a'  # Default tags if none provided
        for month in self.months:
            for day in self.days:
                url = f"{self.base_url}/{self.year}/{month}/{self.year}{month}{day}.htm"
                time.sleep(1)
                response = requests.get(url)
                if response.status_code == 200:
                    self.process_page(response, url, month, day)
                else:
                    print(f"Failed to retrieve the page: {url}, Status code {response.status_code}")

    def process_page(self, response, url, month, day):
        if 'charset' in response.headers.get('Content-Type', ''):
            encoding = response.headers['Content-Type'].split('charset=')[-1]
        else:
            encoding = response.apparent_encoding
        response.encoding = encoding

        soup = BeautifulSoup(response.text, 'lxml')
        for element in soup.find_all(self.tags):
            text = re.sub(r'\s+', ' ', element.get_text()).strip()
            text = text.replace('\u0094', '')  # Replace specific unicode character if needed    
            if text not in ("Å" , "Sayfa Başı", "Æ", "ÖNCEKİ", "SONRAKİ", ""):
                xpath = self.get_xpath(element)
                if element.name == 'a' and element.has_attr('href'):
                    href = urljoin(url, element['href'])  # Correctly handle href only for 'a' tags
                    
                else:
                    href = "No href" 

            # Check if it's the same as the last href to decide whether to append or start a new line
                if  href == self.last_url:
                    self.content += " " + text  # Append text only, corrected from '\n' to ' ' for continuity
                else:
                    detail = f"Date: {self.year}-{month}-{day}, XPath: {xpath}, Tag: {element.name}"
                    if href:
                        detail += f", Link: {href}, Text: {text}"
                    else:
                        detail += f", Text: {text}"
                    
                    self.content += f"\n{detail}"
                    self.last_url = href  # Update last_url regardless of element type
                    self.last_xpath = xpath

    def save_content_to_file(self):
        directory = "resmigazete_all"
        filename = f"{directory}/XPaths_resmigazete_{self.year}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.content.strip())
        print(f"Content saved to {filename}")

    def parse_to_dataframe(self):
        lines = self.content.split('\n')
        current_entry = {"Text" :"" }
        for line in lines:
            # Use regex to correctly split the line into key-value pairs
            try:
                parts = re.split(r', (?=\b(?:Date|XPath|Tag|Text|Link)\b)', line.strip())
                entry = {key.strip(): value.strip() for part in parts for key, value in [part.split(': ', 1)]}
            except:
                entry = {"Text" : ""}
            
            # Manage appending or creating new entries based on the link continuity
            if current_entry and entry.get('Link') == current_entry.get('Link'):
                # If the same link, concatenate the text
                current_entry['Text'] += " " + entry['Text']
            else:
                # If a different link or a new line, append the current entry and start a new one
                if current_entry:
                    self.data.append(current_entry)
                current_entry = entry

        # Ensure the last entry is added
        if current_entry:
            self.data.append(current_entry)
        
        # Create DataFrame from the list of dictionaries
        self.df = pd.DataFrame(self.data)
        self.df.drop(["XPath", "Tag"], axis=1, inplace = True)
        # Optionally, add empty columns as required
        empty_columns = ['Legal Category', 'Summary', 'Hyperlinks', 'Note1', 'Note2', 'Note3']
        for col in empty_columns:
            self.df[col] = "EMPTY"
 

    def save_to_json(self):
        if self.df.empty:
            print("No data to save.")
            return
        output_file = f"resmigazete_all/titles_resmigazete_{self.year}.json"
        self.df.to_json(output_file, orient='records', lines=True)
        print(f"Data saved to {output_file}")

    def save_to_excel(self):
        if self.df.empty:
            print("No data to save to Excel.")
            return
        output_file = f"resmigazete_all/titles_resmigazete_{self.year}.xlsx"
        self.df.to_excel(output_file, index=False)
        print(f"Data saved to {output_file}")

    def update_hyperlinks(self, filepath, start_date, end_date):
        # Load the DataFrame from the given Excel file
        hyper_df = pd.read_excel(filepath)
        hyper_df['Date'] = pd.to_datetime(hyper_df['Date'])  # Ensure Date column is in datetime format
        
        # Filter the DataFrame based on the provided date range
        filtered_df = hyper_df[(hyper_df['Date'] >= pd.to_datetime(start_date)) & (hyper_df['Date'] <= pd.to_datetime(end_date))]
        
        # Process each row in the filtered DataFrame to extract hyperlinks
        for index, row in filtered_df.iterrows():
            url = row['Link']
            try:
                response = requests.get(url)
                time.sleep(1)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'lxml')
                    links = [urljoin(url, tag.get('href', '')) for tag in soup.find_all('a', href=True)]
                    links_str = '; '.join(links)  # Join all links with a semicolon
                    hyper_df.at[index, 'Hyperlinks'] = links_str  # Update the DataFrame
            except requests.RequestException as e:
                print(f"Failed to retrieve {url}: {str(e)}")
        
        # Convert Date column back to string format without time component
        hyper_df['Date'] = hyper_df['Date'].dt.strftime('%Y-%m-%d')
        
        # Save the updated DataFrame back to the same Excel file
        hyper_df.to_excel(filepath, index=False)
        print(f"Updated Excel file saved to {filepath}")



## Merged with Scraper
class ResmiGazeteLinkParser:
    def __init__(self, year):
        self.year = year
        self.file_path = f"resmigazete_all/XPaths_resmigazete_{self.year}.txt"
        self.data = []
        self.df = None  # DataFrame attribute

    def parse_file(self):
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return

        current_entry = None
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if 'Link:' in line:
                    parts = re.split(r', (?=\b(?:Date|XPath|Tag|Text|Link)\b)', line.strip())
                    entry = {key.strip(): value.strip() for part in parts if ': ' in part for key, value in [part.split(': ', 1)]}

                    if current_entry and current_entry['Link'] == entry['Link']:
                        current_entry['Text'] += "" + entry['Text']
                    else:
                        if current_entry:
                            self.data.append(current_entry)
                        current_entry = entry

        if current_entry:
            self.data.append(current_entry)

        self.df = pd.DataFrame(self.data)
        self.df.drop(["XPath", "Tag"], axis=1)
        
        # Adding extra empty columns
        empty_columns = ['Legal Category', 'Summary', 'Hyperlinks', 'Note1', 'Note2', 'Note3', 'Note4', 'Note5', 'Note6']
        for col in empty_columns:
            self.df[col] = "This is empty."
    
    def save_to_json(self):
        if self.df is None or self.df.empty:
            print("No data to save.")
            return

        output_file = f"resmigazete_all/titles_resmigazete_{self.year}.json"
        self.df.to_json(output_file, orient='records', lines=True)
        print(f"Data saved to {output_file}")
    
