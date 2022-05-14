import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import smtplib
import requests
import kivy
import json

from kivymd.app import MDApp
from kivy.lang import Builder
from urllib.request import urlopen
from kivymd.uix.button import MDRaisedButton

kv = '''
BoxLayout:
    orientation:'vertical'
    spacing: 30
    space_x: self.size[0]/3
    MDToolbar:
        title: 'MAC-Alexa'
        md_bg_color: app.theme_cls.primary_color
        specific_text_color: 1, 1, 1, 1



    MDBottomNavigation:


    MDIconButton:
        text: 'speak'
        icon: "microphone"
        pos_hint: {"center_x": .5, "center_y": .5} 
        on_press: app.main()  



'''


class Alexa(MDApp):
    def build(self):

        self.title = 'Alexa'
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(kv)

    def main(self):
        listener = sr.Recognizer()
        my_mic = sr.Microphone(device_index=1)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)

        # talk
        def talk(text):
            engine.say(text)
            engine.runAndWait()

        # take command
        def take_command():
            try:
                with my_mic as source:
                    talk('listening...')
                    print('listeneing...')
                    listener.adjust_for_ambient_noise(source)
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice, language ='en-in')
                    command = command.lower()
                    if 'alexa' in command:
                        command = command.replace('alexa', '')
                        print(command)
            except:
                pass
            return command

        class alexaname:
            asname = ''

            def alname(selfff, name):
                selfff.asname = name
                return selfff

        class person:
            name = ''

            def setName(selff, name):
                selff.name = name
                return selff.name

        def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()

            # Enable low security in gmail
            server.login('your email id', 'your email password')
            server.sendmail('your email id', to, content)
            server.close()

        def usrname():
            #for _ in range(3):
                try:
                    name1 = person()
                    talk("What should i call you sir")
                    uname = take_command()
                    name1.setName(uname)
                    talk("Welcome Mister")
                    talk(uname)

                    talk("How can i Help you, Sir")
                except:
                    talk("Please say that again...")
                    #continue
            #else:  # if the loop exited normally, e.g. if all 3 attempts failed
               # pass
               # talk("Please try again....")

        def wishMe():

                hour = int(datetime.datetime.now().hour)

                if hour >= 0 and hour < 12:
                    talk("Good Morning Sir !")

                elif hour >= 12 and hour < 18:
                    talk("Good Afternoon Sir !")

                else:
                    talk("Good Evening Sir !")

                asname = ("alexa 1 point o")
                talk("I am your Assistant")
                talk(asname)




        # Main function
        if __name__ == '__main__':

            wishMe()
            usrname()
            person_obj = person()
            alxaname = alexaname()
            while True:

                command = take_command()

# commands

# play yt
                if 'play' in command:
                    song = command.replace('play', '')
                    talk('playing ' + song)
                    pywhatkit.playonyt(song)
# time
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    talk('Current time is ' + time)
# wikipedia
                elif "wikipedia" in command:
                    webbrowser.open("wikipedia.com")
                    talk("opening wikipedia...")
# where is
                elif "where is" in command:
                    query = command.replace("where is", "")
                    location = query
                    talk("User asked to Locate")
                    talk(location)
                    webbrowser.open("https://www.google.nl / maps / place/" + location + "")
# who is wiki
                elif 'who is' in command:
                    person = command.replace('who is', '')
                    info = wikipedia.summary(person, 1)

                    talk(info)

                elif 'tell me about ' in command:
                    thing = command.replace('tell me about ', '')
                    info = wikipedia.summary(thing, 1)

                    talk(info)
# dating
                elif 'date with me' in command:
                    talk('sorry, I have a headache')
# single
                elif 'are you single' in command:
                    talk('I am in a relationship with wifi')
# exit
                elif 'exit' in command:
                    talk("Thank you for your time")
                    exit()

# jokes
                elif 'joke' in command:
                    talk(pyjokes.get_joke())
# my name
                elif 'my name' in command:
                    if (person_obj.setName == ''):
                        talk('dont know your name, if you tell me i will remember')
                        with my_mic as sources:
                            talk('tell ur name...')
                            listener.adjust_for_ambient_noise(sources)
                            voicess = listener.listen(sources)
                            manames = listener.recognize_google(voicess)
                            maname = manames.lower()
                            person_obj.setName(maname)
                            talk('Okay i will remember that')
                            talk('Your name is' + maname)


                    else:
                        talk('your name is' + person_obj.setName)
# change name to
                elif "change name to" in command:
                    query = command.replace("change my name to", "")
                    alxaname.alname = query
                elif "change your name" in command:
                    talk("What would you like to call me, Sir ")
                    asname = take_command()
                    talk("Thanks for naming me" + asname)
# ur name
                elif "what is your name" in command or "What is your name" in command:
                    talk("My friends call me alexa")

# ur name
                elif "your lover" in command or "lover name" in command:
                    talk("I'm in love with Macucuchi Macusubhi aka Mahesh")

# who made you
                elif "who made you" in command or "who created you" in command:
                    talk("I have been created by Mahesh also known as MACDEVIL.")
# how r u
                elif 'how are you' in command:
                    talk("I am fine, Thank you")
                    talk("How are you, Sir")
# i'm bored
                elif ' bore' in command:
                    talk("may i play you some song")
# fine
                elif 'fine' in command:
                    talk("It's good to know that your fine")
# who i am
                elif "who am i" in command:
                    talk("If you talk then definately your human.")

                elif 'why you came to world' in command:
                    talk("Thanks to Mahesh. further It's a secret")
                elif 'is love' in command:
                    talk("It is 7th sense that destroy all other senses")
                elif 'who are you' in command:
                    talk("I am your virtual assistant created by Mahesh")
                elif 'reason for you' in command:
                    talk("I was created as a Minor project by Mister Mahesh")
# weather in palakkad
                elif "weather in palakkad" in command:
                    talk("Here is the report")
                    webbrowser.open("https://www.accuweather.com/en/in/palakkad/188811/weather-forecast/188811")
# weather today
                # Google Open weather website
                # to get API of Open weather

                elif "weather today" in command:
                    # Google Open weather website
                    # to get API of Open weather
                    api_key = "6ff6c55abc05e2a56dfac5f1f2c3314e"
                    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

                    talk(" City name ")

                    city_name = take_command()

                    # upadting the URL
                    URL = BASE_URL + "q=" + city_name + "&appid=" + api_key
                    # HTTP request
                    response = requests.get(URL)
                    # checking the status code of the request
                    if response.status_code == 200:
                        # getting data in the json format
                        data = response.json()
                        # getting the main dict block
                        main = data['main']
                        # getting temperature
                        temperature = main['temp']
                        # getting the humidity
                        humidity = main['humidity']
                        # getting the pressure
                        pressure = main['pressure']
                        # weather report
                        report = data['weather']
                        talk(f"{city_name:-^30}")
                        talk(f"Temperature: {temperature}")
                        talk(f"Humidity: {humidity}")
                        talk(f"Pressure: {pressure}")
                        talk(f"Weather Report: {report[0]['description']}")
                    else:
                        # showing the error message
                        talk("Error in the HTTP request")
# news
                elif 'news' in command:
                    talk("headlines from BBC news")

                    # BBC news api
                    # following query parameters are used
                    # source, sortBy and apiKey
                    query_params = {
                        "source": "bbc-news",
                        "sortBy": "top",
                        "apiKey": "6d1bebbaa55f45f08530d8fc15bc1d50"
                    }
                    main_url = " https://newsapi.org/v1/articles"

                    # fetching data in json format
                    res = requests.get(main_url, params=query_params)
                    open_bbc_page = res.json()

                    # getting all articles in a string article
                    article = open_bbc_page["articles"]

                    # empty list which will
                    # contain all trending news
                    results = []

                    for ar in article:
                        results.append(ar["title"])



                    # to read the news out loud for us
                    from win32com.client import Dispatch
                    speak = Dispatch("SAPI.Spvoice")
                    speak.Speak(results)
#i love you
                elif "i love you" in command:
                    talk("It's hard to understand")

#good morning
                elif "Good Morning" in command:
                    talk("A warm" + command)
                    talk("How are you Mister")

#email
                elif 'send a mail' in command:
                    try:
                        talk("What should I say?")
                        content = take_command()
                        talk("whome should i send")
                        to = take_command()
                        sendEmail(to, content)
                        talk("Email has been sent !")
                    except Exception as e:

                        talk("I am not able to send this email")

                else:
                    talk('Please say the command again.')


Alexa().run()












