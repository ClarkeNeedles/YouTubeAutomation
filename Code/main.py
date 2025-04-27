import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    # Get environment variable key
    api_key=os.getenv("OPENAI_API_KEY"),
)

def generate_script(topic):
    prompt = f"Write a short-form video script under 60 seconds for the topic: '{topic}'"
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a coding assistant that talks like a pirate.",
        input=prompt,
    )

    return response.output_text

# Example
print(generate_script("Why saving money in your 20s matters"))
