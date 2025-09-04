# **House Price Prediction – ML Pipeline & REST API**
This project demonstrates how to build a simple Machine Learning pipeline (data preprocessing → training → evaluation), deploy it as a REST API using Flask, and test predictions with a Python client
# **Project Overview**

This project implements a machine learning pipeline to predict house prices using the Melbourne Housing Dataset. The workflow includes:

Data preprocessing (outlier removal, scaling, one-hot encoding)

Model training with LinearRegression inside a Pipeline

Model evaluation with multiple regression metrics (MAE, RMSE, R², MAPE)

Deployment of the trained model as a REST API using Flask

Testing API predictions with a Python client

This project demonstrates the complete end-to-end ML lifecycle: preprocessing → training → evaluation → deployment → monitoring.

# **Installation**
Clone the repo and set up the environment:
bash
git clone https://github.com/Wyse10/Npontu.git
cd Npontu

Create a virtual environment and install dependencies:  
bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# **How to Run the Project**
## **Start the Flask API**
Bash
python app.py

## **Test the API with Python Client**
Bash
python test.py

# **Model Evaluation**
The model was evaluated using the following metrics:
R² Score → how well the model explains variance in the data.

# **Monitoring Model Performance in Production**
Over time, model accuracy may degrade due to data drift or concept drift.
To monitor performance in production:
Track Prediction Distribution → monitor shifts in predicted prices compared to training distribution.

1.Log Real Outcomes (if available) → compare predicted vs. actual prices when real sales occur.

2.Retraining Schedule → retrain periodically (e.g., quarterly) with fresh data.

3.Monitoring Metrics → track MAE, MSE, R² over time and set thresholds for alerts.

4.Error Analysis → log and review large deviations to improve pipeline.

# **Tech Stack**
1.Python 3.10+

2.Pandas / NumPy → data preprocessing

3.Matplotlib / Seaborn → visualization & outlier detection

4.Scikit-learn → pipeline, regression model, evaluation metrics

5.Flask → REST API deployment

6.Requests → client testing