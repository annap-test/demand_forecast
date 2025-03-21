import streamlit as st
from app.config import DATA_PATH, MODEL_PATH
from data.data_utils import load_data, preprocess_input_data
from model.model_utils import load_model, predict
import datetime

def main():
    st.title("Corporación Favorita Sales Forecasting")

    # Load data and model
    df_stores, df_items, df_transactions, df_oil, df_holidays, df_train = load_data(DATA_PATH)
    model = load_model(MODEL_PATH)
    
    store_ids = df_stores[df_stores['state'] == 'Guayas']['store_nbr'].unique()
    item_families = ['GROCERY I', 'BEVERAGES', 'CLEANING']

    # now, we can get ids for the items that are in these familieis
    item_ids = df_items[df_items['family'].isin(item_families)]['item_nbr'].unique()

    # UI components for inputs
    store_id = st.selectbox("Store", store_ids)
    item_id = st.selectbox("Item", item_ids)
    #store_id = st.selectbox("Store", [1]) #for testing limit to one store
    #item_id = st.selectbox("Item", [564533,838216,582865,364606]) #for testing limit to a few items

    default_date = datetime.date(2014, 3, 1)  # Default to March 1, 2014
    min_date = datetime.date(2014, 1, 1)
    max_date = datetime.date(2014, 4, 1)
    date = st.date_input("Forecast Date",value=default_date,min_value=min_date,max_value=max_date)

    # Run prediction when button is clicked
    if st.button("Get Forecast"):
        input_data = preprocess_input_data(store_id, item_id, date, df_stores, df_items, df_train)
        prediction = predict(model, input_data)
        st.write(f"Predicted Sales for {date}: {prediction[0]}")

if __name__ == "__main__":
    main()