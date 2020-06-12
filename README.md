# Indian-Trade-Data-Analysis-and-Forecasting
* Trade is an economic concept which involves Buying and Selling of the commodities, or exchanging goods and services between needy people. 
* Trade is important in a way that it increases competition and decreases overall world wise cost of a product. 


## Data
* We scraped the trade dataset from Department of Commerce, Govt. of India website. 
* Monthly Trade data is available from January, 2006 to January, 2020. 
* We have total trade amount (Import/Export) for each month which is expressed in million US dollars. 
* HS Code - Harmonized System (HS) of tariff nomenclature is an internationally standardized system of names and numbers to classify traded products, e.g. 1 for Live Animal, 95 for Toys, Games and Sports Requisites …
* Data can be viewed in terms of Country wise or HS code wise.

## Model Used For Forecasting
* Exponential Smoothing
* Auto Regressive Model
* Moving Average Model
* Holt-Winters Model
* ARIMA Additive
* ARIMA Multiplicative
* ARIMA Seasonal
* RNN --> LSTM (Long Short Term Memory)

Forecasting values based on last 12 months trade amount, we predicted trade amount for last 13 months ie from Jan, 2019 till Jan, 2020.
#### Model Architecture For LSTM
Both models have same architecture : LSTM(200) --> LSTM(200) --> LSTM(150) --> DENSE(1)

## Result
![image](https://user-images.githubusercontent.com/34620833/84470802-b7b49a00-aca1-11ea-80df-615a391c68f4.png)
* Surprisingly Seasonal ARIMA outperformed LSTM in Forecasting Export Data, which shows that ARIMA captures seasonality much better than any other model, even with lesser data and randomness.
* LSTM model performed better for Import Data as expected because of it’s capability of retaining information of long period of time.
