#Importing required libraries
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import datetime 
from datetime import datetime, date, time

#Side bar: walker or user?
user_type = ['User', 'Dawgly Team Member']
st.sidebar.selectbox('Are you a sitter or a user?', user_type)

#Side bar: select your account
#accounts = w3.eth.accounts
#address = st.sidebar.selectbox('Please select your account', options =accounts)

#Customer to select their desired service
st.header('Dawgly Services')
st.write('Please select your desired Dawgly Service:')

#Select box for dog size
dog_size = st.selectbox('What is the size of your dog?', ['Small: < 20lbs', 'Medium: 20-50 lbs', 'Large: 50+ lbs'])
dog_price=0
if dog_size == 'Small < 20 lbs':
    dog_price = 5
    st.write('The fee for this dog size is $', round (dog_price, 2), '.')
elif dog_size == 'Medium: 20-50 lbs':
    dog_price = 8
    st.write('The fee for this dog size is $', round (dog_price, 2), '.')
elif dog_size == 'Large: 50+ lbs':
    dog_price = 10
    st.write('The fee for this dog size is $', round (dog_price, 2), '.')
    
#Select date of service
st.header("Please pick date and time")
date = st.date_input('Start date?')

#Start time of service?
start_time = st.time_input('Start time?')

#Select length of service
time = st.number_input('Length of Service? (Whole numbers only)')

#Select box for service to be provided 
service = ['Walk', 'Feed', 'Appointment']
select_service = st.selectbox('Service?', service)

#Cost function
@st.cache(suppress_st_warning=True)
def cost(select_service, time):
    price = 0
    if select_service == 'Walk':
        price = 10
        total_cost = price * time + dog_price
        st.write('The total cost for your desired service is $', round(total_cost, 2), '.')
    elif select_service == 'Feed':
        price = 5
        total_cost = price* time + dog_price
        st.write('The total cost for your desired service is $', round(total_cost, 2), '.')
    elif select_service == 'Appointme t':
        price = 15
        total_cost = price * time + dog_price
        st.write('The total costs for your desired service is $', round(total_cost, 2), '.')

#Button for cost of service
if st.button('Show Total Cost'):
    cost(select_service, time)


#Confirm the customer's service 
confirm_purchase = st.selectbox('Would you like to confirm your purchase?', ['Yes', 'No'])
if confirm_purchase == 'Yes':
    st.write("Purchase confirmed.")
else:
    st.write("Please re-select your desired service options.")

