import streamlit as st
import pickle
import numpy as np
import pandas as pd


def show_general_page():
    st.title("Bangalore Home Price Prediction")
    st.write(
        "This web app has been created to help brokers, property dealers and general public to predict prices in and around different Bangalore locations. We take basic parameters to predict the house prices. Below we have listed the parameters which we consider for house prediction. "
    )

    st.subheader("\n\nLocation")
    st.write(
        """A specific location in Bangalore where you are looking for the house."""
    )

    st.subheader("\n\nArea in Square Feet")
    st.write(
        """The total area of the house in sqaure feet (Standard property measurement unit)."""
    )

    st.subheader("\n\nBathroom")
    st.write("""Number of bathrooms present in the house.""")

    st.subheader("\n\nBedroom Hall Kitchen (BHK)")
    st.write("""Indicates the number of bedrooms, hall and kitchen in the apartment.""")
