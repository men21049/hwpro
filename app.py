import streamlit as st
from file_to_df import FileToDf

st.title("Facebook Data Analysis from Kaggle 👋")
st.markdown(
    """ 
    The current project analysis data from Facebook available in Kaggle.
    https://www.kaggle.com/datasets/sheenabatra/facebook-data?resource=download
    
    .The idea is to demostrate the usage of Pandas as an data analysis library
    and to display graphs **First we look at the dataset**
    and then analyze what gender gets more likes and their median age
    """
)

df = FileToDf("pseudo_facebook.csv")

st.dataframe(df.cvtodf())

st.dataframe(df.filterdataframe('gender', 'female'))
st.dataframe(df.filterdataframe('gender', 'male'))

st.markdown(
    """
    Now are going to order the dataset by age
    """)

st.dataframe(df.sortfilter('gender', 'female', 'age'))
st.dataframe(df.sortfilter('gender', 'male', 'age'))

st.title(
    """
    What is the median age for each gender?

    """)

st.write(f""" The median age for females is: **{df.getmedianbycolumn('gender', 'female', 'age')}**
         and a standard deviation of : **{df.getstdbycolumn('gender', 'female', 'age'):.2f}**""")
st.write(f""" The median age for males is: **{df.getmedianbycolumn('gender', 'male', 'age')}**
         and a standard deviation of : **{df.getstdbycolumn('gender', 'male', 'age'):.2f}**""")


dffemale = df.getfilterbycolumngroupbycolumn('gender', 'female', 'age', 'friend_count')
st.title("The below graph shows the average number of friends of female users by age")
st.line_chart(dffemale[['age', 'friend_count']], x = 'age', y = 'friend_count', color="#FF0000")

dfmale = df.getfilterbycolumngroupbycolumn('gender', 'male', 'age', 'friend_count')
st.title("The below graph shows the average number of friends of male users by age")
st.line_chart(dfmale[['age', 'friend_count']], x = 'age', y = 'friend_count', color="#0000FF")


df1 = df.getgroupbycolumn(['gender', 'age'],'likes_received')
pivot = df1.pivot(index='age', columns='gender', values='likes_received')
st.title("Now we can compare the number of likes each gender receives by age: ")
st.line_chart(pivot, color= ["#FF0000","#0000FF"])

st.write("Now we can see that females at a younger age receive more likes than their males counterparts at the same age")