{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;}
{\colortbl;\red255\green255\blue255;\red24\green25\blue27;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c12549\c12941\c14118;\cssrgb\c100000\c100000\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 %%writefile myfirstapp.py\
import streamlit as st\
import numpy as np\
import pandas as pd\
\
st.header("My first Streamlit App")\
st.write(pd.DataFrame(\{\
    'Intplan': ['yes', 'yes', 'yes', 'no'],\
    'Churn Status': [0, 0, 0, 1]\
\}))}