# Indian-Import-Export-Data-Analysis

## Model 
Forecasting values based on last 12 months trade amount, we predicted trade amount for last 13 months ie from Jan, 2019 till Jan, 2020.
### Model Architecture
Both models have same architecture : LSTM(200) --> LSTM(200) --> LSTM(150) --> DENSE(1)
### Import Model
RMSE = 2637.71
### Export Model
RMSE = 2043.39
