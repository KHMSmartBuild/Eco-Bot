"""
This is the streamlit app for the eco game.
"""
# filename: eco_game_streamlit.py

import streamlit as st
import streamlit.components.v1 as components


def load_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


components.html(load_html("assets/game/index.html"))


