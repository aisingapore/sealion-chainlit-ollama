from dotenv import load_dotenv
from openai import AsyncOpenAI
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
    LLM_TEMPERATURE = float(os.environ.get("LLM_TEMPERATURE", "0.8"))
except KeyError as e:
    logging.error(f"The environment variable {e} is not defined.")
    sys.exit(1)

# Initialise the client
client = AsyncOpenAI(base_url=LLM_BASE_URL, api_key="-")

# Set the model settings
settings = {
    "model": LLM_MODEL,
    "temperature": LLM_TEMPERATURE,
}

# Initialise the message history
initial_message_history = [
    {
        "role": "user",
        "content": "You are SEA-LION Chatbot, a helpful and knowledgeable assistant.",
    }
]
message_history = initial_message_history


# Set the starters
@cl.set_starters
async def set_starters():
    """
    Define a set of starter prompts that users can choose from.

    Returns:
        list: A list of cl.Starter objects each containing a label, message, and icon.
    """
    return [
        cl.Starter(
            label="Translate a speech to Indonesian",
            message="Translate a well-known historical speech or literary text into Indonesian. Display the original text.",
            icon="/public/translate.svg",
        ),
        cl.Starter(
            label="Summarise an essay",
            message="Summarise a famous essay in 300 words.",
            icon="/public/document.svg",
        ),
        cl.Starter(
            label="Suggest tourist attractions in Thai",
            message="สถานที่ท่องเที่ยวในเชียงใหม่มีอะไรบ้าง?",
            icon="/public/travel.svg",
        ),
        cl.Starter(
            label="Suggest an AI Project",
            message="Suggest an idea for an interesting scientific AI project.",
            icon="/public/idea.svg",
        ),
    ]


# A new chat session is created
@cl.on_chat_start
def on_chat_start():
    # Reset the message history
    message_history = initial_message_history


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
    # Add the user's message to the message history
    message_history.append({"role": "user", "content": message.content})

    # Create a new message object to send the response
    msg = cl.Message(content="")
    await msg.send()

    # Generate a completion stream from the language model
    # Ollama has built-in compatibility with the OpenAI Chat Completions API: https://ollama.com/blog/openai-compatibility
    stream = await client.chat.completions.create(
        messages=message_history, stream=True, **settings
    )

    # Stream tokens from the model's response and update the message
    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)

    # Add the assistant's response to the message history and update the message
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
