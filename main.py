# pip install streamlit prophet yfinance plotly

import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Define the start date and today's date
START = "2023-08-08"
TODAY = date.today().strftime("%Y-%m-%d")

# Fetch stock data for TATASTEEL.NS as an example
tata = yf.download("TATASTEEL.NS", start=START, end=TODAY)

# Set the title of the Streamlit app
st.title('Stock Prediction App')

# Define the list of stocks
stocks = ('TATASTEEL.NS', 'TTML.NS', 'ADANIGREEN.NS', 'RVNL.NS', 'IRFC.NS')

# Create a selectbox for the user to select a dataset for prediction
selected_stock = st.selectbox('Select dataset for prediction', stocks)

# Fetch stock data for the selected stock
stock_data = yf.download(selected_stock, start=START, end=TODAY)

# Display the fetched data
st.write(f"Data for {selected_stock}")
st.write(stock_data)

# START = "2015-01-01"
# TODAY = date.today().strftime("%Y-%m-%d")
# tata = yf.download("TATASTEEL.NS", start="2021-01-02")
# st.title('Stock Forecast App')


# stocks = ('tata','TTML', 'ADANIGREEN', 'RVNL', 'IRFC')
# selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365


@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
# @st.cache
# def load_data(ticker):
#     data = yf.download(ticker, START, TODAY)
#     data.reset_index(inplace=True)
#     return data

	
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)