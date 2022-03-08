

import yfinance as yf
import streamlit as st

### HEADING OF THE PAGE ###
st.write("""
# Simple Stock Price App
""")

# following link for more yfinance concepts
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# INPUT the ticker symbol in a text input
tickerSymbol = st.text_input(" Search using ticker symbol ", key = "stock")
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1mo', start='2010-5-31', end='2020-5-31')

# Display price table with all params 
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write(" ## Price Table: ", st.session_state.stock)
tickerDf

###################################################
### Display the checkboxes for different params ###
###################################################
st.write("select for chart:")
Open = st.checkbox("Open")
Close = st.checkbox("Close")
High = st.checkbox("High")
Low = st.checkbox("Low")
Dividends = st.checkbox("Dividends")
Volume = st.checkbox("Volume")

### st.cache trying to optimize performance but not effectively implemented here!!!
@st.cache(suppress_st_warning = True, allow_output_mutation=True)
def call_chart():
    if Open:
        st.write(""" ## Prices Open""")
        st.line_chart(tickerDf.Open)

    if High:
        st.write(""" ## Prices High""")
        st.line_chart(tickerDf.Low)

    if Low:
        st.write(""" ## Prices Low""")
        st.line_chart(tickerDf.Low)


    if Close:
        st.write(""" ## Closing price""")
        st.line_chart(tickerDf.Close)

    if Volume:
        st.write(""" ## Volume""")
        st.line_chart(tickerDf.Volume)

    if Dividends:
        st.write(""" ## Prices Dividends """)
        st.line_chart(tickerDf.Dividends)

call_chart()

# Extra recommended stocks.
st.write(""" **Recommended Stocks** """)
tickerData.recommendations
