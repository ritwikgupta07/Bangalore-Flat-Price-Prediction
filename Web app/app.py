import streamlit as st
from predict import show_predict_page
from graphs import show_graph_page
from home import show_general_page

page = st.sidebar.selectbox("Options", ("Home", "Graphs", "Predict"))
if page == "Graphs":
    show_graph_page()
elif page == "Predict":
    show_predict_page()
elif page == "Home":
    show_general_page()
