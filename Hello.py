import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.let_it_rain import rain 

LOGGER = get_logger(__name__)

st.set_page_config(
    page_title="Rolled Up",
    page_icon="💨",
    layout="wide"
    )
def example():
    rain(
        emoji="💸",
        font_size=54,
        falling_speed=5,
        animation_length=15,
    )
example()    
st.image("https://i.postimg.cc/pVqgbMcY/DRC-PRINTS-FIRE.jpg", use_column_width=True)