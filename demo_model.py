import joblib 
import pandas as pd
from clean_data import load_and_clean

df = load_and_clean("btc_4h_price.csv")

# Load model
loaded_model = joblib.load("D:\\User\\42Bangkok\\CapstoneProject\\crypto_project\\crypto-trading-capstone\\crypto_predict_model.pkl")

features2 = [
    "Close_lag_1", "Close_lag_2", "Close_lag_3",
    "Close_lag_4", "Close_lag_5", "Close_lag_6",
    "log_volume", "is_zero_volume", "vol_ma_20" , "vol_ratio"
]

#predict
X_new = df[features2].iloc[-1:]  
pred = loaded_model.predict(X_new)

print("-->",df[["Datetime","Open","Close"]].iloc[-1:] )
print("Predicted Close:", pred[0])