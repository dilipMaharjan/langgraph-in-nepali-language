from graphs import graph_builder
from llms.groq import Groq
import uvicorn
from fastapi import FastAPI, Request
import os
from  dotenv import load_dotenv

load_dotenv()


app=FastAPI()

os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

@app.post("/blogs")
async def create_blog(request:Request):
    data=await request.json()
    topic=data.get("topic","")
    groq_obj=Groq()
    llm=groq_obj.get_llm()

    graph_builder_obj=graph_builder.GraphBuilder(llm)

    if topic:
        graph=graph_builder_obj.setup_graph(usecase="topic")
        state=graph.invoke({"topic":topic})
    return {"data":state}

if __name__=="__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8002,reload=True)








