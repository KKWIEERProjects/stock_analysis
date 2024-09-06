import streamlit as st

st.set_page_config(
    page_title="Stock Prediction App",
    page_icon="📈",
)

st.markdown(
    """# 📈 **Stock Prediction App**
### **Predicting Stocks with ML**

**It is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

Stock Prediction App is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Prophet** - A tool for time series forecasting with seasonal trends.
- **Plotly** - To create interactive financial charts

## 🚀 **Description**


1. **Streamlit (`streamlit`):** 
   - **Purpose:** A framework for building interactive web applications in Python. 
   - **Features Used:**
     - Title setting, dropdown menus, text display, and interactive charts.

2. **Datetime (`datetime`):**
   - **Purpose:** For handling dates and times.
   - **Features Used:**
     - Fetching the current date.

3. **Yahoo Finance (`yfinance`):**
   - **Purpose:** To download historical stock market data from Yahoo Finance.
   - **Features Used:**
     - Fetching stock data for specific tickers.

4. **Prophet (`prophet`):**
   - **Purpose:** For forecasting time-series data.
   - **Features Used:**
     - Creating and fitting a forecasting model, generating future dates, and making predictions.

5. **Plotly (`plotly`):**
   - **Purpose:** For creating interactive plots.
   - **Features Used:**
     - Generating interactive charts from Prophet forecasts.

##  🚀 **The app workflow is:**

1. User selects a stock ticker
2. Historical data is fetched with YFinance
3. ARIMA model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

## 🎯 **Key Features**

- **Real-time data** - Fetch latest prices and fundamentals 
- **Financial charts** - Interactive historical and forecast charts
- **ARIMA forecasting** - Make statistically robust predictions
- **Backtesting** - Evaluate model performance
- **Responsive design** - Works on all devices


## 📈 **Future Roadmap**

Some potential features for future releases:

- **More advanced forecasting models like LSTM**
- **Quantitative trading strategies**
- **Portfolio optimization and tracking**
- **Additional fundamental data**
- **User account system**

## **⚖️ Disclaimer**
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**
"""
)
