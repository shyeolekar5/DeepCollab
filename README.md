# Customer Personality Analysis using Machine Learning

<mark>Highlighted text needs to be edited<mark>

Text without highlighting or a code box is ready for review

## Table of Contents
- [Project Overview and Objective](#project-overview-and-objective)
- [Understanding The Data](#understanding-the-data)
- [Methods & Technologies](#methods--technologies)
- [Key Findings & Conclusion](#key-findings--conclusion)
- [Team Information](#team-information)

# Project Overview and Objective

Understanding a customer's shopping personality is a crucial step in developing a personalized marketing strategy for your customer. Our project aims to help businesses better understand their customers by providing an in-depth analysis of "customer personalities". By gaining a deeper understanding of these personalities, businesses can tailor their marketing efforts to target the right customers with the right content at the right time.

Our approach involves using K-Means clustering to segment customers into distinct "shopping profiles", and a [type of predictive model we used] predictive model to assess how likely each customer is to respond to a future marketing campaign. This allows marketing teams to optimize their resources by better understanding how to engage with their customers and by focusing on the segments most likely to repond, thereby improving the effectiveness of their campaigns and maximizing ROI.

Through this analysis, businesses will gain valuable insights into their customer base, enabling them to refine their marketing strategies and deliver more personalized, targeted experiences. This project ultimately aims to help businesses:

1. Better understand how to engage with each profile, and aim to **increase customer engagement** through tailored interactions that resonate with each customer's individual preferences and behaviors.

2. **Drive sales** by implementing hyper-personalized marketing strategies that align with the specific needs and desires of each profile.

3. **Optimize marketing resources and efforts** by effectively targeting each profile, and ensuring that campaigns are directed at the most responsive and relevant customers.

### Stakeholders & Their Interests
- **Marketing Teams**: Optimize campaigns by targeting the right customers with the right content at the right time.

- **Business Executives**: Improve decision-making regarding product offerings and promotions.

- **Data Science Teams**: Implement machine learning models to refine customer segmentation and predictive analytics.


### Business Value
- **Enhanced Marketing Strategies**: More targeted and cost-effective promotional campaigns.

- **Customer-Centric Approach**: Personalization of marketing efforts to improve customer experience.

- **Data-Driven Decision Making**: Leveraging machine learning to extract insights and improve business strategies.

# Understanding The Data

The Customer Personality Analysis dataset used in this project provides valuable insights into a company’s ideal customer segments, helping businesses better understand its customers and makes it easier for them to modify products according to the specific needs, behaviors and concerns of different types of customers. Our exploratory data analysis of the dataset found the following:

## Required Libraries

`Echo, Shraddha, Lauren, Frances, Kevin`

This project uses the following Python libraries:

- **pandas**: used for data manipulation and analysis

## Key Attributes:
- **Demographics**: birth year, education, marital status, income, household composition.
- **Store Engagement**: enrollment date at store, number of dayas since last purchase at store, whether a customer has raised complaints in the past two years.
- **Purchase Behavior**: amount spent in the past 2 years on wine, fruit, meat products, fish products, sweet products and gold.
- **Promotion Response**: number of purchases made with a discount and whether a customer has accepted a campaign.
- **Channel Engagement**: Frequency of purchases made via the web, catalog, and physical stores, along with website visit frequency.

## Data Set Limitations: 

`Echo`

<mark>This dataset has 2240 rows and 29 attributes - it is mostly clean. The following are limitations found on the dataset:<mark>

<mark>- **Missing income data**: 24 out of 2240 rows don’t have an income value.<mark>

<mark>- **Limited transaction history**: The dataset covers spending from the last 2 years, but it lacks detailed transaction data such as purchase dates, individual transaction amounts, channel purchased through, brand preferences, etc.<mark>

<mark>- **Limited demographic information**: No gender or location.<mark>

## Risks and Uncertainties

`Echo`

<mark>The following are risks and uncertainties we have about the dataset:<mark>

<mark>- **Data Set Size and Limitations**: The dataset consists of only 2,240 records, which may limit model performance and generalizability.<mark>

<mark>- **Model Generalization**: Clustering and predictive models might not generalize well across different customer groups.<mark>

<mark>- **External Factors**: Economic changes, seasonal trends, or competitive actions could influence customer behavior in ways not captured by historical data.<mark>

# Methods & Technologies

## Exploratory Data Analysis

### Data Quality Assessment, Cleaning, and Transformations

`Echo`

<mark>The following data cleaning and transformations were conducted on the dataset:<mark>

<mark>- Missing values were handled, duplicates were removed, data type issues were fixed, and outliers were handled.<mark>

<mark>- Data distributions were analyzed and and potential data quality issues were identified.<mark>

<mark>- Customer data was visualized to better understand the ratio of high-value customers to budget shoppers, past purchasing behaviour and promo use of each customer, and customer demographics and behaviours.<mark>

### Feature Engineering

`Echo`

<mark>Minor feature engineering was conducted on the dataset:

<mark>- New features were created including total spend, campaign response rate, shopping frequency, household size, and customer lifetime value metrics.<mark>

<mark>- Features were scaled and analyzed to better understand their distributions and relationships. Key steps included scaling numerical features, generating a correlation matrix, and analyzing various data visualizations.<mark>

## Preprocessing and Pipeline

`Shraddha - review and confirm that pipeline was only used on clustering models`

<mark>Precprocessing was conducted on the dataset and imported into a master pipeline that was used for both clustering models. The following approach was taken:<mark>

<mark>- Additional feature engineering was conducted on top of the feature engineering done in our EDA.<mark>

<mark>- Data preprocessing was conducted on the dataset.<mark>

<mark>- Both steps were chained together in a single object to ensure that all steps were applied sequentially and that data leakage was avoided.<mark>

## Model Exploration and Selection

`Lauren and Frances`

<mark>Our approach to clustering each customer into "shopper profiles" consisted of testing out two different clustering methods, k-means and DBSCAN, and selecting the high performing model to perform our analysis.<mark>

### DBSCAN Clustering

`Lauren`

<mark>[x]<mark>

### K-Means Clustering

`Frances`

<mark>[x]<mark>

## Feature Selection

<mark>(approach only, no findings)<mark>

# Key Findings & Conclusion

## Exploratory Data Analysis

### Data Quality Assessment

`Echo`

<mark>The dataset was checked for missing values, duplicates, outliers, and inconsistent values. Data distributions were analyzed and potential data quality issues were identified.<mark>

### Data Cleaning and Transformation

`Echo`

<mark>Missing values were handled, duplicates were removed, data type issues were fixed, and outliers were handled. The following are some of the key transformations that were completed on the data set:<mark>

<mark>- Missing values in Income were replaced with the column's median<mark>

<mark>- Date columns were converted to datetime format.<mark>

<mark>- Marital_Status categories were transformed into either 'Single_Household', 'Couples' or 'Unknown'.<mark>

<mark>- Age column was created from Year_Birth.<mark>

`Echo - please confirm if all or some string values were encoded`

<mark>- Attributes containing string values were encoded into numerical values.<mark>


### Feature Engineering

`Echo`

<mark>For more information on our EDA, please look at the [x] file in our repo<mark>

## Preprocessing and Pipeline

`Shraddha`

<mark>(results)<mark>

<mark>For more information on our preprocessing method, please look at the [x] file in our repo<mark>

## Deep Learning Modeling

### K-Means Clustering

`Shraddha and Frances`

<mark>(results)<mark>

<mark>For more information on our approach to modeling, please look at the [x] file in our repo<mark>

`Kevin`

<mark>(results)<mark>

<mark>For more information on our approach to modeling, please look at the [x] file in our repo<mark>

## Conclusion

<mark>This project will demonstrate how machine learning can enhance customer analysis, providing valuable insights for businesses to refine marketing strategies. By combining clustering and predictive modeling, we aim to offer a robust framework for personalized marketing and improved business outcomes.<mark>

<mark>**Final Outcome**<mark>

<mark>**Key Business Takeaways**<mark>

# Team Information

`Lauren`

### Team Members
Team Member | GitHub | Email | Role & Responsibilities | Video
--- | --- | --- | ---  | ---
Fan(Echo) Yu | [echooocc](https://github.com/echooocc) | echo2go@gmail.com | <mark>[x]<mark> | <mark>[[x]]([x])<mark> |
Kevin Lu | [kevinlutoronto](https://github.com/kevinlutoronto) | kevin.lu.toronto@gmail.com  | <mark>[x]<mark> | <mark>[[x]]([x])<mark> |
Lauren Tonello | [ltonello](https://github.com/ltonello) | lauren.tonello@gmail.com | <mark>[x]<mark> | <mark>[[x]]([x])<mark> |
Oi Yee(Frances) Chung | [franceschung](https://github.com/franceschung) | frances.chungoy@gmail.com | <mark>[x]<mark> | <mark>[[x]]([x])<mark> |
Shraddha Yeolekar | [shyeolekar5](https://github.com/shyeolekar5)| shraddha.goyani@gmail.com | <mark>[x]<mark> | <mark>[[x]]([x])<mark> |

## Team's Approach to Collaboration

<mark>[x]<mark>
