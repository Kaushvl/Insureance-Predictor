import streamlit as sl
import pickle,numpy as np


model = pickle.load(open('model.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

sl.title('Insurance Price Estimator')

age = sl.number_input('Age')

sex = sl.selectbox('Sex',['Male','Female'])

bmi = sl.number_input('Bmi')

children = sl.number_input('No. of children')

smoker = sl.selectbox('Smoker',['Yes','No'])

region = sl.selectbox('Region',['northeast','northwest','southeast','southwest'])

l1=0
l2=0
l3=0


if sl.button("Calculate Price"):
    
    if sex == 'Male':
        sex = 1
    else:
        sex = 0

    if smoker=='Yes':
        smoker=1
    else :
        smoker=0

    if region=='northeast':
        l1=1
        l2=0
        l3=0
    elif region=='northwest':
        l1=0
        l2=1
        l3=0
    elif region=='southeast':
        l1=0
        l2=0
        l3=1
    else:
        l1=0
        l2=0
        l3=0



    query = np.array([age,sex,bmi,children,smoker,l1,l2,l3])
    query = query.reshape(1,8)

    sl.title(model.predict(query).round(2))