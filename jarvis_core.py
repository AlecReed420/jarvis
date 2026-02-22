import datetime
import random
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 165)  # Speed of voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def jarvis_response(command):
    command = command.lower().strip()

    if "time" in command:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    elif "date" in command:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."

    elif "hello" in command or "hi" in command:
        responses = [
            "Online and operational.",
            "Systems active.",
            "Awaiting your command."
        ]
        return random.choice(responses)

    elif "status" in command:
        return "All systems nominal."

    elif "random number" in command:
        return f"Generated number: {random.randint(1, 100)}"

    elif "verse" in command:
        return "Philippians 4:13 — I can do all things through Christ who strengthens me."

    elif "exit" in command or "shutdown" in command:
        return "Shutting down."

    else:
        return "Command not recognized."


# ===== MAIN LOOP =====

print("Jarvis Core Initializing...")
speak("Jarvis core online.")

while True:
    user_input = input("You: ")
    
    response = jarvis_response(user_input)
    
    print("Jarvis:", response)
    speak(response)

    if "exit" in user_input.lower() or "shutdown" in user_input.lower():
        break