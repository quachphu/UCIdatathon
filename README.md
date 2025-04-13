# Uber Driver Conversion Prediction

## Project Overview

This project analyzes a dataset of 54,681 Uber driver signups to predict which drivers are likely to complete their first trip (convert). Only 11.22% of driver signups ever complete their first trip, representing a significant opportunity to improve conversion rates and reduce acquisition costs.

By building machine learning models and conducting thorough exploratory analysis, this project:
- Identifies key factors that determine driver conversion
- Builds predictive models to identify high-potential drivers
- Provides actionable recommendations to improve conversion rates
- Estimates the business impact of implementing these recommendations

## Dataset Description

The dataset contains information about driver signups from January 2016, with data pulled a few months later to include whether drivers completed their first trip. Each record represents a driver signup with the following attributes:

| Column | Description |
|--------|-------------|
| id | Unique driver identifier |
| city_name | City where the driver signed up |
| signup_os | Device OS used for signup ("android", "ios", "website", "other") |
| signup_channel | Acquisition channel ("offline", "paid", "organic", "referral") |
| signup_date | Date of account creation (format: 'YYYY MM DD') |
| bgc_date | Date of background check consent (format: 'YYYY MM DD', 'NA' if not completed) |
| vehicle_added_date | Date when vehicle information was uploaded (format: 'YYYY MM DD', 'NA' if not completed) |
| vehicle_make | Make of vehicle uploaded (e.g., Honda, Ford, Kia) |
| vehicle_model | Model of vehicle uploaded (e.g., Accord, Prius, 350z) |
| vehicle_year | Year the car was made (format: 'YYYY') |
| first_completed_date | Date of first trip as a driver (format: 'YYYY MM DD', 'NA' if no trip completed) |

**Note:** Missing values are represented as 'NA' strings in the dataset, not actual null values.

## Requirements

This project requires Python 3.7+ and the following packages:
```
pandas==1.3.4
numpy==1.21.4
matplotlib==3.5.0
seaborn==0.11.2
scikit-learn==1.0.1
```

You can install all requirements with:
```bash
pip install -r requirements.txt
```

## Analysis Approach

1. **Data Cleaning and Preprocessing**:
   - Handling 'NA' values in date fields
   - Creating binary target variable for first trip completion
   - Converting dates to datetime format
   - Creating flags for completed onboarding steps

2. **Exploratory Data Analysis**:
   - Analyzing onboarding funnel and dropout rates
   - Calculating conversion rates by various segments
   - Examining time relationships between signup and key milestones

3. **Feature Engineering**:
   - Creating completion status flags for key onboarding steps
   - Encoding categorical variables
   - Generating time-based features
   - Creating interaction terms

4. **Model Development**:
   - Logistic Regression for interpretability
   - Random Forest for handling non-linear relationships
   - Gradient Boosting for maximizing predictive performance
   - Simple rule-based model as a baseline

5. **Model Evaluation**:
   - Train/test split validation
   - Accuracy, precision, recall, and F1 score metrics
   - Confusion matrices
   - Feature importance analysis

## Key Findings

1. **Onboarding completion is critical**:
   - Both BGC and vehicle completed: 45.59% conversion
   - Only BGC completed: 1.32% conversion
   - Only vehicle added or neither step: 0% conversion

2. **Time sensitivity is crucial**:
   - Same day BGC completion: 42.10% conversion
   - 1-3 days: 31.10% conversion
   - 4-7 days: 19.04% conversion
   - 8-14 days: 9.67% conversion
   - 15+ days: 2.45% conversion

3. **Acquisition channel matters**:
   - Referral: 19.89% conversion
   - Organic: 9.01% conversion
   - Paid: 6.19% conversion

4. **Signup platform influences conversion**:
   - Mac: 16.28% conversion
   - Windows: 13.25% conversion
   - iOS web: 13.17% conversion
   - Android web: 9.73% conversion

5. **Feature importance (Logistic Regression)**:
   - bgc_completed: 5.55
   - has_vehicle_info: 2.74
   - vehicle_added: 2.17

## Model Performance

Our best-performing model achieved:
- Accuracy: 92.93%
- Precision: 70.07%
- Recall: 65.13%
- F1 Score: 67.51%

The high recall indicates we successfully identify the vast majority of drivers who will take their first trip.

## Business Recommendations

Based on model insights, we recommend:

1. **Focus on completing both onboarding steps**:
   - Simplify vehicle addition process
   - Create clear onboarding progress tracker
   - Target interventions for drivers who completed BGC but not vehicle info

2. **Optimize for quick background checks**:
   - Conversion drops dramatically when BGC takes more than 3 days
   - Implement urgent follow-up for drivers with delayed BGC

3. **Expand the referral program**:
   - Referrals convert at ~20% vs ~6% for paid channels
   - Reallocate budget from paid to referral incentives

4. **Implement real-time prediction and intervention**:
   - Score drivers daily and flag those at risk
   - Deploy targeted interventions based on model predictions
   - A/B test different incentives for at-risk segments

## Expected Impact

Implementing these recommendations could:
- Increase overall conversion rate from 11.22% to 16-18%
- Reduce average time to first trip by 30-40%
- Decrease cost per converted driver by 20-25%
- Improve driver supply in key markets by 15-20%

## Future Work

1. **Real-time scoring system** for new driver signups
2. **A/B testing framework** for intervention validation
3. **Enhanced feature engineering** with additional data sources
4. **Dynamic model updates** with continuous retraining
5. **Personalized intervention optimization** based on driver characteristics

## Acknowledgements and Presentation Slide 

This dataset was provided as part of a take-home assignment in the recruitment process for data science positions at Uber. The analysis and models are for educational purposes.

Presentation Slide : https://docs.google.com/presentation/d/1X3fqHPpnkzPW_yd7OMVyDSamq9uDRc9s0ZLmzXUB5Hs/edit?usp=sharing

DevPost Link : https://devpost.com/software/zotzotzot-predicting-driver-activation/joins/DITk_wOi4PpacQiDfKwYvQ

Deep Note : https://deepnote.com/workspace/Gary-20031a52-8762-4423-8108-a8cf79af7426/project/Datathon-2025-d0319f7c-57fc-43b6-be9a-9141d1afb87b/notebook/a4c989398d63422791a244f330e1b77f
