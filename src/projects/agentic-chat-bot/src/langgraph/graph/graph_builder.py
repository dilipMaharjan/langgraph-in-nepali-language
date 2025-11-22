
from src.langgraph.state.state import State
from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import tools_condition
from src.langgraph.nodes.basic_chatbot import BasicChatBotNode
from src.langgraph.tools.web_serach_tool import get_tools,create_tool_node
from src.langgraph.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraph.nodes.ai_news_node import AINewsNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def build_basic_chatbot_graph(self):
        """
        Builds a basic chatbot graph using LangGraph. 
        This method initializes a chatbot node using 
        the BasicChabotNode class intengrates it into the graph.
        The chatbot node is set as both entry and exit point of the graph.
        """
        self.basic_chatbot_node=BasicChatBotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def build_chatbot_with_tool_graph(self):
        """
        Builds a chatbot with tool integration graph using LangGraph. 
        This method initializes a chatbot node and tool node.
        It integrates tool with chatbot.
        """
        tools=get_tools();
        tool_node=create_tool_node(tools)
       

        chatbot_obj=ChatbotWithToolNode(self.llm)
        chatbot_node=chatbot_obj.create_chatbot(tools)


        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")    

    def build_ai_news_chatbot_graph(self):
        """
        Builds a chatbot with tool integration graph using LangGraph. 
        This method initializes a chatbot node and tool node.
        It integrates tool with chatbot.Fetches ai news based on selected timeframe.
        """
        ai_news_node=AINewsNode(self.llm)

        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize)
        self.graph_builder.add_node("save_result",ai_news_node.save_result)

        self.graph_builder.add_edge(START,"fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result",END)
       
    def setup_graph(self,usecase:str):
        """
        Sets the graph for selected use case.

        """
        if usecase == "Basic Chatbot":
            self.build_basic_chatbot_graph()
        if usecase == "Chatbot with Tool":
            self.build_chatbot_with_tool_graph()
        if usecase == "AI News":
            self.build_ai_news_chatbot_graph()

        graph=self.graph_builder.compile()
        graph_image = graph.get_graph().draw_mermaid_png()
        with open("graph.png", "wb") as f:
            f.write(graph_image)
        print("Saved to graph.png")
        return graph



