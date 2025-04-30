import os
import random

import google.generativeai as genai
from dotenv import load_dotenv
from difflib import SequenceMatcher

# Load environment variables
load_dotenv()

# Load API Key from .env file
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Variables
# Load all the topics and moods
topics_file = open("topics.txt", "r")
moods_file = open("moods.txt", "r")
scripts_file = open("scripts.txt", "r")

topics = topics_file.read().split("<>")
moods = moods_file.read().split("<>")
scripts = scripts_file.read().split("<>")

# Function definition
def generate_script(topic, mood):
    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt = f"Write a {mood} short video script about '{topic}'. Make it under 60 seconds."

    response = model.generate_content(prompt)

    return response.text.strip()

def is_unique(new, existing, threshold=0.6):
    for item in existing:
        similarity = SequenceMatcher(None, new, item).ratio()
        if similarity > threshold:
            return False
    return True

def add_new_item(type):
    types = ["topic", "mood", "script"]

    while True:
        str_input = input(f"Enter a new {types[type - 1]}, exit to stop.\nIf you are generating a new script, press enter.")

        if str_input.lower() == "exit":
            break;

        # Setting the list to compare
        compare_list = []
        match type:
            case 1:
                compare_list = topics
            case 2:
                compare_list = moods
            case 3:
                # Ensure that topics and moods is not empty to generate a new script
                str_input = generate_script(random.choice(topics), random.choice(moods))
                compare_list = scripts

        if is_unique(str_input, compare_list):
            with open(f"{types[type-1]}s.txt", "a") as f:
                f.write("<>" + str_input)
        else:
            print("Topic has already been added")

def main():
    while True:
        user_input = int(input("What would you like to add/create?:\n1.Topic\n2.Mood\n3.Script\n4.Stop"))

        if user_input == 4:
            break;

        add_new_item(user_input)

main()
