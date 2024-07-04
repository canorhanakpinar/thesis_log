import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import re
import pandas as pd
import os

class ResmiGazeteScraper:    
    def __init__(self, year):  
        self.base_url = 'https://www.resmigazete.gov.tr/eskiler'
        self.year = str(year)
        self.months = [f"{month:02d}" for month in range(1, 13)]
        self.days = [f"{day:02d}" for day in range(1, 32)]
        self.content = ""  # Content accumulated as a single string
        self.last_url = None
        self.last_xpath = None

    def get_xpath(self, element):
        """Generate XPath for a BeautifulSoup element by walking up its tree."""
        components = []
        child = element if element.name else element.parent
        while child is not None and child.name != '[document]':
            siblings = list(child.parent.children) if child.parent else []
            count = 1 + sum(1 for sib in siblings[:siblings.index(child)] if sib.name == child.name)
            components.append(f"{child.name}[{count}]")
            child = child.parent
        components.reverse()
        return '/' + '/'.join(components)

    def scrape(self):
        for month in self.months:
            for day in self.days:
                url = f"{self.base_url}/{self.year}/{month}/{self.year}{month}{day}.htm"
                time.sleep(1)  # Adjusted delay to prevent too frequent requests
                response = requests.get(url)
                
                if 'charset' in response.headers.get('Content-Type', ''):
                    encoding = response.headers['Content-Type'].split('charset=')[-1]
                else:
                    encoding = response.apparent_encoding
                response.encoding = encoding

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'lxml')
                    for element in soup.find_all(True):  # True fetches all tags
                        raw_text = element.get_text()
                        text = re.sub(r'\s+', ' ', raw_text).strip()  # Replace multiple whitespace/newline with single space
                        text = text.replace('\u0094', '')  # Strip the specific unicode character
                        if text:
                            xpath = self.get_xpath(element)
                            current_detail = f"Date: {self.year}-{month}-{day}, XPath: {xpath}, Tag: {element.name}"
                            if element.name == 'a':
                                href = element['href'] if 'href' in element.attrs else 'No href available'
                                href = urljoin(url, href)
                                text_detail = f"Link: {href}, Text: {text}"
                            else:
                                text_detail = f"Text: {text}"
                            
                            if xpath == self.last_xpath and url == self.last_url:
                                self.content += " " + text  # Append text only
                            else:
                                self.content += f"\n{current_detail}, {text_detail}"
                                self.last_url = url
                                self.last_xpath = xpath
                
                else:
                    print(f"{self.base_url}/{self.year}/{month}/{self.year}{month}{day}.htm: Status code {response.status_code}")

    def save_content_to_file(self):
        directory = "resmigazete_all"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f"{directory}/XPaths_resmigazete_{self.year}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.content.strip())  # Save cleaned-up content
        print(f"Content saved to {filename}")




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

        # Adding extra empty columns
        empty_columns = ['Legal Category', 'Summary', 'Hyperlinks', 'Note1', 'Note2', 'Note3', 'Note4', 'Note5', 'Note6']
        for col in empty_columns:
            self.df[col] = "This is empty."
    
    def save_to_json(self):
        if self.df is None or self.df.empty:
            print("No data to save.")
            return

        output_file = f"resmigazete_all/links_resmigazete_{self.year}.json"
        self.df.to_json(output_file, orient='records', lines=True)
        print(f"Data saved to {output_file}")
    
