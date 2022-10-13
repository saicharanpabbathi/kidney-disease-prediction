#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
import pickle
import numpy as np
model=pickle.load(open("rf.pkl","rb"))
st.title("Chronic Kidney Disease Prediction")
age=st.number_input("what is your age:",0,100)
bp=st.number_input("bp",0,180)
sg=st.text_input("specific gravity")
al=st.selectbox("albumin range",[0,1,2,3,4,5])
su=st.selectbox("sugar level",[0,1,2,3,4,5])
rbc=st.selectbox("redblood cell levels:",["normal","abnormal"])
if(rbc=="normal"):
    rbc=1
else:
    rbc=2
bgr=st.text_input("blood glucose random:")
bu=st.text_input("blood urea:")
sc=st.text_input("serum:")
sod=st.text_input("sodium:")
pot=st.text_input("potissum:")
hemo=st.text_input("hemoglobin:")
wc=st.text_input("white blood count:")
rc=st.text_input("red blood count:")
htn=st.selectbox("do you have hypertension:",["yes","no"])
if(htn=="yes"):
    htn=1
else:
    htn=0
dm=st.selectbox("do you have diabatic millets",["yes","no"])
if(dm=="yes"):
    dm=1
else:
    dm=0
cad=st.selectbox("do you have heart disease:",["yes","no"])
if(cad=="yes"):
    cad=1
else:
    cad=0
appeit=st.selectbox("how is your appitite:",["good","poor"])
if(appeit=="good"):
    appeit=0
else:
    appeit=1
pe=st.selectbox("do you have swollen legs",["yes","no"])
if(pe=="yes"):
    pe=1
else:
    pe=0
ane=st.selectbox("do you have anemia:",["yes","no"])
if(ane=="yes"):
    ane=1
else:
    ane=0
def prediction(age=40,bp=80,sg=127.0,al=1,su=1,rbc=1,bgr=102.1,bu=13.2,sc=120.2,sod=10,pot=22,hemo=180,wc=7800,rc=9,htn=0,dm=0,cad=0,appeit=1,pe=0,ane=0):
    return model.predict([[age,bp,sg,al,su,rbc,bgr,bu,sc,sod,pot,hemo,wc,rc,htn,dm,cad,appeit,pe,ane]])

x=2


# In[9]:


if(st.button("predict")):
    x=prediction(age,bp,float(sg),al,su,rbc,float(bgr),float(bu),float(sc),float(sod),float(pot),float(hemo),int(wc),float(rc),htn,dm,cad,appeit,pe,ane)
if(x==1):
    st.success("The patient don't have the disease")
elif(x==0):
    st.error("The patient has the disease")


# In[ ]:




