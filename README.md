# Local AI Agent using LangChain + Ollama (Phi-3)

A simple **local AI chatbot agent** built using **LangChain** and **Ollama**, powered by the **Phi-3 model** running entirely on your machine.

This project demonstrates how to build an AI assistant **without using any external APIs or API keys**, leveraging a locally hosted LLM.

---

## Table of Contents
- Features
- Tech Stack
- Project Structure
- Setup & Installation
- How It Works
- Usage
- Example Run
- Key Learnings
- Future Improvements

---

## Features

- Runs completely locally (no API costs)
- Uses Phi-3 model via Ollama
- Built with LangChain agents
- Interactive CLI-based chatbot
- Easily extendable with tools (calculator, APIs, etc.)

---

## Tech Stack

- Python 3.x
- LangChain
- LangChain Ollama Integration
- Ollama (Local LLM runtime)
- Phi-3 Model
- python-dotenv

---

## Project Structure

llm/
│── main.py          # Main application file  
│── .env             # Environment variables (optional)  
│── README.md        # Project documentation  
│── pyproject.toml   # Dependencies (uv)  

---

## Setup & Installation

### 1. Install Ollama

Download and install from:  
https://ollama.com

---

### 2. Pull and run the Phi-3 model
ollama run phi3

## How It Works

This project follows a client-server architecture.
### Components
1. Ollama Server
- Runs locally on http://localhost:11434
- Hosts the Phi-3 model
- Processes prompts
2. LangChain (ChatOllama)
- Sends HTTP requests to Ollama
- Receives responses
- Formats output
3. Agent (create_agent)
- Manages conversation flow
- Can be extended with tools

## Flow
User Input
→
LangChain Agent
→
ChatOllama
→
Ollama Server (localhost:11434)
→
Phi-3 Model
→
Response → User

## Key Learnings
- Difference between local models and API-based models
- Understanding client-server architecture
- How LangChain interacts with LLM backends
- How Ollama exposes a local REST API
- Building a basic AI agent loop