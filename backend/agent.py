import os
from langchain_openai import ChatOpenAI
from tools import get_weather
import re


llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)


def ask_agent(query: str) -> str:
    """
    Simple router:
    - If query mentions weather → call weather tool
    - Else → let LLM respond
    """

    lowered = query.lower()

    if "weather" in lowered:
        # Remove punctuation
        clean_query = re.sub(r"[^\w\s]", "", lowered)

        # Common patterns
        patterns = [
            r"weather of (\w+)",
            r"weather in (\w+)",
            r"(\w+) weather"
        ]

        city = None
        for pattern in patterns:
            match = re.search(pattern, clean_query)
            if match:
                city = match.group(1)
                break

        if not city:
            return "Please specify a city name."

        return get_weather(city)

    # fallback: normal LLM response
    response = llm.invoke(query)
    return response.content
