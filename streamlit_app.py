
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
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


#normalize the json from fruitvice 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output to a dataframe
streamlit.dataframe(fruityvice_normalized)
