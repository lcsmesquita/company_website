# Here i will need to develop a company website
# It's a task that i got delivered by the teacher of the course i am taking.

import streamlit as st
import pandas

st.set_page_config(layout='wide')
st.header("The Best Company")
#First, a need a title that is written "The best company"

#Second, i need a subtitle telling something about the company
st.write("""
         This is the space were the informations of the company should be.
         Important data like year of foundation, niche market, description
         of how the company works, and things like that.
         """)

#then i need another title that shows "Our team"
st.subheader("Our Team")
#After that, i need to show in 3 columns, the name of de person, then, 
#its function in the company, and its picture. All of that is in the data.csv and images.
col1, col2, col3 = st.columns(3)

# Reading the csv file with pandas
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(row['first name'].title() + " " + row['last name'].title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row['first name'] + " " + row['last name'])
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row['first name'] + " " + row['last name'])
        st.write(row['role'])
        st.image(f"images/{row['image']}")
