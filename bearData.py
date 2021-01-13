import pandas as pd 
import streamlit as st 
import numpy as np 
import datetime

st.title('Bear Killings')
# st.subheader('Where are you mostly to be killed by a bear')

bears = pd.read_csv('C:/Users/erhicakorf/Documents/Specno/Streamlit/north_america_bear_killings.csv')

if st.checkbox('Show data summary'):
    st.subheader('Data summary')
    st.write(bears.describe())

#
import matplotlib.pyplot as plt  
st.subheader('Ages of the number of people killed')

if st.checkbox('Show graph'):
    # radio
    genre = st.radio(
        "What's your favourite color?",
        ('green','red', 'blue','yellow')
    )
    hist_values = np.histogram(
    bears['age'], bins=24, range=(0,24))[0]
    plt.hist(bears['age'],bins=25,color=genre,)
    plt.xlabel('Age in Years')
    plt.ylabel('Number of people killed')
    plt.title('Number and age of people who were killed by bears')
    st.pyplot()

st.subheader('Ready to find out your probability of being killed by a bear?')
agree = st.checkbox('Sure')
if agree:
       st.write("Let's find out!")
       # radio
       genre = st.radio(
       "What's your favourite movie genre?",
       ('Comedy', 'Drama','Documentary'))
       if genre == 'Comedy':
          st.write('Bears love comedies!')
       else:
          st.write("You don't like to laugh.")
       option = st.selectbox(
           'Where will you be travelling to in the future? ',
           ('North America','South America','Canada','Europe',
           'Asia','Russia','North Africa','South Africa',
           'Australia','New Zealand','Antartica')
       )
       d = st.date_input(
       f'What day will you enter {option} ?',
       datetime.date.today()
       )
       import time
       class tqdm:
            def __init__(self, iterable, title=None):
                if title:
                    st.write(title)
                self.prog_bar = st.progress(0)
                self.iterable = iterable
                self.length = len(iterable)
                self.i = 0

            def __iter__(self):
                for obj in self.iterable:
                    yield obj
                    self.i += 1
                    current_prog = self.i / self.length
                    self.prog_bar.progress(current_prog)
       st.subheader('Calculation')
       calc = st.checkbox('Yes, calculate')
       safe = '0.1%'
       med = '20%'
       risky = '45%'
       very_risky = '66%'
       if calc:
            for i in tqdm(range(200), title=''):
                    time.sleep(0.005)
            if ((genre == 'Comedy') or (option == 'North America') 
                    or (d.month == 8)):
                    st.write(risky)
            elif((genre != 'Comedy') and (option == 'Russia')):
                    st.write(very_risky) 
            elif ((genre != 'Comedy') or (option == 'South Africa') 
                    or (option == 'South America') and (d.month == 2)):
                st.write(safe)
            elif ((genre != 'Comedy') and (option == 'North America') 
                    and (d.month != 2)):
                    st.write(medium)
            else:
                st.write('10%') 

            if option == 'Russia':
                st.write('You better change your destination!')
            st.write('** This is not statistically correct, only for practice purposes')
            



















# Age slider
# age = st.slider('How old are you?',0,130,25)
# st.write("I'm ",age,'years old')

# st.write(bears['age'==(93)])


# if st.button('Press hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')







# Select box
# option = st.selectbox(
#         'How would you like to be contacted?',
#         ('Email','Home phone','Mobile phone')
# )
# st.write('You selected:', option)



# Age slider
# age = st.slider('How old are you?',0,130,25)
# st.write("I'm ",age,'years old')

# Range slider


# Text
# title = st.text_input('Movie title','Life of Brian')
# st.write('The current movie title is', title)

# Sentiment analysis
# txt = st.text_area('Text to analyze','''
#     It was the best of times, it was the worst of times,it was
#      the age of wisdom, it was the age of foolishness, it was
#      the epoch of belief, it was the epoch of incredulity, it
#      was the season of Light, it was the season of Darkness, it
#      was the spring of hope, it was the winter of despair, (...)
#         ''' )
# st.write('Sentiment:', run_sentiment_analysis(txt))

# date input
# d = st.date_input(
#     'When is your birthday?',
#     datetime.date(2019,7,6)
# )
# st.write('Your birthday is: ',d)

# file upload
# uploaded_file = st.file_uploader('Choose a CSV file',type='csv')
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     st.write(data.head())

# # widgets
# add_selectbox = st.sidebar.selectbox(
#     'How ould you like to be contacted?',
#     ('Email','Home Phone','Mobile phone')
# )



# with st.spinner('Wait for it...'):
#     time.sleep(3)
# st.success('Done')

# st.balloons()


