import random
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer


nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hi!", "Hello! How can I assist you today?"],
    "bye": ["Goodbye!", "Take care!", "See you soon!"],
    "name": ["I'm SupportBot.", "You can call me SupportBot!"],
    "contact": ["Email us at support@example.com", "Call us at 1100-111-4567"],
    "help": ["Sure! What do you need help with?", "I'm here to assist you!"],
    "how are you": ["I'm great, thanks for asking!", "Doing well! How about you?"]
}

def tokenize_and_lemmatize(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokenizer = TreebankWordTokenizer()
    tokens = tokenizer.tokenize(text)
    return [lemmatizer.lemmatize(word) for word in tokens]

def get_response(user_input):
    tokens = tokenize_and_lemmatize(user_input)
    if not tokens:
        return "Can you please type something?"

    for key in responses:
        key_tokens = tokenize_and_lemmatize(key)
        if set(key_tokens).intersection(tokens):
            return random.choice(responses[key])

    return "I'm not sure how to answer that. Try asking something else."

def run_chatbot():
    print("SupportBot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["exit", "quit"]:
            print("SupportBot: Goodbye!")
            break

        reply = get_response(user_input)
        print("SupportBot:", reply)

if __name__ == "__main__":
    run_chatbot()
