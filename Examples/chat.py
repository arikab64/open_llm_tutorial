#!/usr/bin/env python3

import os
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxx"
os.environ["OPENAI_API_BASE"] = "http://127.0.0.1:8000/v1"


prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            """
            You are a nice helper that answer to chatbot 
            """
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

llm = ChatOpenAI(
    temperature=0,
    max_tokens=4096,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)
memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

# # Start the conversation
while True:
    # Get the user's input
    # human_input = input("Human: ")
    human_input = input(">>> Human: ")
    print(">>> Assistant:")
    # Generate a response from the language model
    response = conversation.predict(input=human_input)
    print()
