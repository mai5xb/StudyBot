# StudyBot
A simple, interactive Python chatbot designed to support students while studying programming. It answers FAQs, shares study tips, provides small challenges, and logs all interactions.
The project applies core programming concepts such as loops, functions, conditionals, and file handling.

# Features
Answers frequently asked programming questions
Provides study tips and coding challenges
Logs all user interactions
Separates logic from interface for cleaner design
Beginner‑friendly Python structure

# How It Works
logic.py
Handles all processing:
load_file(study) → reads study.txt
get_response(user_input, content) → finds matching FAQ answers
log_interaction() → saves user questions + bot replies

interface.py
Controls user interaction:
Greets the user and asks for their name
Runs the chatbot using a while loop
Validates commands:
faq
tips
challenge
exit
Tracks usage with counters
Detects section headers like [FAQ], [Tips], [Challenge]

study.txt
Contains three sections:
FAQs + answers
Study tips
Programming challenges

log.txt
Stores interactions in this format:
User: what is a loop?
Bot: A loop repeats code. Python uses 'for' and 'while' loops.
Useful for debugging and tracking user activity.
