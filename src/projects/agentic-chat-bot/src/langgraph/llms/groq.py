import os
from re import A 
import streamlit as st
from langchain_groq import ChatGroq

class Groq:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input
    def get_model(self):
        try:
            api_key=self.user_controls_input["GROQ_API_KEY"]
            selected_model=self.user_controls_input["selected_groq_model"]
            if api_key == '' and os.environ["GROQ_API_KEY"] == '':
                st.error("Please Enter the Groq API KEY")
            llm=ChatGroq(api_key=api_key,model=selected_model)
        except Exception as e:
            raise ValueError(f" Error Occurred with Exception : {e}")
        return llm
    
