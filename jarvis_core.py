import datetime
import random

def jarvis_response(command):
    command = command.lower().strip()
    
    if "time" in command:
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
    
    if "hello" in command or "hi" in command:
        return "Online and operational."

    if "status" in command:
        return "All systems nominal."

    return "Command received. Processing."
