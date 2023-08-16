import nltk
import random
from nltk.chat.util import Chat, reflections

# Define the chatbot responses
faq_pairs = [
    [
        r"What programs does the university offer?",
        ["The university offers a wide range of programs including Computer Science, Engineering, Business, and more."]
    ],
    [
        r"How do I apply for a program?",
        ["Texo apply for a program, you need to visit the university's official website and follow the application "
         "instructions."]
    ],
    [
        r"What are the admission requirements?",
        ["Admission requirements vary depending on the program. Generally, you need a high school diploma or "
         "equivalent and may need to submit test scores."]
    ],
    [
        r"How much is the tuition fee?",
        ["Tuition fees vary by program. You can find detailed information about tuition on the university's website."]
    ],
    [
        r"Is financial aid available?",
        ["Yes, the university offers various financial aid options. You can find more information on the financial "
         "aid section of the website."]
    ],
    [
        r"What is the campus address?",
        ["The university campus is located at [Campus Address]."]
    ],
    [
        r"Can I schedule a campus tour?",
        ["Of course! You can schedule a campus tour by visiting the university's website and selecting the 'Campus "
         "Tours' section."]
    ],
    [
        r"Can I study part-time?",
        ["Yes, many programs offer part-time study options. You can find more information about part-time programs on "
         "the website."]
    ],
    [
        r"Is there a deadline for applications?",
        ["Application deadlines vary by program. You can find the specific deadlines on the 'Admissions' page of the "
         "website."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't have information on that. Please visit the university's website or contact the "
         "admissions office for more details."]
    ]
]

# Create a chatbot using the defined FAQ pairs
faq_chatbot = Chat(faq_pairs, reflections)

# Main loop to interact with the FAQ chatbot
print("Hello! I'm the University FAQ chatbot. How can I assist you? Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("FAQ Chatbot: Goodbye! Have a great day!")
        break
    response = faq_chatbot.respond(user_input)
    print("FAQ Chatbot:", response)

