# Classification-Project-Customer-Churn-Prediction By Miatta Sinayoko

# Project Description

 Analyzing and mitigating customer churn is a vital undertaking for any thriving business. The ability to retain existing customers before they defect is far more advantageous than attempting to win them back. It is crucial for companies to comprehend and prevent customer churn in order to secure long-term success.

The objective of this project is to employ statistical testing to examine the significant factors influencing customer churn. Furthermore, we will construct a classification model that predicts churn based on these factors. Alongside this, we will offer actionable recommendations for customer retention and deliver churn predictions for a given list of customers in CSV format. By accomplishing these tasks, we aim to empower businesses to proactively address customer churn and fortify their customer base.

# Project Goal
Find drivers for customer churn at Telco. Why are customers churning?

Construct a ML classification model that accurately predicts customer churn.

Present your process and findings to the lead data scientist



# Initial Hypothesis
Which variables are associated with churn?

Are average monthly charges higher for customers who churn?

Are tenure shorter for customer who churn?

Are additional services independent with churn?

# Project Plan 
1. Data Acquisition
Gather data from Codeup database
acqure.py
2. Data Preparation
Data Cleaning
Data Splitting
3. Exploratory Analysis
Ask questions to find what are the key variables that are driving the churn

Gather and sort churn rate from each driver into .xlsx file

Import churn_rates.xlsx and store the data in the form of dataframe

Create visualizations for the churn rate for each variable

Explore each feature's dependency with churn and create visualization for each

4. Statistical Testing & Modeling
Conduct T-Test for categorical variable vs. numerical variable

Conduct Chi^2 Test for categorical variable vs. categorical variable

Conclude hypothesis and address the initial questions

5. Modeling Evaluation
Create decision tree classifer and fit train dataset

Find the max depth for the best performing decision tree classifer (evaluated using classification report, accuracy score)

Create random forest classifier and fit train dataset

Find the max depth for the best performing random forest classifier (evaluated using classification report, accuracy score)

Create KNN classifier and fit train dataset

Find the k for the best performing KNN classifier (evaluated using classification report, accuracy score)

Create logistic regression model and fit train dataset

Find the parameter C for the best performing logistic regression model (evaluated using classification report, accuracy score)

Pick the top 3 models among all the models and evaluate performance on validate dataset

Pick the model with highest accuracy and evaluate on test dataset


# Data Dictionary
# Data Dictionary

| Variable | Value | Meaning |
|---|---|---|
| Contract Type | 1) Month-to-month 2) One year 3) Two year | Indicates the type of contractual agreement in place with the customer. |
| Device Protection | 1) Yes 2) No 3) No internet service | Indicates if the customer has device protection service. |
| Internet Service Type | 1) DSL 2) Fiber Optic 3) None | Indicates the type of internet service the customer has, if any. |
| Monthly Charges | Float number | Indicates the amount the customer is paying each month. |
| Online Backup | 1) Yes 2) No 3) No internet service | Indicates if the customer has online backup service. |
| Online Security | 1) Yes 2) No 3) No internet service | Indicates if the customer has online security service. |
| Payment Type | 1) Bank transfer 2) Credit card 3) Electronic check 4) Mailed check | Indicates how the customer is paying for service. |
| Streaming Movies | 1) Yes 2) No 3) No internet service | Indicates if the customer has streaming movies service. |
| Streaming TV | 1) Yes 2) No 3) No internet service | Indicates if the customer has streaming TV service. |
| Tenure | Integer ranging from 0-72 | Indicates the length of time (in months) the customer has stayed with the company. |



# Steps to Reproduce
 
 
### Key Findings


# Recommendations


### Next Steps
