# eco_buddies_page():
"""
Display the Eco-Buddies page and provide options to add them to the chat window.

This function is responsible for displaying the Eco-Buddies page. It uses the `st.write` function 
to display the heading "Meet your Eco-Buddies!". It then reads the content of the file 
"eco_buddies_options.txt" and writes it to the page using the `st.write` function.

After displaying the Eco-Buddies page, the function provides options to add the Eco-Buddies to the chat window.

Parameters:
    None

Returns:
    None
"""
import streamlit as st
import icecream as ic
from eco_buddies import eco_buddies

