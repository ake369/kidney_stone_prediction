## End-to-End User Interface Based ML Project for Predicting Kidney Stone Existence
This project aims to predict the possible existence of kidney stones using a lab report dataset. It features an end-to-end machine learning pipeline, starting from data preprocessing to the deployment of a user-friendly interface for prediction. The project integrates essential data science activities such as data preprocessing, feature engineering, model training, and evaluation, all wrapped in a web-based interface to enhance user interaction.
## Project Overview
## Goal
The primary objective is to develop a machine learning model that can predict the likelihood of kidney stones based on several lab test results. The prediction model is embedded within a web-based user interface that allows healthcare professionals and patients to input lab values and get instant predictions.
## Key Features:
* User Interface: A clean, responsive, and intuitive web interface that allows users to input lab values and receive predictions.
* Data Science Pipeline: Complete data science workflow, including data preprocessing, feature engineering, transformation, and model training.
* Model Evaluation: Training 10 different machine learning models and selecting the best performing one based on accuracy and other evaluation metrics.
## Project Activities
#### Data Preprocessing
* Data Cleaning: The dataset is cleaned to handle missing values, remove duplicates, and standardize data types.
* Outlier Detection: Outliers are detected and addressed to ensure model stability.
* Normalization/Standardization: The numerical features are normalized or standardized to improve model performance.
#### Feature Engineering
* Feature Selection: Important features that influence kidney stone formation (e.g., specific gravity, pH level, calcium concentration) are selected based on domain knowledge and correlation analysis.
#### Data Transformation
* Scaling: Data is scaled using techniques such as Min-Max Scaling or StandardScaler, ensuring that the features are on a comparable scale.

#### Model Training
* Model Selection: 10 different machine learning models are trained, including:
- Logistic Regression
- Random Forest
- Gradient Boosting
- Decision Tree
- XGBoost
- Adaboost
#### Cross-validation: 
- K-fold cross-validation is used to ensure robust model performance and avoid overfitting.
#### Model Evaluation and Selection
- Evaluation Metrics: The models are evaluated based on metrics such as accuracy, precision, recall, F1 score, and AUC-ROC.
- Best Model Selection: The model with the best performance based on these metrics is selected for deployment.
#### Deployment and Web Interface
- Web Interface Development: A web-based interface is created using HTML, CSS, and Flask to allow users to input lab report values.
- Prediction: The best-performing model is integrated into the web app to provide real-time kidney stone predictions based on user input.
### How to Run the Project
1. Clone the Repository:
<pre> '''git clone https://github.com/Noah369-Create/kidney-stone-prediction.git
cd kidney-stone-prediction '''
</pre>
2. Install Dependencies:
<pre> 
pip install -r requirements.txt
</pre>
