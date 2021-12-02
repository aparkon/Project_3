import os
import json
from hydralit import HydraHeadApp
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from SearchforToken import TokenApp


w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

#create a wrapper class
class contApp(HydraHeadApp):
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
        tokens = contract.function.balanceOf(selected_address).call()
        st.write(f"This address awns {tokens} tokens")
        token_id = st.selectbox("Dawgly Tokens", list(range(tokens)))
        if st.button("Display"):
            owner = contract.functions.ownerOf(token_id).call()
        st.write(f"The token is registerd to{owner}")
        token_uri = contract.functions.tokenURI(token_id).call()
        st.write(f"The tokenURI is {token_uri}")
        st.image(token_uri)

