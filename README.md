# Customer Personality Analysis using Machine Learning

## Table of Contents
- [Project Overview and Objective](#project-overview-and-objective)
- [Understanding The Data](#understanding-the-data)
- [Methods & Technologies](#methods--technologies)
- [Key Findings & Conclusion](#key-findings--conclusion)
- [Team Information](#team-information)

## Project Overview and Objective
Understanding a customer's shopping personality is a crucial step in developing a personalized marketing strategy for your customer. Our project aims to help businesses better understand their customers by providing an in-depth analysis of "customer personalities". By gaining a deeper understanding of these personalities, businesses can tailor their marketing efforts to target the right customers with the right content at the right time.

Our approach involves using K-Means clustering to segment customers into distinct "shopping profiles", and logic regression and random forest classifier predictive models to assess how likely each customer is to respond to a future marketing campaign. This allows marketing teams to optimize their resources by better understanding how to engage with their customers and by focusing on the segments most likely to respond, thereby improving the effectiveness of their campaigns and maximizing ROI.
Through this analysis, businesses will gain valuable insights into their customer base, enabling them to refine their marketing strategies and deliver more personalized, targeted experiences. This project ultimately aims to help businesses:

1. Better understand how to engage with each profile, and aim to **increase customer engagement** through tailored interactions that resonate with each customer's individual preferences and behaviors.
2. **Drive sales** by implementing hyper-personalized marketing strategies that align with the specific needs and desires of each profile.
3. **Optimize marketing resources and efforts** by effectively targeting each profile, and ensuring that campaigns are directed at the most responsive and relevant customers.

#### Stakeholders & Their Interests
- **Marketing Teams:** Optimize campaigns by targeting the right customers with the right content at the right time.
- **Business Executives:** Improve decision-making regarding product offerings and promotions.
- **Data Science Teams:** Implement machine learning models to refine customer segmentation and predictive analytics.

#### Business Value
- **Enhanced Marketing Strategies:** More targeted and cost-effective promotional campaigns.
- **Customer-Centric Approach:** Personalization of marketing efforts to improve customer experience.
- **Data-Driven Decision Making:** Leveraging machine learning to extract insights and improve business strategies.
  
## Understanding The Data
The *Customer Personality Analysis* dataset used in this project provides valuable insights into a company’s ideal customer segments, helping businesses better understand its customers and makes it easier for them to modify products according to the specific needs, behaviors and concerns of different types of customers. Our exploratory data analysis of the dataset found the following:

### Required Libraries
This project uses the following Python libraries:
- **pandas, numpy:** data manipulation and analysis
- **Sklearn:** data transformation, scaling and different models
- **Matplotlib, seaborn:** data visualization

### Key Attributes:
- **Demographics:** birth year, education, marital status, income, household composition.
- **Store Engagement:** enrollment date at store, number of days since last purchase at store, whether a customer has raised complaints in the past two years.
- **Purchase Behavior:** amount spent in the past 2 years on wine, fruit, meat products, fish products, sweet products and gold.
- **Promotion Response:** number of purchases made with a discount and whether a customer has accepted a campaign.
- **Channel Engagement:** Frequency of purchases made via the web, catalog, and physical stores, along with website visit frequency.

### Data Set Limitations
This dataset has 2240 rows and 29 attributes - it is mostly clean. The following are limitations found on the dataset:
- **Missing income data:** 24 out of 2,240 rows don’t have an income value.
- **Limited transaction history:** The dataset covers spending from the last 2 years, but it lacks detailed transaction data such as purchase dates, individual transaction amounts, channel purchased through, etc.
- **Limited demographic information:** No gender or location.

### Risks and Uncertainties
The following are risks and uncertainties we have about the dataset:
- **Data Set Size and Limitations:** The dataset consists of only 2,240 records, which may limit model performance and generalizability.
- **Model Generalization:** Clustering and predictive models might not generalize well across customer groups.
- **External Factors:** Economic changes, seasonal trends, or competitive actions could influence customer behavior in ways not captured by historical data.

## Methods & Technologies

### Exploratory Data Analysis

#### Data Quality Assessment, Cleaning, and Transformations
The following data cleaning and transformations were conducted on the dataset:
- Missing values were handled, duplicates were removed, data type issues were fixed, and outliers were handled.
- Data distributions were analyzed and potential data quality issues were identified.

#### Feature Engineering
Minor feature engineering was conducted on the dataset:
- New features were created including total spend, campaign response rate, shopping frequency, household size, and customer lifetime value metrics.
- Features were scaled and analyzed to better understand their distributions and relationships. Key steps included scaling numerical features, generating a correlation matrix, and analyzing various data visualizations.

### Model Exploration and Selection

#### Clustering Models
Our approach to clustering each customer into "shopper profiles" consisted of testing out two different clustering methods, **K-means** and **DBSCAN**, and selecting the highest performing model to perform our analysis.

Our **K-means clustering model ended up being the better choice** as the clusters were more populated and evenly dispersed. The DBSCAN model had a large number of “noise points” and only a little of the data was correctly segmented.

**K-Means Clustering**
Our K-means clustering approach consisted of:
- Standardized numerical features to ensure fair comparisons.
- Determined the optimal number of clusters using the Elbow Method and Silhouette Score.
- Assigned customers to clusters based on their similarities in key behavioral and demographic features.
- Analyzed relative variance across features to identify key differentiators between clusters.
- Applied an inverse transformation to interpret cluster characteristics in their original scale for actionable insights.

**DBSCAN Clustering**
Our approach to using DBSCAN to cluster our data consisted of:
- Using the same preprocessing steps as our k-means clustering model (e.g., feature selection, standardization, etc.)
- Calculating a silhouette score and a Davies-Bouldin score to evaluate model and compare to our k-means clustering model.
- Calculated cluster distribution and evaluated model stability to determine whether the model was worth using as the final clustering model.

For more details on our DBSCAN clustering model, please look at <mark>[x]<mark> in our repo.

#### Predictive Models
We conducted, evaluated and compared two predictive models, Logic Regression and Random Forest Classification. The same process of splitting data into training and testing sets, standardizing data and using SMOTE was used for both predictive models.
- Split data into training (80%) and testing (20%) sets using train_test_split.
- Apply StandardScaler to normalize numerical features for fair comparisons.
- Use SMOTE (Synthetic Minority Oversampling) to balance class distribution and improve the model’s ability to predict minority classes (responders).

**Logistic Regression Model**
- Trained with C=0.1 for L2 regularization.
- Optimized using GridSearchCV for best hyperparameters.
- Focuses on predicting responders correctly (recall-focused).

**Random Forest Classifier**
- Uses 100 trees, max depth = 10, max features = "sqrt".
- Class weights balanced to handle the imbalance issue.
- Tuned using GridSearchCV.
- Prioritizes precision (reducing false positives).

### Pipeline Automation
After completing our project, we compared the manual vs. automated (pipeline-based) approach to preprocessing and clustering with K-means. Our goal was to assess the impact of automation on efficiency, consistency, and model performance.

The following steps were taken for the pipeline automation approach: 
- Features were split into numerical and categorical categories. Features to drop and passthrough were identified.  
- All preprocessing steps were chained together in a single object to ensure that steps were applied sequentially and uniformly across the dataset. 

<mark>[INSERT IMAGE]<mark>

We noticed that there were several benefits to this approach: 
1. **Enhanced scalability:** The same pipeline could be reused for new datasets without re-writing code.
2. **Better Efficiency:** Automated transformations reduced processing time and human intervention.
3. **Improved Consistency:** Ensured all preprocessing steps were applied uniformly across the dataset.

We plan to continue working on refining the pipeline and automating the steps.

For more details on our pipeline automation, please look at <mark>[x]<mark> in our repo.

## Key Findings & Conclusion
### Exploratory Data Analysis
Our EDA found the following insights about high-value shoppers and budget-conscious shoppers:
- High-value shoppers
  - Have strong correlations between income, total spending, and shopping frequency.
  - Spend generously.
  - Respond well to campaigns, making them ideal for premium offers. 
- Budget-conscious customers
  - Often larger families with lower income.
  - Spend less, but visit the website frequently, suiting them for discounts and online deals.
These insights suggest that marketing should target **high-value shoppers with campaigns** and offer **tailored promotions for budget-conscious shoppers** to maximize engagement and sales.

Below is a comprehensive correlation matrix of customer features.

<mark>[INSERT IMAGE]<mark>

For more details on our EDA, please look at <mark>[x]<mark> in our repo.

### Deep Learning Modeling
#### K-Means Clustering
After a thorough exploration of different clustering models and approaches, we decided to use a **K-means clustering model without a pipeline.** Our clustering model identified five distinct customer segments - differentiated by spending patterns, income levels, discount dependency, household size, campaign responsiveness, and web engagement. The following details each segment's key features, distribution (proportion in train and test datasets), insights, and actionable business takeaways as well as general observations from our clustering model results.

**Cluster 3: Discount-Driven Family Shoppers**
**Key Features:** Low spending ($187), low purchase frequency (7.80), high discount dependency (0.39), moderate-income ($42,709), largest households (3.50), low campaign response (4.0%), low complaints (0.009), high web visits (6.26).
**Distribution:** Train: 25.30%, Test: 29.93%. (most common).
**Insight:** The largest cluster, these price-sensitive customers rely heavily on discounts and have bigger households, driving lower per-person spending. High web visits reflect active deal-seeking behavior.
**Business Takeaway:** Prioritize frequent online promotions and family-oriented deals to retain this dominant segment. Leverage their high web activity with targeted online promotions.

**Cluster 2: Budget-Conscious Low Spenders**
**Key Features:** Very low spending ($112), low purchase frequency (6.08), high discount dependency (0.32), low income ($29,698), moderate household size (2.44), very low campaign response (3.2%), higher complaints (0.013), high web visits (6.93).
**Distribution:** Train: 25.81%, Test: 26.76% (2nd most common).
**Insight:** This large group spends the least, constrained by low income and reliant on discounts. Frequent web visits suggest they're hunting for value, while slightly higher complaints indicate some dissatisfaction.
**Business Takeaway:** Offer low-cost products and aggressive online discounts, addressing complaints to improve retention.

**Cluster 4: Stable Middle-Income Spenders**
**Key Features:** High spending ($1,046), moderate purchase frequency (18.26), low discount dependency (0.08), high income ($72,202), smaller households (2.04), low campaign response (4.0%), low complaints (0.008), low web visits (2.49).
**Distribution:** Train: 21.67%, Test: 19.27% (3rd most common).
**Insight:** This segment spends steadily with high income and minimal reliance on discounts or campaigns, suggesting they value quality or habit over deals. Their low web activity indicates a preference for traditional shopping channels (e.g., in-store).
**Business Takeaway:** Maintain their loyalty with consistent, quality-focused offerings through offline channels.

**Cluster 0: Engaged Middle-Income Spenders**
**Key Features:** High spending ($964), high purchase frequency (18.91), moderate discount dependency (0.16), solid income ($60,267), moderate household size (2.53), low campaign response (6.4%), very low complaints (0.006), moderate web visits (5.82).
**Distribution:** Train: 19.12%, Test: 16.55%. (4th most common).
**Insight:** These customers are active spenders with a slightly higher responsiveness to campaigns compared to Cluster 0. They're middle-income with moderate online engagement. Their discount dependency is low-to-moderate, suggesting they're selective but not entirely price-driven.
**Business Takeaway:** Target this group with tailored campaigns (since they've shown some responsiveness) and enhance their online experience to boost web purchases, given their moderate web activity.

**Cluster 1: Affluent High-Spending Responders**
**Key Features:** Very high spending ($1,593), high purchase frequency (19.70), low discount dependency (0.06), highest income ($80,686), smallest households (1.71), very high campaign response (45.9%), low complaints (0.007), low web visits (3.34).
**Distribution:** Train: 8.11%, Test: 7.48% (least common).
**Insight:** The smallest cluster, these affluent customers spend heavily, respond strongly to campaigns, and don't rely on discounts. Small households and low web visits point to a focus on quality and offline shopping.
**Business Takeaway:** Invest heavily in personalized campaigns (e.g., exclusive offers, loyalty rewards) for this group, as they're highly responsive and profitable. Focus on offline channels like catalogs or in-store experiences.

**General Observations**
- **Uniform Features Across Clusters:**
  - **Age:** Ranges narrowly from 47 to 60, averaging around 53–59 for most clusters mean, indicating a mature customer base with little age-driven variation.
  - **Education:** Varies from 1.84 to 2.88, but most clusters hover around 2.4–2.8, suggesting a moderate-to-high education level with minor differentiation.
  - **Recency:** Consistently 47–50 days across all clusters, showing similar purchase timing and no significant recency-based segmentation.
  - **Loyalty (Months):** Ranges from 138 to 147, averaging 139–143 for most, reflecting a highly loyal customer base with little variation.
  - **Implication:** These features don't strongly influence cluster separation, suggesting a demographically stable, loyal population where behavior (spending, discounts, campaigns) drives differences.
- **Spending vs. Income:** Spending aligns closely with income levels—Cluster 1 (highest income) spends the most, while Cluster 2 (lowest income) spends the least. This suggests income is a key driver of purchasing power.
- **Discount Dependency:** Lower-income clusters (2 and 3) rely heavily on discounts, while higher-income clusters (0, 1, 4) are less price-sensitive, offering opportunities for differentiated pricing strategies.
- **Campaign Responsiveness:** Cluster 1 stands out as highly responsive to campaigns, while others show low engagement. This highlights the potential for targeted marketing to unlock value in specific segments.

For more details on our K-means clustering model, please look at <mark>[x]<mark> in our repo.

#### Predictive Modeling
To provide additional business value from our dataset analysis, we also conducted predictive modeling on our dataset to determine how likely a customer would respond to a future marketing campaign.

Our predictive models predict customer response to marketing campaigns by using **Logistic Regression** and **Random Forest Classifier.**
- **Logistic Regression:** used because it is a simple and interpretable binary classification model that estimates the probability of a customer responding to a campaign
- **Random Forest Classifier:** is an ensemble learning method that reduces overfitting and improves accuracy by averaging multiple decision trees.

**Additional Preprocessing and Feature Engineering**
The dataset was first further preprocessed by removing irrelevant columns, handling missing values, and encoding categorical variables. Additional feature engineering was applied by creating new features like Total Spending, Discount Dependency, and Loyalty Months to capture customer behavior more effectively.

To ensure fair model training, StandardScaler was used to normalize numerical features, making sure that features with different units or scales did not dominate the model. Additionally, because the dataset was imbalanced (i.e., there are more non-responders than responders) SMOTE (Synthetic Minority Oversampling Technique) was applied to balance the dataset by generating synthetic samples for the minority class (responders). This helped prevent the model from biasing towards the majority class (non-responders) and improved its ability to detect actual responders.

**Hyperparameter Tuning**
Once the data was processed, GridSearchCV was used to tune hyperparameters for both models, ensuring optimal performance. The trained models were then evaluated using accuracy, precision, recall, F1-score, and ROC AUC score to measure their effectiveness. Confusion matrices were plotted to visually assess the number of true positives, false positives, true negatives, and false negatives. The results indicated that while Logistic Regression had better recall (finding more actual responders), Random Forest Classifier provided better precision (more confident positive predictions). The combination of scaling, SMOTE, and hyperparameter tuning enhanced the predictive power of the models, ensuring a more effective marketing campaign strategy.

Below are the individual and comparisons of each model's performance and key findings.

**Logic Regression vs. Random Forest Classifier Performance**

<mark>[INSERT IMAGE]<mark>

**Logic Regression**

<mark>[INSERT IMAGE]<mark>

<mark>[INSERT IMAGE]<mark>

**Key findings from our Logistic Regression Model:**
1. High True Negative Rate (315 True Negatives)
- The model correctly identified 315 customers who did not respond to the marketing campaign.
- This suggests that the model is good at recognizing non-responders, which is beneficial for reducing wasted marketing efforts.
2. Moderate False Positive Rate (60 False Positives)
- The model incorrectly predicted 60 customers as responders when they actually did not respond.
- This means the campaign could target some customers who are unlikely to respond, potentially leading to inefficient marketing resource allocation.
3. Strong Recall for Responders (52 True Positives)
- The model correctly predicted 52 actual responders, meaning it effectively captures a large portion of customers who will respond.
- This is valuable because identifying actual responders helps in maximizing marketing impact.
4. False Negatives (14 Missed Responders)
- There are 14 customers who would have responded but were misclassified as non-responders.
- These potential customers might be missed opportunities if marketing efforts are not extended to them.

**Random Forest Classifier Model**

<mark>[INSERT IMAGE]<mark>

<mark>[INSERT IMAGE]<mark>

**Key findings from our Random Forest Classifier Model:**
1. Very High True Negative Rate (361 True Negatives)
- The model correctly predicted 361 customers who did not respond to the campaign.
- This indicates strong performance in identifying non-responders, minimizing wasted marketing efforts.
2. Significantly Lower False Positives (14 False Positives)
- The model incorrectly predicted 14 non-responders as responders, much lower than the logistic regression model.
- This means fewer marketing resources are wasted on people unlikely to respond, improving efficiency.
3. Lower Recall for Responders (37 True Positives)
- The model correctly identified 37 actual responders, which is lower than the logistic regression model.
- This suggests Random Forest is more conservative and less likely to classify a customer as a responder, potentially missing some real responders.
4. Higher False Negatives (29 Missed Responders)
- There are 29 customers who actually responded but were misclassified as non-responders.
- This means that some potential responders might not receive marketing efforts, leading to lost opportunities.

**Comparison of Confusion Matrices**

<mark>[INSERT IMAGE]<mark>

**Final Evaluation and Comparison of Both Predictive Models**
Based on our predictive models, it is possible to predict whether people will respond to marketing campaigns using machine learning models. Both Logistic Regression and Random Forest Classifier demonstrated the ability to classify customer responses based on behavioral, demographic, and transactional features. While Logistic Regression showed higher recall, making it effective for identifying a larger portion of actual responders, Random Forest achieved higher precision, making it more suitable for targeting the most likely responders with minimal error. These results indicate that predictive models can support data-driven marketing strategies by forecasting customer behavior with a reasonable degree of accuracy and confidence.

For more details on our predictive modeling, please look at <mark>[x]<mark> in our repo.

## Conclusion
Our project provides businesses with a powerful tool to enhance their marketing strategies through a deep understanding of customer shopping personalities. By using K-Means clustering to segment customers into distinct profiles and leveraging predictive models like logistic regression and random forest classifiers, we have enabled businesses to identify high-potential customer segments.

These insights allow for more targeted, personalized marketing campaigns that are more likely to engage customers and drive sales.Additionally, by optimizing marketing resources and focusing efforts on the most responsive profiles, businesses can significantly improve their ROI. Ultimately, this project equips businesses with the knowledge to refine their marketing strategies, leading to stronger customer relationships and increased business success. 

The ability to engage customers based on their individual preferences is a key differentiator in today’s competitive market. Through this analysis, businesses can create more meaningful and effective interactions that drive long-term growth.

### Key Business Takeaways
- **Product Customization:** Develop premium products for “Affluent High-Spending Responders” and affordable, discount-friendly options for “Budget-Conscious Low Spenders” and “Discount-Driven Family Shoppers”.
- **Marketing Strategy:** Allocate campaign budgets toward “Affluent High-Spending Responders” for maximum ROI, while using frequent online promotions for “Budget-Conscious Low Spenders” and “Discount-Driven Family Shoppers”. “Engaged Middle-Income Spenders” and “Affluent High-Spending Responders” may benefit from loyalty programs over aggressive marketing.
- **Channel Optimization:** Enhance the website for deal-hunters (“Budget-Conscious Low Spenders” and “Discount-Driven Family Shoppers”) and invest in catalog/in-store experiences for “Affluent High-Spending Responders”.
- **Customer Retention:** Address “Budget-Conscious Low Spenders”s slightly higher complaint rate to prevent churn, and reward  “Affluent High-Spending Responders”'s responsiveness with exclusive perks.

## Team Information
### Team Members
Team Member | GitHub | Email | Role & Responsibilities | Video
--- | --- | --- | ---  | ---
Fan(Echo) Yu | [echooocc](https://github.com/echooocc) | echo2go@gmail.com | <mark>[x]<mark> | <mark>[link to video]([x])<mark> |
Kevin Lu | [kevinlutoronto](https://github.com/kevinlutoronto) | kevin.lu.toronto@gmail.com  | <mark>[x]<mark> | <mark>[link to video]([x])<mark> |
Lauren Tonello | [ltonello](https://github.com/ltonello) | lauren.tonello@gmail.com | <mark>[x]<mark> | <mark>[link to video]([x])<mark> |
Oi Yee(Frances) Chung | [franceschung](https://github.com/franceschung) | frances.chungoy@gmail.com | <mark>[x]<mark> | [[x]](https://youtu.be/MoLlZbpndkA?si=z3zhL3gwGWH_g5XU) |
Shraddha Yeolekar | [shyeolekar5](https://github.com/shyeolekar5)| shraddha.goyani@gmail.com | <mark>[x]<mark> | <mark>[link to video]([x])<mark> |

## Team's Approach to Collaboration
Our team’s approach to collaboration was centered around all project decisions and results being discussed as a team, but working individually on heads-down work to improve concentration and efficiency. We divided tasks such as exploratory data analysis (EDA), pipeline automation, and modeling, allowing each team member to work independently on their respective sections. After completing each phase, we came together to review the results and decide on the next steps. All approaches, findings, and results were shared and discussed among the team before making any decisions or moving forward. This ensured alignment, transparency, and collective input throughout the process.
