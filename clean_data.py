import pandas as pd
import numpy as np

csv_path = ("btc_4h_price.csv")

def load_and_clean(csv_path):
    df = pd.read_csv(csv_path)

    print(df.info())
    print(df.head())

    #print(df.loc[[4,1],["Price","Close","High","Low","Open"]])

    print("-----------------------------------------------------------------------------------------------------------------")

    df = df.iloc[2:].reset_index(drop=True)

    # แปลง type
    df = df.rename(columns={"Price":"Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df["Datetime"] = df["Datetime"].dt.tz_localize(None)
    price_cols = ["Open", "High", "Low", "Close", "Volume"]
    df[price_cols] = df[price_cols].astype(float)

    # เรียงตามเวลา (ไม่ต้องก็ได้)
    df = df.sort_values("Datetime").reset_index(drop=True)

    df["is_zero_volume"] = (df["Volume"] == 0).astype(int)
    df["log_volume"] = np.log1p(df["Volume"])
    for lag in range(1, 7):
        df[f"Close_lag_{lag}"] = df["Close"].shift(lag)

    #เพิ่ม feature
    df["vol_ma_20"] = df["Volume"].rolling(20).mean()
    df["vol_ratio"] = df["Volume"] / df["vol_ma_20"]

    df = df.dropna().reset_index(drop=True)

    print(df)
    print(df.info())

    return df

#run
# load_and_clean(csv_path)