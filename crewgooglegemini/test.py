import os

import litellm
from dotenv import load_dotenv

load_dotenv()
# print("Vertex Chat Models:", litellm.vertex_chat_models)
# print("Gemini Chat Models:", litellm.gemini_models)


response = litellm.completion(
    model="gemini/gemini-2.0-flash",  # ✅ Correct model format
    messages=[{"role": "user", "content": "Hello, Gemini!"}],
    api_key=os.getenv("GEMINI_API_KEY"),
    # custom_llm_provider="google",  # ✅ Explicitly override the provider
)

print(response)
