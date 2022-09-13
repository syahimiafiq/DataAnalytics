{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue254;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c99608;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl380\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import streamlit as st\cb1 \
\cb3 import pandas as pd\cb1 \
\
\cb3 st.header("My first Streamlit App")\cb1 \
\
\cb3 st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')\cb1 \
\cb3 show = st.checkbox('I agree the terms and conditions')\cb1 \
\cb3 if show:\cb1 \
\cb3     st.write(pd.DataFrame(\{\cb1 \
\cb3     'Intplan': ['yes', 'yes', 'yes', 'no'],\cb1 \
\cb3     'Churn Status': [0, 0, 0, 1]\cb1 \
\cb3 \}))}