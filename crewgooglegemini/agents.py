from crewai import LLM, Agent
from dotenv import load_dotenv
from tools import tool

load_dotenv()
import os

from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

## call the gemini models
# llm = ChatGoogleGenerativeAI(
#     model="gemini/gemini-2.0-flash",
#     verbose=True,
#     temperature=0.5,
#     google_api_key=os.getenv("GEMINI_API_KEY"),
# )
llm = LLM(
    model="gemini/gemini-2.0-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

# Creating a senior researcher agent with memory and verbose mode

news_researcher = Agent(
    role="Senior Researcher",
    goal="Unccover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True,
)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False,
)
