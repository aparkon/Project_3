from hydralit import HydraApp
import streamlit as st
from DawglyHome import HomeApp
from BecomeAminter import MinterApp
from SearchforToken import TokenApp



if __name__ == '__main__':
    #over_theme = {'txc_inactive': '#FFFFFF'}
    #this is the host application, we add children to it and that's it!
    app = HydraApp(title='Dawgly App',favicon="?")
    #app = HydraApp(title='Secure Hydralit Data Explorer',favicon="?",navbar_theme=over_theme,hide_streamlit_markers=True,use_navbar=True, navbar_sticky=True)
  
    #add all your application classes here
    app.add_app("Dawgly Home", icon="?", app=HomeApp())
    app.add_app("Minter",icon="?", app=MinterApp())
    app.add_app("Token",icon="?", app=TokenApp())
    #app.add_app("Contract", icon="?", app=contApp())
    #app.add_app("Signup", icon="?️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)
    #app.add_app("Login", apps.LoginApp(title='Login'),is_login=True)
    
    #run the whole lot
    app.run()
    

    