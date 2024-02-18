	First essay on Propensity Score estimation and Difference-in-Differences analysis methodology.

For estimating similarity, I will define a set of properties defining agricultural production.

In propensity score matching, I defined a set of variables for assessing similarity. As time progresses, new data can add or delete variables from my initial set. This log holds the record of the methodological shift. Because "data" is very subjective in quantitative social sciences. We are coming up with abstract information to represent conceptions. Designing measurement metrics therefore can be quite biased, as well as interpreting the results. 

A computational way of overcoming the measurement problem is to try as many sets in as many combinations. Using a vast set of features, we become less bounded to a curated set and can test many other options. This may cost a significant amount of computation time. Machine learning algorithms may also help to reduce dimensions such as with PCA (Principal Component Analysis), and LDA (Linear Discriminant Analysis).

- Check standard errors

**Explanation** 
My interest in the analysis is to understand whether the affected cities experience alterations before and after the application of the law. 

The subject cities have a diverse distribution regarding their measured traits. Comparing each for itself lacks overcoming self-dependency**. Therefore we must compare them to similar places that have not been treated. In this case, however, there can still be a self-dependency issue if our matched cities are experiencing different situations for specific time periods. 

In short, the estimation requires similarity components that are selected assumably. The assumptions for variable selection therefore need to be comprehensive enough for defining similarity. Then, by choosing my components I am introducing model model-dependent structure for agricultural representation.

One of the reasons propensity score is critiqued is the subjective model selection process. The second point is the after-matching process where we have to omit or aggregate when there are unequal variables in groups after propensity stratification. ***

Computationally, we can estimate propensity scores by machine learning algorithms. In this way, we can create a linear image of the city. Computational methods may work with more features better, estimating covariates and weighting features accordingly. 

On the other hand, computational methods may also help in estimating our interested feature set. Instead of a regression fit, which we applied for zero to one propensity score estimation, using tree-based models may help refine a focused feature set based on all variables' weighting information***.

Then the question is, what defines agricultural similarity? Here I will try to put an exhaustive list of variables and their explanations. The part after "-" indicates the form of the data.

Propensity score matching uses a distance-based distribution model for explanatory features. A non-representative feature might create bias in estimating closeness. To overcome this, we have to test propensity scores by using different sets of variables. 

Additionally, I must decide the period that includes explanatory features. Ideally, I will compare propensity scores year by year and as an aggregated mean. Variation of matching might reveal unmeasurable external factors that are affecting one city differently than the other. 

In all steps, comparing matching methods with random matches will serve as a robustness check for the assessments. Random matching eliminates all the biases related to model selection but may introduce biases due to variance of control sample selection. However, given that we have 67 cities that are not affected by Law 6360, it is possible to test matches exhaustively.  


### Agricultural Components

**Land Size (?log) - Secondary**

How land size is related to agricultural output? What are contrary examples?

**Average parcel size - Secondary**

By averaging, I am estimating the farm fragmentation degree. However, fragmentation may happen differently by ownership. By assessing land size thus assume that land ownership is representing

**Migration - Secondary**

How is migration affected by the law? Do we see a shift in the migration rate trend?

Since farmer migration is a prevalent trend (req. ref.), all cities especially the less industrialized must be experiencing outgoing migration. Therefore we need to look at the resemblance of the rate, considering there is a relationship between corporate farming and industrialization with the reduction of small-scale farming of rural residents.

**Vegetation Density - Transformed data**

How does vegetation density affect agriculture, or to what degree they are correlated?
What are contrary examples?


**Agricultural Output (as size, as fiscal) - Secondary**

How does adding agricultural output as size, fiscal or both changes the propensity estimation? Do other variables contain information regarding agricultural output?

What are the dynamic reasons shaping agricultural output? Natural hazards, high-technology farming, foreign direct investment, and land transfer frequency are some confounding factors.

**Population (?log) - Secondary**

Does using population size as an indicator of the city size introduce bias in estimating similarity?
Or should we proceed with two-stage estimation by grouping population sizes and comparing control cities' other variables' coefficients in a logit and tree model?  

**Agro.Output / Total Output - Secondary**

Agricultural output as a single index of agricultural production may fail the equation due to the size of cities. Including the agricultural output ratio helps estimate the agriculturalization of a city.


**Water Use - Secondary**

Water use size, as well as wastewater size, may indicate the urbanization of a city.
The best is we can use water use data for agriculture. We can then check the value proportion of agricultural output / total output, to see if they resemble each other.

-----
### Non-Agricultural Components

**City light density distribution - Transformed data**

City light density may show the dispersion of settlements in the city.
For example, having more developed provinces outside of the central municipality may affect the city's industrialization. 


**Total number of elementary and high schools - Secondary**
**Total number of colleges - Secondary**

**Road density (connectedness) - Transformed data**

**Distance from sea (Closer distance) - Transformed data** 

Total number of provinces of a city (can we scale by minus 1, extracting central municipality if we compare treated with non-metropolis cities) - Secondary

**Having an airport (Binary variable)**

**Median or Mean temperatures**

**Tourism income**

What is non-industrial income?
Is the service sector proportional to tourism income? 

**Industrial output**

Total Number of workers (may be scaled with population, do agricultural jobs which are informal included in employment statistics?)


-----
### Difference in Differences

After selecting the matches, I will search if there is a diverging trend shift after the law imposition. This is a natural experiment design where I assumed that assessed propensity values represent similarity and therefore the cities are exposed to similar uncontrollable external effects. 

What are the problems of using difference in differences (DID)?
By comparing two cities, we assume a continuous similarity between cities. We assume that external factors such as law changes, environmental conditions, international trade, and economic shifts affect two cities in the same way. However, external factors may affect matched cities disproportionately. If so, the analysis will fail to control external variables. Therefore the matching assumption that is defined prior to DID analysis will not hold, and we should find a new match.

In parallel, coefficient slope analysis can be applied prefiguratively before propensity matching. Slope matching can simplify the process for specific target variables. Simultaneously to propensity scores, running similarity tests for target variables may or may not introduce bias. However, this is the most fundamental way of showing the similarity between two samples. But we are preconditioning ourselves for similarity solely based on a single metric. This is more interpretable than propensity score matching, which matches the distances in linear systems.

To create the model, once again we must assume our dynamic variables. What would be the best way to show the effects of the law? Choosing an unrelated variable prevents finding the real outcome, and may produce bias. I will propose dynamic components that might be affected by the law. Year-by-year constant values that are used in propensity score matching thus, will be excluded.

Using the difference in differences helps to eliminate quantitative characteristics. By looking at the slope of the differences in treated and nontreated cities, we are trying to de-mean the characteristics that are specific to the city, and projecting the possible difference in differences that would be seen if the city hadn't been treated.

**Migration**

**Agricultural output**

What is the change in agricultural output?

**Mean or Median Parcel Size**

How can we assess if there difference in parcel sizes? Is there a reliable and representative data?

**Municipal Budget**

Does the municipal budget affect or explain agricultural production? Law 6360 caused a shift of responsibilities between central and other provinces. Reciprocally, villages should pay newly imposed costs and receive infrastructure services. 





