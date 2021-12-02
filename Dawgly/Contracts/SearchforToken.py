import os
import streamlit as st
from hydralit import HydraHeadApp
from pathlib import Path
import json
from streamlit.elements.number_input import Number
from dotenv import load_dotenv
import inspect
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3, contract
from dawgly_wallet import generate_account, get_balance, send_transaction

load_dotenv()

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))



#create a wrapper class
class TokenApp(HydraHeadApp):
    def run(self):
        
        st.markdown("# Best dog care givers are waiting for you!")
        
        minter_database = {
            "Alex":["Alex", "0x9c9738Ef1308480c0da3E1D83861Db47E7604182", "5.0", 1,"?","?"],
            "Bailey":["Baiyley", "0x5b57Ca93e29631f22408CC4Cdf7AD5946c5368E5", "5.0", 2,"?","?"],
            "Jose":["Jose", "0x9d11E92Ae404DEEb04d0A4dbd98C2bD1B795972d", "4.8", 2,"?","?"],
            "Kian":["Kian", "0x3B025372E0B3b5420335b5c2307C98aD68FADbf5", "4.8", 2,"?","?"],
            "Melaku":["Melaku", "0x1faBbBd7D5b1Fbe397F54D491420939D84E4c352", "4.7", 1,"?","?"]
        }

        minters = ["Alex","Bailey","Jose","Kian","Melaku"]
        def get_minter():
           
            minter_list = list(minter_database.values())
            
            for number in range(len(minters)):
                st.write("Name: ", minter_list[number][0])
                #st.write("Ethereum Account Address: ",db_list[number][1])
                st.write("Dawgly Rating: ",minter_list[number][2])
                st.write("Token Rate per Ether: ", minter_list[number][3], "eth")
                st.date_input("Select Available dates")
                available_token = st.number_input('Available Hours')
                st.write("You have", available_token, "Tokens")
                #st.number_input("Available tokens")
                st.text(" \n")

       
        st.markdown("## Minters list")
        #st.text("\n")

        st.sidebar.markdown("## Token shop")
        # account = generate_account(w3)

        # #st.sidebar.markdown(account.address)

        # ether = get_balance(w3, account.address)
        # if st.sidebar.button("check your balance"):
        #     st.sidebar.markdown("Your Account Balance Is:")
        #     st.sidebar.markdown(ether)

        dog_size = st.sidebar.selectbox('What is the size of your dog?', ['Small: < 20lbs', 'Medium: 20-50 lbs', 'Large: 50+ lbs'])
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
        
        service = ['Walk', 'Feed', 'Appointment']
        
        select_service = st.sidebar.selectbox('Service?', service)
        
        @st.cache(suppress_st_warning=True)
        def cost(select_service, time):
            price = 0
            if select_service == 'Walk':
                price = 10
                total_cost = price * time + dog_price
                st.sidebar.write('The total cost for your desired service is $', round(total_cost, 2), '.')
            elif select_service == 'Feed':
                price = 5
                total_cost = price* time + dog_price
                st.sidebar.write('The total cost for your desired service is $', round(total_cost, 2), '.')
            elif select_service == 'Appointme t':
                price = 15
            total_cost = price * time + dog_price
            st.sidebar.write('The total costs for your desired service is $', round(total_cost, 2), '.')

            if st.sidebar.button('Show Total Cost'):
                cost(select_service, time)

        #Select date of service
        st.sidebar.header("Please pick date and time")
        start_date = st.sidebar.date_input('Start date?')
        end_date = st.sidebar.date_input('End date?')
        
        #Start time of service?
        start_time = st.sidebar.time_input('Start time?')
        end_time = st.sidebar.time_input("End time?")

        #Select length of service
        token = st.sidebar.number_input('Length of Service? (Whole numbers only)')

        
        person = st.sidebar.selectbox('Select a Minter', minters)

        #token = st.sidebar.number_input("Number of Tokens")

        st.sidebar.markdown("## You piked")

        minter = minter_database[person][0]

        st.sidebar.markdown(minter)

        Token_rate = minter_database[person][3]
        
        st.sidebar.markdown("## Token rate per ether is:")

        st.sidebar.markdown(Token_rate)

        minter_address = minter_database[person][1]

        #st.sidebar.markdown(minter_address)

        st.sidebar.markdown("## Total amount of Ether claimed")

        price = (minter_database[person][3]) * token

        st.sidebar.markdown(price)
        # if st.sidebar.button("send Transaction"):
        #     minter(available_token) = (minter(available_token) - token
       
        account = generate_account(w3)

        #st.sidebar.markdown(account.address)

        ether = get_balance(w3, account.address)
        if st.sidebar.button("check your balance"):
            st.sidebar.markdown("Your Account Balance Is:")
            st.sidebar.markdown(ether)


        if st.sidebar.button("Send Transaction"):
            transaction_hash = send_transaction(account, minter_address, price )
            st.sidebar.markdown("#### Validated Transaction Hash")
            st.sidebar.markdown(transaction_hash)
            #minter(available_token) = minter(available_token) - token

        get_minter()

        # contract loader function
        @st.cache(allow_output_mutation=True)
        def load_contract():
            with open(Path('./Contracts/Compiled/dawglyToken_abi.json')) as f:
                dawglyToken_abi = json.load(f)

            contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

            contract = w3.eth.contract(
                address=contract_address,
                abi=dawglyToken_abi
            )

            return contract

        contract = load_contract()


        st.title("Minting Dawgly Token")
        accounts = w3.eth.accounts
        address = (minter_database[person][2])
        address = st.selectbox("Select Artwork Owner", options=accounts)
        artwork_uri = st.text_input("The URI to the Token")
    

        if st.button("Dawgly Token Minted"):
            tx_hash = contract.functions.mint(address, artwork_uri).transact({
                "from": address,
                "gas": 1000000
        })
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
        st.markdown("---")


            ######################
        st.markdown("## Display Token")

        select_address = st.selectbox("Select Account", options=accounts)
        tokens = contract.function.balanceOf(select_address).call()
        st.write(f"This address awns {tokens} tokens")
        token_id = st.selectbox("Dawgly Tokens", list(range(tokens)))
        if st.button("Display"):
            owner = contract.functions.ownerOf(token_id).call()
        st.write(f"The token is registerd to{owner}")
        token_uri = contract.functions.tokenURI(token_id).call()
        st.write(f"The tokenURI is {token_uri}")
        st.image(token_uri)



    
   