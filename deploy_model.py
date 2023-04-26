###############################
# This program lets you       #
# - Create a dashboard        #
# - Every dashboard page is  #
# created in a separate file  #  
###############################

# Python libraries
import streamlit as st
from PIL import Image

# User module files
from eda import eda

def main():
  
    #############  
    # Main page #
    #############   
    
    options = ['Home','EDA','Stop']
    choice = st.sidebar.selectbox("Menu",options, key = '1')
    
    if ( choice == 'Home' ):            
      st.title("Welcome to the Czech bank, where your dreams can come true!!")
      st.image('images/istockphoto-1288703928-170667a.jpg')
      pass
      
    elif ( choice == 'EDA' ):
      eda()
      pass
      
    else:
      st.stop()
      
    
main()
