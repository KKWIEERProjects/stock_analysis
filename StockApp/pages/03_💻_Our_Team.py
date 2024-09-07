import streamlit as st

# Add a centered heading for the team section
st.markdown("<h1 style='text-align: center;'>Meet Our Team</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# Create a single row with four columns
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# Team Member 1 - Pratik
with col1:
    st.image("E:\\ML_Project\\stock\\stock_analysis\\assets\\pratik.jpg", caption="Pratik", width=150)

# Team Member 2 - Sumedh
with col2:
    st.image("E:\\ML_Project\\stock\\stock_analysis\\assets\\sumedh.jpg", caption="Sumedh", width=150)

# Team Member 3 - Madhura
with col3:
    st.image("E:\\ML_Project\\stock\\stock_analysis\\assets\\madhura.jpg", caption="Madhura", width=150)

# Team Member 4 - Vedant
with col4:
    st.image("E:\\ML_Project\\stock\\stock_analysis\\assets\\vedant.jpg", caption="Vedant", width=150)
