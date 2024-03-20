import streamlit as st
import pandas as pd

# Configure the page to use wide mode
st.set_page_config(layout="wide")

# Load the DataFrame
file_path = 'https://drive.google.com/uc?export=download&id=1-CgGfpzLa862SbgmQaVG7uY6GxTkP0Bn'
df = pd.read_csv(file_path)

def app():
    st.title('Stock Buy/Sell Recommendations')

    # Display the DataFrame, setting it to use the container's width
    st.dataframe(df, use_container_width=True)

    # Dropdown for stock selection
    stock_options = df['Name of the Stock'].unique().tolist()
    selected_stock = st.selectbox('Select a stock:', stock_options)

    # Display the selected stock's Buy/Sell recommendation
    if selected_stock:
        recommendation = df[df['Name of the Stock'] == selected_stock]['Buy/Sell'].iloc[0]
        st.write(f"Recommendation for {selected_stock}: {recommendation}")

if __name__ == '__main__':
    app()
