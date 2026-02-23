# Financial-RAG-Agent
An autonomous AI agent built in Python that fetches live stock data and parses local financial PDFs.
# Autonomous AI Financial Research Agent (RAG)

## Overview
This is a Python-based Retrieval-Augmented Generation (RAG) agent designed to automate financial research. It utilizes LLM tool-calling to dynamically decide between fetching real-time market data and extracting text from local unstructured financial documents.

## Features
* **Real-Time Data Integration:** Uses the `yfinance` API to pull live stock market prices.
* **Document Parsing:** Uses `pypdf` to extract raw text from local corporate earnings reports (PDFs).
* **Autonomous Tool Calling:** Powered by the Google Gemini API (`gemini-2.5-flash`), the agent intelligently routes user queries to the correct Python function, synthesizes the data, and returns formatted analytical summaries.

## Tech Stack
* Python
* Google Gemini API (GenAI)
* yfinance
* PyPDF
