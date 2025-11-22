import streamlit as st
from src.langgraph.llms.groq import Groq
from src.langgraph.ui.streamlit.load_ui import LoadStreamlitUI
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlit.display_result import DisplayResultStreamlit
import traceback

def load_agentic_app_ui():
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error(" Error : Failed to load user input from the UI")
    user_message = st.chat_input ("Enter your message.")

    if st.session_state.IsFetchButtonClicked:
        user_message=st.session_state.timeframe
    else:
        user_message= st.chat_input("Enter your message:")

    if user_message:
        try:
            llm=Groq(user_controls_input=user_input)
            model=llm.get_model()
            if not model:
                st.error("Error : LLM model could not be initialized")
                return 
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error : Please select a use case")
                return 
            
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result()
            except Exception as e:
                st.error(f" Graph Display Failed with error: {e}")
                tb = traceback.format_exc()
                st.text("Full traceback:")
                st.text(tb)
                return 
        except Exception as e:    
            st.error(f"Graph Setup Failed with error: {e}")
            return     
