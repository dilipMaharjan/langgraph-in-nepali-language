from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns a list of tool instances.
    """
    tools = [TavilySearch(max_results=2)]
    return tools


def create_tool_node(tools):
    """
    Creates and returns a ToolNode for use in a LangGraph.
    
    Args:
        tools (list): A list of initialized tool objects.
    
    Returns:
        ToolNode: A node wrapping the provided tools.
    """
    return ToolNode(tools)
