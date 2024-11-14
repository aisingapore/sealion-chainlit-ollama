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
            label="Translate a speech",
            message="Translate a paragraph of a famous speech to Indonesian.",
            icon="/public/translate.svg",
        ),
        cl.Starter(
            label="Summarise an essay",
            message="Summarise a famous essay in 300 words.",
            icon="/public/document.svg",
        ),
        cl.Starter(
            label="Suggest an AI Project",
            message="Suggest an idea for an interesting scientific AI project.",
            icon="/public/idea.svg",
        ),
    ]


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
    # Retrieve the current message history from the user session
    message_history = cl.user_session.get("message_history")
    if message_history is None:
        message_history = []

    # Add the user's message to the message history
    message_history.append({"role": "user", "content": message.content})

    # Create a new message object to send the response
    msg = cl.Message(content="")
    await msg.send()

    # Generate a completion stream from the language model
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
