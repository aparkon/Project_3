from hydralit import HydraApp
import hydralit_components as hc
import streamlit as st


import streamlit as st
import pandas as pd
import numpy as np

#add an import to Hydralit
from hydralit import HydraHeadApp

#create a wrapper class
class MinterApp(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):
        #-------------------existing untouched code------------------------------------------
        st.markdown('Would you like to have fun with dogs by taking a good care of them?')
        st.markdown('You are at the right place, please sign up and join ower minter comunity.')
        st.title("create an account")
        st.text_input('User Name')
        st.text_input('First Name')
        st.text_input('Last Name')
        st.text_input('Email')
        st.text_input('Address')
        st.text_input('Account Number')
        st.text_area('Your Story')

        choice = st.selectbox('Please Upload Image' ,['Image', 'Camera'])
        def load_image(image_file):
	        img = "Image".open(image_file)
	        #return img
    #menu = ["Image", "Camera"]
    #choice = st.sidebar.selectbox('Image' , 'Camera')   

        if choice == "Image":
	        st.subheader("Image")
	        image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        if image_file is not None:
            
                
               # file_details = {"filename":image_file.name, "filetype":image_file.type, "filesize":image_file.size}
		           # st.write(file_details)

        # To View Uploaded Image
            st.image(load_image(image_file),width=250)
    
        if st.button("Submit"):
        #create_walkertable()
        #add_walkerdata(username= 'User Name',first_name='First Name',last_name='Last Name',email = 'Email',address='Address',account_number='Account Number',image='image_file')
            st.success("Congratulations!!")
            st.write("Now you are one of wonderful walker!!")
            st.info("Go to Login Menu to login")
