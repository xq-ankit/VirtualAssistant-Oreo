import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import openai
from myapi import APIKEY

oreo = pyttsx3.init()
oreo.setProperty('rate', 180)
voices = oreo.getProperty('voices')
oreo.setProperty('voice', voices[0].id)

talk = ""


def say(text):
    oreo.say(f"{text}")
    oreo.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold = 1
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("Recognizating...")
        query = r.recognize_google(audio, language="en-in")
        print(f"Lord said: {query}")
        return query
    except Exception as e:
        return ""

samay = int(datetime.datetime.now().strftime("%H%M"))


def time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def wishme():
    if 2400 < samay < 1200:
        say(f'''Good morning! I hope you slept well and woke up feeling refreshed and 
        ready to take on the day. May this morning bring you the energy and positivity you need to 
        accomplish your goals and make the most of every moment. Remember to take some time for yourself 
        today and enjoy the little things that bring you happiness. Have a wonderful day ahead!''')
    elif 1200 < samay < 1600:
        say(f'''Good afternoon! I hope your day has been going well so far. 
        Whether you've been busy with work or enjoying some leisure time, 
        I hope you've been able to find moments of joy and fulfillment. As we move into the afternoon, 
        may your focus and productivity remain strong, and may you continue to make progress towards your goals.
        Take a break when you need it, and remember to take care of yourself.
        Wishing you a happy and successful rest of the day!''')
    else:
        say(f"""Hey lord, it's time to wind down and get some rest. I hope today brought you joy, happiness, 
        and fulfillment. As you prepare to end the day, take a moment to reflect on all the good things that happened, 
        and let go of any negativity that may be weighing you down. 
        Close your eyes, breathe deeply, and let your mind and body relax. 
        May you have a peaceful and restful night's sleep, and wake up tomorrow 
        feeling refreshed and ready to tackle whatever comes your way.
        Good night.... Sweet dreams, my lord!""")


def chat(text):
    global talk

    openai.api_key = APIKEY
    talk += f"Lord: {text}\nOreo: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        reply = response['choices'][0]['text']
        say(reply)
        talk += f"{reply}\n"
        print(talk)
        return reply
    except Exception as e:
        return ""

if __name__ == '__main__':
    print('I am Oreo, your Personal Assistant\nTo close:say "exit system"\n')
    print("----------------------------Made by xq_ankit-----------------------------------")
    say("Hello Lord, I am Oreo your virtual personal assistant")
    while True:
        print("Listening...")
        text = takeCommand()
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["google", "https://www.google.com"],
            ["Instagram", "https://www.instagram.com"],
            ["Wikipedia", "https://www.wikipedia.org"],
            ["GitHub", "https://www.github.com"],
            ["Stack Overflow", "https://stackoverflow.com"],
            ["Amazon", "https://www.amazon.com"],
            ["LinkedIn", "https://www.linkedin.com"]
        ]
        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]} my lord...")
                webbrowser.open(site[1])
        if "file explorer".lower() in text.lower():
            path = r"C:\Users\hp"
            say("Opening file explorer as per your wish my lord...")
            subprocess.Popen(['explorer', path])
            # we cannot directly use subprocess.Popen(path) to open a directory in Windows Explorer.
            # The subprocess.Popen function is used to execute commands, and it expects a list of arguments
            # rather than a single string.


        elif "what's the time" in text.lower() or "what is the time" in text.lower():
            say(time())
        elif "wish me" in text:
            wishme()
        elif "exit system".lower() in text.lower():
            break
        elif "what's your name".lower() in text.lower() or "what is your name".lower() in text.lower():
            say("My name is Oreo, my lord.")
        else:
            chat(text)

