import os
import yfinance as yf
from pypdf import PdfReader
from google import genai
from google.genai import types

# 1. Setup the AI
my_api_key = "paste your api key here"
client = genai.Client(api_key=my_api_key)


# ==========================================
#          THE AGENT'S TOOLS
# ==========================================

# Tool 1: The Stock Price Fetcher
def get_stock_price(ticker: str) -> str:
	"""Fetches the current live stock price for a given company ticker symbol (like AAPL or MSFT)."""
	print(f"\n[Agent is picking up the phone to check the price for {ticker}...] ")
	stock = yf.Ticker(ticker)
	todays_data = stock.history(period="1d")
	current_price = todays_data['Close'].iloc[0]
	return f"The current price of {ticker} is ${round(current_price, 2)}"


# Tool 2: The Filing Cabinet Reader
def read_financial_reports() -> str:
	"""Reads and returns the text from all local PDF financial reports in the 'reports' folder."""
	print("\n[Agent is using the magnifying glass to read the PDFs...] ")
	all_combined_text = ""
	for filename in os.listdir("reports"):
		if filename.endswith(".pdf"):
			full_path = os.path.join("reports", filename)
			reader = PdfReader(full_path)
			first_page_text = reader.pages[0].extract_text()
			all_combined_text += f"\n--- DATA FROM {filename} ---\n{first_page_text}"
	return all_combined_text


# ==========================================
#          THE AGENT'S BRAIN
# ==========================================

def run_financial_agent():
	print("Waking up the Ultimate Financial Agent... (Type 'quit' to stop)")

	# 1. Initialize the Chat Agent (Same as before)
	agent_chat = client.chats.create(
		model="gemini-2.5-flash",
		config=types.GenerateContentConfig(
			system_instruction="You are a senior financial analyst. Answer user questions by using your tools. Always summarize financial documents in bullet points.",
			tools=[get_stock_price, read_financial_reports],
			automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
		)
	)

	# 2. The Chat Loop! This keeps the script running forever until you say "quit"
	while True:
		# Ask the user for input
		user_question = input("\nYou: ")

		# Secret kill-switch to stop the code
		if user_question.lower() == 'quit':
			print("Agent: Goodbye! Good luck with your investments.")
			break

		print("Agent is thinking...")

		# Send the message to the AI and print the answer
		response = agent_chat.send_message(user_question)
		print(f"\nAgent: {response.text}")


# Run the whole script
run_financial_agent()