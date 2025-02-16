from agents import news_researcher, news_writer
from crewai import Crew, Process
from dotenv import load_dotenv
from tasks import research_task, write_task

load_dotenv()
import os

## Forming the tech focused crew with some enhanced configuration
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    # embedder={
    #     "provider": "google",
    #     "config": {
    #         "api_key": os.getenv("GOOGLE_API_KEY"),
    #         "model": "gemini/gemini-2.0-flash",
    #     },
    # },
)

## starting the task execution process wiht enhanced feedback

result = crew.kickoff(inputs={"topic": "AI in healthcare"})
print(result)
