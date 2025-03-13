# Customer Personality Analysis using Machine Learning

## Table of Contents
- [Project Introduction](#project-introduction)
- [Dataset Introduction](#dataset-introduction)
- [Objectives and Business Case](#objectives-and-business-case)
- [Risks and Uncertainties](#risks-and-uncertainties)
- [Methods & Technologies](#methods--technologies)
- [Conclusion](#conclusion)
- [Team Members](#team-members)

## Project Introduction

Customer Personality Analysis is a crucial step in understanding consumer behavior and tailoring business strategies accordingly. This project aims to segment customers using clustering techniques and develop a predictive model to assess the effectiveness of promotional campaigns. By leveraging machine learning, we seek to provide actionable insights that enhance marketing efficiency and customer satisfaction.

## Dataset Introduction

The dataset, sourced from [Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis), provides a comprehensive view of customer demographics, purchasing behavior, and promotional engagement. The data is valuable for businesses looking to optimize marketing efforts and better understand customer segments.

### Key Attributes:
- **Demographics**: Birth year, education, marital status, income, household composition
- **Purchase Behavior**: Spending across different product categories, such as wine, fruits, meat, fish, sweets, and gold
- **Promotion Response**: Whether customers accepted promotional offers across multiple campaigns
- **Engagement**: Frequency of purchases made via the web, catalogs, and physical stores, along with website visit frequency
- **Recency & Complaints**: Last purchase recency and whether a customer has raised complaints in the past two years

### Data Set Limitations: 

## Objectives and Business Case
The dataset with 2240 rows and 29 attributes is mostly clean. The below is a list of limitations on dataset.
- **Missing income data**: Out of 2240 rows, 24 rows don’t have income.
- **Limited transaction history**: The dataset covers spending from the last 2 years, but it lacks specific timestamps for individual transactions.
- **Limited information**: No information on product preferences beyond spending categories (e.g., no breakdown by products’ brands). No customer feedback data (aside from complaints), which could help refine engagement strategies.

### Stakeholders & Their Interests
- **Marketing Teams**: Optimize campaigns by targeting the right customer segments.
- **Business Executives**: Improve decision-making regarding product offerings and promotions.
- **Data Science Teams**: Implement machine learning models to refine customer segmentation and predictive analytics.

### Business Value
- **Enhanced Marketing Strategies**: More targeted and cost-effective promotional campaigns.
- **Customer-Centric Approach**: Personalization of marketing efforts to improve customer experience.
- **Data-Driven Decision Making**: Leveraging machine learning to extract insights and improve business strategies.

### Objectives
Our project aims to:
1. **Segment customers** based on purchasing behavior and demographics using clustering techniques. For example, can we classify customers as high-value or budget shoppers based on their purchasing behavior and promotional usage?
2. **Develop a predictive model** to analyze the effectiveness of promotional campaigns. For example, can we predict their likelihood of responding to future marketing campaigns using past data?
3. **Provide insights** on optimizing marketing efforts to increase customer engagement and revenue.

## Risks and Uncertainties
- **Data Set Size and Limitations**: The dataset consists of only 2,240 records, which may limit model performance and generalizability.
- **Model Generalization**: Clustering and predictive models might not generalize well across different customer groups.
- **External Factors**: Economic changes, seasonal trends, or competitive actions could influence customer behavior in ways not captured by historical data.

## Methods & Technologies
- **Exploratory Data Analysis**
- **Data Cleaning**: Handle missing values and outliers, Remove Duplicates, and Fix DataType Issues
- **Data Preprocessing**: Normalize/scale numerical features and encoding categorical variables.
- **Feature Engineering**: Derive new features for example Total Spending
- **Clustering Techniques**: K-Means to segment customers.
- **Predictive Modeling**
- **Evaluation Metrics**
- **Tools & Technologies**:
  - Python (Pandas, NumPy, Scikit-learn, Matplotlib)
  - Jupyter Notebook for experimentation
  - Cloud platforms or local compute resources for model training

## Conclusion
This project will demonstrate how machine learning can enhance customer analysis, providing valuable insights for businesses to refine marketing strategies. By combining clustering and predictive modeling, we aim to offer a robust framework for personalized marketing and improved business outcomes.

## Team Members
- [Fan(Echo) Yu](https://github.com/echooocc) 
- [Kevin Lu](https://github.com/kevinlutoronto) 
- [Lauren Tonello](https://github.com/ltonello) 
- [Oi Yee(Frances) Chung](https://github.com/franceschung) 
- [Shraddha Yeolekar](https://github.com/shyeolekar5) 
