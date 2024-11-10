import random

# Enhanced Chatbot for Customer Interaction

def chatbot():
    print("ChatBot: Hello! I am here to assist you. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        elif "services" in user_input:
            responses = [
                "We offer AI development, data analysis, and cloud computing services. Which one are you interested in?",
                "Our services include AI, data analytics, and cloud solutions. How can we assist you today?",
                "We specialize in AI, data science, and cloud services. Would you like more information on any of these?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "ai" in user_input:
            responses = [
                "Our AI services include model creation, training, and deployment. Do you have specific requirements?",
                "We offer custom AI solutions for businesses. Would you like to know about pricing or project timelines?",
                "Our AI services range from model development to deployment. How can we assist with your AI needs?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "data analysis" in user_input:
            responses = [
                "We analyze your data to extract meaningful insights. Would you like to discuss a potential project?",
                "Our data analysis services include reporting and insights. What type of data are you looking to analyze?",
                "We provide end-to-end data analysis services. Do you have any specific data-related queries?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "charges" in user_input or "price" in user_input:
            responses = [
                "Our charges depend on the project's scope and complexity. Can you share more details about your requirements?",
                "Pricing varies depending on the complexity of the project. Would you like a customized quote?",
                "We offer competitive rates based on project needs. Would you like a detailed estimate for your project?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "time" in user_input:
            responses = [
                "AI projects typically take between 1 to 6 months. How soon do you need the project completed?",
                "Timelines depend on the project scope, but AI projects can take anywhere from a few weeks to several months.",
                "On average, AI projects take 1-6 months to complete. What kind of timeline are you working with?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "hello" in user_input or "hi" in user_input:
            responses = [
                "Hello! How can I assist you today?",
                "Hi there! What can I help you with?",
                "Hey! How can I be of service?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "thanks" in user_input or "thank you" in user_input:
            responses = [
                "You're welcome! Is there anything else I can help you with?",
                "Glad I could help! Do you have any other questions?",
                "You're welcome! Feel free to reach out if you need anything else."
            ]
            print(f"ChatBot: {random.choice(responses)}")
        else:
            responses = [
                "I'm sorry, I don't quite understand. Could you please ask that again?",
                "I didn't catch that. Could you please clarify your question?",
                "Hmm, I am not sure how to respond to that. Can you ask something else?"
            ]
            print(f"ChatBot: {random.choice(responses)}")

# Run the chatbot
chatbot()
