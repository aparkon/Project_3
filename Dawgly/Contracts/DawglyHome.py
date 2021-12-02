import streamlit as st
import numpy as np
import pandas as pd
import time
import base64
from shapely.geometry import Point, Polygon
#import geopandas as gpd
import pandas as pd
import geopy



#from data.create_data import create_table

#add an import to Hydralit
from hydralit import HydraHeadApp

#create a wrapper class
class HomeApp(HydraHeadApp):
    def run(self):
        #st.title('Welcome to Dawgly!')
        
        #Side bar: walker or user?
        user_type = ['User', 'Dawgly Team Member']
        st.sidebar.selectbox('Are you a sitter or a user?', user_type)

        menu = ["Login", "SignUp", "About"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Login":
            st.subheader("Welcome to Dawgly!")

        st.image("./resources/DawglyImage.jpg", width=200)

        # username = st.sidebar.text_input("User Name")
        # password = st.sidebar.text_input("Password", type='password')
       

