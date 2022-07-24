import streamlit as st
import pandas as pd
from PIL import Image
# data = pd.read_csv('C:\\Users\\RONAK\\PycharmProjects\\ml car ride project\\heart.csv')
# st.title('hello')
# st.header('hello')
# st.subheader('hello')
# st.write('agwrgwrgwqg') # for text wrighting
# st.text('text')
# st.markdown("""
#h1tag<br>
##h2tag<br>
# :moon:<br>
# :sunglasses:""",True)
# for display data
# st.write(data)
# #st.dataframe(data) alternate
# # st.table(data) # it do not have scroll option
# x=data[['age']]
# st.bar_chart(x)
# import matplotlib.pyplot as px
# px.bar(data['age'],data['cp'])
# st.pyplot()
# image k liye
img=Image.open('C:\\Users\\RONAK\\PycharmProjects\\ml car ride project\\download.png')
st.image(img,width=200)
