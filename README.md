

# Basic Interaction Bot with OpenAI GPT-4

This repository contains the implementation of a basic interaction bot using the OpenAI GPT-4 framework. The bot is designed to greet users, ask for their name, email, and company, and store the collected information in a simple in-memory structure.

## Features

- Greets the user.
- Asks for the user's name, email, and company.
- Stores the collected information in a Python dictionary.
- Utilizes the OpenAI GPT-4 model for natural language processing.

## Requirements

- Python 3.x
- OpenAI API Key

## Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/kunal654/interaction-bot.git
    cd interaction-bot
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install Required Libraries**:
    ```sh
    pip install openai python-dotenv
    ```

4. **Obtain OpenAI API Key**:
    - Sign up and log in to [OpenAI](https://www.openai.com/).
    - Navigate to the API keys section and create a new API key.
    - Store the API key securely.

5. **Create a `.env` File**:
    - Create a file named `.env` in the project directory.
    - Add your API key to the `.env` file:
      ```
      OPENAI_API_KEY=your-openai-api-key
      ```

## Usage

1. **Run the Bot**:
    ```sh
    python bot.py
    ```

2. **Interact with the Bot**:
    - Follow the prompts to enter your name, email, and company.
    - The bot will store and display the collected information.

## Example Output

```
Bot: Hello! Welcome to our service. What is your name?
You: John Doe
Bot: Nice to meet you, John Doe. Could you please provide your email?
You: john.doe@example.com
Bot: Thank you! And which company do you work for?
You: Example Corp
Bot: Great! Thank you for the information, John Doe. Have a wonderful day!

Collected Information: {'name': 'John Doe', 'email': 'john.doe@example.com', 'company': 'Example Corp'}
```

## Code

```python
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

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
```

## License

This project is licensed under the MIT License.

---

Feel free to modify the content according to your preferences and replace placeholders like `kunal654` and `sk-proj-Yf5wB74X9Nf7MrIVFsucT3BlbkFJmFuHkVIkxsV3CQMhYkq7` with the actual values.
