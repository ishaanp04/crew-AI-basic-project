from dotenv import load_dotenv

load_dotenv()
import os

serper_api_key = os.getenv("SERPER_API_KEY")
if not serper_api_key:
    raise ValueError("SERPER_API_KEY is missing! Check your .env file.")

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()
