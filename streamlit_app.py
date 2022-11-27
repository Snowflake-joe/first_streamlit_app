
import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favoriates')
streamlit.text('\N{bowl with spoon}	Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{leafy green} Kale, Spinage & Rocket Smoothie')
streamlit.text('\N{chicken} Hard-boiled Free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
