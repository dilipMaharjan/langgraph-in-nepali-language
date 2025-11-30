import stat
from states.blog_state import Blog, BlogState
from langchain_core.messages import HumanMessage

class BlogNode:
    """ Blog Node"""
    def __init__(self,llm):
        self.llm=llm
    def title_creation(self,state:BlogState):
        """ Creates a title for the blog"""

        if "topic" in state and state["topic"]:
            prompt="""
                        You are an expert blog content writer. Use Markdown formatting. Generate a blog title for the {topic}.
                        This title should be creative and SEO friendly. 
                    """
            system_message=prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}
    
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            prompt="""
                        You are an expert blog content writer. Use Markdown formatting. Generate a detailed blog content with detailed breakdown for the {topic}.
                    """
            system_message=prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
        return {"blog": {"title": state['blog']['title'],"content":response.content}}
    
    def content_translate(self, state: BlogState):
        """Translate the blog title and content to the specified language."""

        blog_title = state["blog"]["title"]
        blog_content = state["blog"]["content"]

        translation_prompt = """
        Translate the following blog into {language}.  
        INSTRUCTIONS:
        - Output must be in **proper {language} language**.
        - Do NOT keep Hindi words or Roman script.  
        - Remove all special formatting: no bullets (*), hashes (#), dashes (-), or asterisks.  
        - Keep paragraph breaks intact, but no extra empty lines.  
        - Output in the following exact format:

        TITLE: <translated title in {language}>
        CONTENT: <translated content in {language}>

        Original blog:

        TITLE:
        {blog_title}

        CONTENT:
        {blog_content}

        """

        prompt = translation_prompt.format(
            language=state["content_language"],
            blog_title=blog_title,
            blog_content=blog_content
        )

        messages = [HumanMessage(content=prompt)]

        translated_text = self.llm.invoke(messages).content

        # Separate title and content from LLM output
        # For example, you could instruct the LLM to format as:
        # "TITLE: ...\nCONTENT: ..."
        # and then split here
        title_line, content_text = translated_text.split("\n", 1)

        # Remove the "TITLE: " prefix
        translated_title = title_line.replace("TITLE:", "").strip()
        translated_content = content_text.replace("CONTENT:", "").strip()

        return {"blog": Blog(title=translated_title, content=translated_content)}
    
    def route(self,state:BlogState):
        return {"content_language":state['content_language']}
    
    def route_decision(self,state:BlogState):
        """ Routes the content as per the appropriate route function"""

        if state['content_language']=="nepali":
            return "nepali"
        elif state['content_language']=="spanish":
            return "spanish"
        else:
            return state["content_language"]

    


