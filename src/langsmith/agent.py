from typing import Annotated
from typing_extensions import TypedDict
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
import os
from dotenv import load_dotenv

#load keys

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

#create state

class State(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]
    

#initialize chat
llm = ChatGroq(model_name="llama-3.1-8b-instant",temperature=0.7)

def default_graph():
    graph=StateGraph(State)
    
    def call_llm(state):
        return {"messages":[llm.invoke(state["messages"])]}
    
    graph.add_node("call_llm",call_llm)
    graph.add_edge(START,"call_llm")
    graph.add_edge("call_llm",END)
    call_llm=graph.compile()
    return call_llm

llm_call=default_graph()
    
