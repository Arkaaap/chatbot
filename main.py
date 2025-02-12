from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the conversation template
template = """
Answer the question below.
Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initialize the model
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""  # Corrected initialization
    print("Welcome to the Sasta ChatGPT! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye", "bye bye"]:
            print("Goodbye!")
            break
        
        # Invoke model with current context
        result = chain.invoke({"context": context, "question": user_input})

        print("Bot:", result)

        # Update context to include the new conversation turn
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()

