import pandas as pd
import joblib

model = joblib.load("models/model.pkl")


def predict_price(
    brand,
    cpu,
    ram,
    storage,
    screen,
    performance
):

    data = pd.DataFrame({
        "Brand": [brand],
        "CPU": [cpu],
        "RAM_GB": [ram],
        "Storage_GB": [storage],
        "Screen_Inch": [screen],
        "Performance_Score": [performance]
    })

    prediction = model.predict(data)

    return round(prediction[0], 2)

