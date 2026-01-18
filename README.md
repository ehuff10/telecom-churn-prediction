# Telecom Churn Prediction
by Ethan Huffman
# Project Overview
Customer churn is one of the most expensive challenges for subscription-based businesses, especially in the telecommunications industry. Acquiring a new customer often costs significantly more than retaining an existing one, making early identification of churn risk a critical business priority.
This project builds a supervised machine learning solution that predicts whether a customer is likely to churn and assigns each customer to a risk tier. The final output is designed to support real-world decision-making by enabling businesses to proactively intervene before customers leave.

# Business Understanding
Telecom companies need a reliable way to identify customers who are likely to churn so that retention teams can take targeted action. The key challenge is balancing accuracy with recall: missing a customer who is about to churn is far more costly than flagging a customer who may not.

This project prioritizes recall for churners, ensuring that high-risk customers are captured even if it results in more false positives.
# Data Understanding
The final Gradient Boosting Classifier produced 450 true positives, 41 false negatives, 780 false positives, and 657 true negatives, resulting in an overall accuracy of approximately 68 percent, churn recall of approximately 85 percent, and churn precision of approximately 43 percent. The high recall means the model successfully identifies the vast majority of customers who actually churn, while the lower precision reflects a higher number of customers flagged as at risk who would not have churned. This tradeoff was intentional because false negatives or missed churners directly result in lost revenue, whereas false positives only increase retention outreach cost, which is far less damaging to the business. Accuracy was deprioritized because in imbalanced churn data, a high accuracy model can still fail by predicting most customers as non churners and missing those who are truly at risk.
# Modeling
- Data preprocessing includes handling missing values, scaling numeric features, encoding categorical variables, and addressing class imbalance using SMOTE.
- A baseline Logistic Regression model is used for comparison.
- The final model is a Gradient Boosting Classifier, selected for its ability to capture non-linear relationships.
- A custom probability threshold is applied to align predictions with business goals.

- Customers are grouped into risk tiers (Low, Medium, High, Very High) based on predicted churn probability.
# Streamlit app
The Streamlit application allows users to:
-Enter customer information using dropdowns and numeric inputs
-Generate a churn probability and risk tier
-Simulate how the model would be used by a real retention team
- streamlit run app.py
# Reproducibility
pip install -r requirements.txt
Google Colab
This project is fully compatible with Google Colab.
Steps:
- Upload the notebook to Colab
- Run the first setup cell (which clones the repository)
- Execute all cells in order
- The notebook automatically adjusts paths when running in Colab.
telecom-churn-prediction/
# Citations
Data Sources
- IBM Telco Customer Churn Dataset
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

- BigML Telecommunications Churn Dataset
https://www.kaggle.com/datasets/mnassrib/telecom-churn-datasets

- Streamlit App Inspiration Video
 https://youtu.be/ZZ4B0QUHuNc?si=9eAn2_0imufvIJL0
This video inspired the design and structure of the Streamlit churn prediction application included in this project.

# Conclusion

