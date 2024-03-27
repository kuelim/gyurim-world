import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

# st.sidebar.title('Sidebar title')

# st.title ("this is the app title") 
# st. header("this is the markdown")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r''' atar^1+ar2+ar^3''')



# st.image('https://cdn.imweb.me/thumbnail/20210315/9f21923ccf729.jpg')

# st.checkbox('yes')
# st.button('Click')
# gender = st.radio('Pick your gender', ['Male', 'Female'])
# st.selectbox('Pick your gender', ['Male', 'Female'])
# planet = st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
# st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
# x = st.slider('Pick a number', 0,50)

# st.write('성별',gender)
# st.write('행성', planet)

# st.number_input('Pick a number', 0,10)
# #st.text_ input('Email address') st.date_input('Travelling date')
# #st.time_input('School time')
# #st. text_area('Description"
# #st.file_uploader('Upload a photo’)
# Color = st.color_picker('Choose your favorite color')

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1,2, size=20)
fig,ax = plt.subplots()
ax.hist(rand,bins=15)
st.pyplot(fig)
