import streamlit as st
import pickle
import numpy as np
import pandas as pd


def load_model():
    with open(
        r"C:\Users\my\Desktop\KMPG Research\Bangalore Falt Prices Regression\regression_model",
        "rb",
    ) as file:
        model = pickle.load(file)
    return model


loc = pd.read_csv(
    r"C:\Users\my\Desktop\KMPG Research\Bangalore Falt Prices Regression\location.csv"
)
loc = loc["location"].to_numpy()

X = pd.read_csv(
    r"C:\Users\my\Desktop\KMPG Research\Bangalore Falt Prices Regression\bhp.csv"
)

data = load_model()
model = data["model"]


def show_predict_page():
    st.title("Prediction page")
    st.write("Provide information for prediction\n")

    location = st.selectbox("\nLocation", loc)
    sqft = st.number_input("\nArea of house (sqft)")
    bathroom = st.slider("\nNumber of bathrooms", 1, 16)
    bhk = st.slider("\nBHK", 1, 16)

    st.subheader("\n\n")
    ok = st.button("Predict Price")
    if ok:

        def predict_saved_price(location, sqft, bath, bhk):
            loc_index = np.where(X.columns == location)[0][0]
            x = np.zeros(len(X.columns))
            x[0] = sqft
            x[1] = bath
            x[2] = bhk
            if loc_index >= 0:
                x[loc_index] = 1

            return model.predict([x])[0]

        y = predict_saved_price(location, sqft, bathroom, bhk)
        st.subheader(
            "The Price of the house is expected to be around Rs.{:.2f} Lakhs".format(y)
        )
