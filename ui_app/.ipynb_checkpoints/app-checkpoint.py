import pickle
import streamlit as st
from streamlit_option_menu import option_menu

model_name = "/home/hoyindamola/Documents/Programming/Energy_Price_Prediction_/ui_app/saved_model.sav"

# load the model instance
with open(model_name, 'rb') as file:
    loaded_model = pickle.load(file)
    
# Load the LabelEncoder instances for each categorical column
label_encoder_state_filename = "label_encoder_state.pkl"
with open(label_encoder_state_filename, 'rb') as file:
    label_encoder_state = pickle.load(file)

label_encoder_sector_filename = "label_encoder_sector.pkl"
with open(label_encoder_sector_filename, 'rb') as file:
    label_encoder_sector = pickle.load(file)


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
    name = st.text_input("Enter youe name")
    state_input = st.selectbox("Select State", label_encoder_state.classes_)
    sector_input = st.selectbox("Select Sector", label_encoder_sector.classes_)

    # Preprocess the encoded data
    encoded_state = label_encoder_state.transform([state_input])[0]
    encoded_sector = label_encoder_sector.transform([sector_input])[0]

    # prediction output
    st.write(name)
    

    # prediction button
    if st.button('Predict Price'):
        #loaded_model.predict([[]])
        st.success("My prediction comes here")
    
# About page
if (selected == "About App"):
    st.header("This is an information about app here")
   