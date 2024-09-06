import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Define the start date and today's date
START = "2023-08-08"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('📈 Stock Prediction Analysis')

# Define the list of stocks
stocks = ('TATASTEEL.NS', 'TTML.NS', 'ADANIGREEN.NS', 'RVNL.NS', 'IRFC.NS')

# Create a selectbox 
selected_stock = st.selectbox('Choose Stock for prediction', stocks)

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start=START, end=TODAY)
    data.reset_index(inplace=True)
    return data

# Fetch and display data
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader(f'Data for {selected_stock}')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], mode='lines', name="Stock Open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name="Stock Close"))
    fig.update_layout(title_text='Time Series Data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Prepare data for Prophet
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# Predict forecast with Prophet
m = Prophet()
m.fit(df_train)
n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast Data')
st.write(forecast.tail())

st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast Components")
fig2 = m.plot_components(forecast)
st.plotly_chart(fig2)