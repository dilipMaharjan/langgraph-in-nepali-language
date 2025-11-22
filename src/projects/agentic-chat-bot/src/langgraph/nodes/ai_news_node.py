from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self,llm):
        """
        Initialize the AINewsNode with API keys for Tavily and GROQ.
        """
        self.tavily=TavilyClient()
        self.llm=llm
        self.state={}
    
    def fetch_news(self,state:dict)->dict:
        """
        Fetch AI news based on the specified frequency.

        Args:
            state(dict): State dictionary containing frequency
        Returns:
            dict: Updated state with 'news_data' key containing fetched news.

        """
        frequency=state['messages'][0].content.lower()
        self.state['frequency']=frequency
        time_range_map={'daily':'d','weekly':'w','monthly':'m','yearly':'y'}
        days_map={'daily':1,'weekly':7,'monthly':30,'year':365}

        response=self.tavily.search(
            query="Top artificial Intellignec (AI) technology news globally.",
            topic="news",
            time_range_map=time_range_map[frequency],
            include_answer="advanced",
            max_results=15,
            days=days_map[frequency]
        )
        state['news_data']=response.get('results',[])
        self.state['news_data']=state['news_data']
        return state
        
    def summarize(self,state:dict)->dict:
            """
            Summarize the fetched news using an LLM

            Args:
                state (dict) : The state dictionary containing 'news_data'
            Returns:
                dict: Updated state with 'summary' key containing the summarized news.
            """
            news_item=self.state['news_data']
            prompt_template=ChatPromptTemplate.from_messages([
                 ("system"),
                """
                You are an AI assistant. Summarize AI news articles strictly based on the input data.
                Do NOT generate any news that is not present in the articles provided. 

                For each article:
                - Include the date in YYYY-MM-DD format in CST timezone.
                - Provide a concise summary in one or two sentences.
                - Include the source URL as a Markdown link.
                - Sort news by date, latest first (most recent first). 
                Use format:
                ### [Date]
                    [Summary](URL)"""
                ,
                ("user","Articles:\n {articles}")
                ])
            articles_str="\n\n".join(
                [
                    f"Content:{item.get('content','')}\nURL: {item.get('url','')}\nDate:{item.get('published_date','')}"
                    for item in news_item
                ])
            final_prompt = prompt_template.format_prompt(articles=articles_str)

            # The final text that will be sent to the LLM
            print("final prompt : {}",final_prompt.to_string())
            response=self.llm.invoke(final_prompt)
            state['summary']=response.content
            self.state['summary']=state['summary']
            return self.state
    
    def save_result(self,state):
        frequency=self.state['frequency']
        summary=self.state['summary']
        filename=f"./news/{frequency.lower()}_summary.md"
        with open(filename,'w') as f:
            f.write(f'# {frequency.capitalize()} AI News Summary\n\n')
            f.write(summary)
        self.state['filename']=filename
        return self.state
