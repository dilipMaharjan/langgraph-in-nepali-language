from re import S
from langgraph.graph import StateGraph, START,END
from nodes.blog_node import BlogNode
from states.blog_state import BlogState

class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)
    
    def build_graph(self):
        """ Build a graph to generate blog based on given topic """

        self.blog_obj=BlogNode(self.llm)

        #Nodes
        self.graph.add_node("title_creation",self.blog_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_obj.content_generation)

        #Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation",END)

        return self.graph
    
    def setup_graph(self,usecase):
        if usecase=="topic":
            self.build_graph()
        return self.graph.compile()

        


        
