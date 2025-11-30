from langgraph.graph import StateGraph, START,END
from nodes.blog_node import BlogNode
from llms.groq import Groq
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
    
    def build_translate_graph(self):
        """
        Build a language translate graph.
        """ 
        self.blog_obj=BlogNode(self.llm)

        #Nodes
        self.graph.add_node("title_creation",self.blog_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_obj.content_generation)
        self.graph.add_node("nepali_translation",lambda state: self.blog_obj.content_translate({**state,"content_language":"nepali"}))
        self.graph.add_node("spanish_translation",lambda state: self.blog_obj.content_translate({**state,"content_language":"spanish"}))
        self.graph.add_node("route",self.blog_obj.route)

        #Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation","route")

        self.graph.add_conditional_edges(
            "route",
            self.blog_obj.route_decision,
            {
                "nepali":"nepali_translation",
                "spanish":"spanish_translation"
            }
        )
        self.graph.add_edge("nepali_translation",END)
        self.graph.add_edge("spanish_translation",END)
        return self.graph


    
    def setup_graph(self,usecase):
        if usecase=="topic":
            self.build_graph()
        if usecase=="language":
            self.build_translate_graph()
        return self.graph.compile()

llm=Groq().get_llm()
graph_builder=GraphBuilder(llm)
graph=graph_builder.build_translate_graph().compile()


        


        
