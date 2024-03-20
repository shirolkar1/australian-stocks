
import streamlit as st
import pandas as pd

# Load the DataFrame
file_path = 'https://drive.google.com/file/d/1-CgGfpzLa862SbgmQaVG7uY6GxTkP0Bn/view?usp=drivesdk'
df = pd.read_csv(file_path,delimiter='\t')

def app():
    st.title('Stock Buy/Sell Recommendations')

    # Display the DataFrame
    st.dataframe(df)

    # Dropdown for stock selection
    stock_options = df['Name of the Stock'].unique().tolist()
    selected_stock = st.selectbox('Select a stock:', stock_options)

    # Display the selected stock's Buy/Sell recommendation
    if selected_stock:
        recommendation = df[df['Name of the Stock'] == selected_stock]['Buy/Sell'].iloc[0]
        st.write(f"Recommendation for {selected_stock}: {recommendation}")

if __name__ == '__main__':
    app()
