
import streamlit

streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favoriates')
streamlit.text('\N{bowl with spoon}	Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{leafy green} Kale, Spinage & Rocket Smoothie')
streamlit.text('\N{chicken} Hard-boiled Free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's Put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
