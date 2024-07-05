'''
Implementing a Basic Interaction for LLM framework powered
BotDesign the conversation flow for the bot with a simple 
flowchart or script of the bot’s conversation.Choose an 
LLM framework (e.g., OpenAI GPT-4 or Hugging Face Transformers). 
Implement a basic bot using the chosen framework to handle the 
designed conversation flow. The bot should be able to greet users 
and ask for their name, email, and company. Store the collected information 
in a simple in-memory structure (e.g., a Python dictionary). 

'''




import openai

# Initialize OpenAI API
openai.api_key = 'sk-proj-Yf5wB74X9Nf7MrIVFsucT3BlbkFJmFuHkVIkxsV3CQMhYkq7'

# In-memory structure to store user information
user_info = {}

def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def bot_conversation():
    # Greet User
    greeting = "Hello! Welcome to our service. What is your name?"
    print("Bot:", greeting)
    user_name = input("You: ")
    user_info['name'] = user_name
    
    # Ask for Email
    ask_email = f"Nice to meet you, {user_name}. Could you please provide your email?"
    print("Bot:", ask_email)
    user_email = input("You: ")
    user_info['email'] = user_email
    
    # Ask for Company
    ask_company = "Thank you! And which company do you work for?"
    print("Bot:", ask_company)
    user_company = input("You: ")
    user_info['company'] = user_company
    
    # Thank User
    thank_user = f"Great! Thank you for the information, {user_name}. Have a wonderful day!"
    print("Bot:", thank_user)
    
    # Return collected information
    return user_info

if __name__ == "__main__":
    collected_info = bot_conversation()
    print("\nCollected Information:", collected_info)
