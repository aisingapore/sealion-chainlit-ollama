from dotenv import load_dotenv
from openai import AsyncOpenAI
from typing import Dict, Optional
import chainlit as cl
import logging
import os
import sys

"""
A chatbot application built with Chainlit.

This application provides answers to user prompts.
"""

# Set the log level
logging.basicConfig(level=logging.INFO)

# Get the environment variables for LLM base URL and model name, raise an error and exit if not defined
try:
    LLM_BASE_URL = os.environ["LLM_BASE_URL"]
    LLM_MODEL = os.environ["LLM_MODEL"]
except KeyError as e:
    logging.error(f"The environment variable {e} is not defined.")
    sys.exit(1)

# Initialise the client
client = AsyncOpenAI(base_url=LLM_BASE_URL, api_key="-")

# Set the model settings
settings = {
    "model": LLM_MODEL,
    "temperature": 0.8,
}


# Set the message response
@cl.on_message
async def on_message(message: cl.Message):
    """
    Responds to a user message by generating text based on the predefined model and settings.

    Parameters:
        message (cl.Message): The user's message.

    Returns:
        None
    """
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot created by AI Singapore. You provide clear and high quality answers.",
                "role": "assistant",
            },
            {"content": message.content, "role": "user"},
        ],
        **settings,
    )
    await cl.Message(content=response.choices[0].message.content).send()
