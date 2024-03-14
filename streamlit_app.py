import time

import pandas as pd
import streamlit as st

placeholder = st.empty()

while True:
    df = pd.read_csv('D:\\streamlit_input_files\\pnl_scenario_sqlview\\dropcopy_Dealer_PNL_mar_pinpout_scenario_sqlview.csv')
    placeholder.dataframe(df)
    time.sleep(3)

