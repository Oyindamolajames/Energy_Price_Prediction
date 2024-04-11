import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os
import pandas as pd

# get working directory
root_dir = os.getcwd()
# set the path for the model and label encoder
model_name = os.path.join(root_dir, 'ui_app/saved_model.sav')
label_encoder_state_filename = os.path.join(root_dir, 'ui_app/label_encoder_state.pkl')
label_encoder_sector_filename = os.path.join(root_dir, 'ui_app/label_encoder_sector.pkl')
accuracy_img_path = os.path.join(root_dir, 'img/accuracy.png')

# load the model instance
with open(model_name, 'rb') as file:
    loaded_model = pickle.load(file)

# Load the LabelEncoder instances for each categorical column
with open(label_encoder_state_filename, 'rb') as file:
    label_encoder_state = pickle.load(file)
with open(label_encoder_sector_filename, 'rb') as file:
    label_encoder_sector = pickle.load(file)


# Define labels for months
month_labels = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


with st.sidebar:

    selected = option_menu('Energy Price Prediction System',
                          ['Predict Price',
                           'About App'],
                           icons = ['activity','info'],
                          default_index=0)

# Prediction Page
if (selected == 'Predict Price'):
    st.header('Energy Price Prediction Using Machine Learning')

    # inputs 

    col1, col2 = st.columns(2)

    with col1:
        year = st.slider('Year', min_value=2024, max_value=2026, value=2024, step=1)
        state_input = st.selectbox("Select State", label_encoder_state.classes_)
        customers = st.number_input('Number of Customers', min_value=0, max_value=50416198, value=500000, step=10000)
    with col2:
        month = st.selectbox('Month', month_labels.keys(), format_func=lambda x: month_labels[x])
        sector_input = st.selectbox("Select Sector", label_encoder_sector.classes_)

    # Display the selected inputs
    st.sidebar.write('Selected Inputs:')
    st.sidebar.write(f'- Year: {year}')
    st.sidebar.write(f'- Month: {month_labels[month]}')
    st.sidebar.write(f'- Number of Customers: {customers}')
    st.sidebar.write(f'- State: {state_input}')
    st.sidebar.write(f'- Sector: {sector_input}')

    

    
    # prediction button
    if st.button('Predict Price'):
        # Preprocess the encoded data
        encoded_state = label_encoder_state.transform([state_input])[0]
        encoded_sector = label_encoder_sector.transform([sector_input])[0]

        # prediction output
        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'year': [year],
            'month': [month],
            'customers': [customers],
            'state_encoded': [encoded_state],
            'sector_encoded': [encoded_sector]
        })

        # Make predictions using the loaded model
        prediction = loaded_model.predict(input_data)
        st.success("The predicted price is {} per kilowatt-hour (kWh) in cents".format(round(prediction[0],2)))
    
# About page
if (selected == "About App"):
    st.header("Energy Price Prediction Project")

    st.markdown('This project is developed by Ogunsanya James for the Optimus AI Labs Hackathon. The goal of this project is to build a machine learning model and a user interface application for predicting energy prices. The dataset used for training the model was obtained from Kaggle and can be found [here](https://www.kaggle.com/datasets/alistairking/electricity-prices?select=clean_data.csv).') # see #*

    st.markdown('## Overview')

    st.markdown('Energy price prediction is a crucial task for energy companies, policymakers, and consumers alike. Accurate predictions can help optimize energy production and consumption, leading to cost savings and improved resource management. In this project, the aim is to develop a machine learning model that can predict energy prices based on historical data and relevant features.')
    
    st.markdown('## Technologies Used')

    st.markdown('- Python for model developement')

    st.markdown('- Random Forest Regressor')

    st.markdown('- Streamlit for the UI')

    st.markdown('[Link to github repository](https://github.com/Oyindamolajames/Energy_Price_Prediction)')

    st.markdown('## Model Accuracy')

    st.image(accuracy_img_path, use_column_width=True)

    st.markdown('## Acknowledgments')

    st.markdown('- [Alistair King](https://www.kaggle.com/alistairking) for providing the dataset on Kaggle.')

    st.markdown('- Optimus AI Labs for organizing the hackathon.')

    st.markdown('## Author')

    st.markdown('- **Ogunsanya James** - Machine Learning Engineer')

    st.markdown('- [Github](https://www.github.com/oyindamolajames)')

    st.markdown('- [Linkdein](https://www.linkedin.com/in/james-ogunsanya-7088928a/)')

    st.markdown('## Feedback')

    st.markdown('If you have any feedback, please reach out to us at oyindamolajames@gmail.com')    