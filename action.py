import text_to_speech
import datetime
import webbrowser
import os
import pyjokes


def Action (data) :
    
    user_data = data.lower()

    if "what is your name" in user_data :
        text_to_speech.text_to_speech("My name is Nexa")
        return "My name is Nexa"

    elif "hello" in user_data or "hye" in user_data :
        text_to_speech.text_to_speech("Hey, mam how can i help you")
        return "Hey, mam how can i help you"

    elif "good morning" in user_data :
        text_to_speech.text_to_speech("Good morning mam")
        return "Good morning mam"

    elif "time now" in user_data :
        current_time=datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" , (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data :
        text_to_speech.text_to_speech(" Ok mam")
        return "Ok mam"

    elif "play music" in user_data :
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is now ready for you to play")
        return "gaana.com is now ready for you to play"

    elif "open youtube" in user_data :
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you to play")
        return "youtube.com is now ready for you to play"

    elif "open google" in user_data :
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you to play")
        return "youtube.com is now ready for you to play"
    
    elif "search google for" in user_data:
        query = user_data.replace("search google for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        text_to_speech.text_to_speech(f"Here are the results for {query}")
        return f"Searched Google for {query}"
    
    elif "open calculator" in user_data:
        os.system("calc.exe")
        text_to_speech.text_to_speech("Opening Calculator")
        return "Opening Calculator"
    
    elif "lock my pc" in user_data:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        text_to_speech.text_to_speech("PC locked")
        return "PC locked"
    
    elif "what is your favorite color" in user_data:
        text_to_speech.text_to_speech("My favorite color is blue.")
        return "My favorite color is blue."

    elif "open notepad" in user_data:
        os.system("notepad.exe")
        text_to_speech.text_to_speech("Opening Notepad")
        return "Opening Notepad"
    
    elif "open whatsapp" in user_data:
        os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
        text_to_speech.text_to_speech("Opening Whatsapp")
        return "Opening Whatsapp"
    
    elif "open word" in user_data:
        os.system("start winword")
        text_to_speech.text_to_speech("Opening Microsoft Word")
        return "Opening Microsoft Word"
    
    elif "tell me a joke" in user_data:
        joke = pyjokes.get_joke()
        text_to_speech.text_to_speech(joke)
        return joke

    else :
        text_to_speech.text_to_speech("I am not able to understand!")
        return "I am not able to understand!"