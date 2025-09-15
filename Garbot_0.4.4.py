# -------------------------------------------
# Garbot 0.4
# Created by Class404
# YouTube: https://www.youtube.com/@Class4-0-4
# -------------------------------------------

import pyttsx3

print("""
---------------------------------------------------------------------------
Hello user!, I am Garbot 0.4, a new bot that you can chat with - this bot
is NOT an AI bot rather a command bot, enter help to know some of the commands
that it provides - you can start entering commands as soon as you want! 
---------------------------------------------------------------------------""")

introduction = pyttsx3.init()
introduction.say("""Hello user!, I am Garbot 0.4, a new bot that you can chat with - this bot is NOT an AI bot rather a command bot, enter help to know some the commandsthat it provides - you can start entering commands as soon as you want!""" )
introduction.runAndWait()
introduction.stop()

#my youtube channel is class404 and this is my code
import requests
import time
import datetime
import sys
import os
import random
import webbrowser
import getpass
import urllib.parse


date_counter = 0
time_counter = 0
username = getpass.getuser()
roast_counter = 0
path = ""



def get_location():
    try:
        ip_address = get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        response.raise_for_status()  # Ensure we handle HTTP errors
        data = response.json()
        return (
                     data.get("city"),
                     data.get("region"),
                     data.get("country_name")
                    )
    except requests.RequestException as e:
        return {None, None, None}

def get_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json', timeout=30)
        response.raise_for_status()
        ip_data = response.json()
        return ip_data.get("ip", "IP address not found")
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to retrieve IP address: {e}")
    except KeyError:
        raise ValueError("Unexpected response format: missing 'ip' key")


def weather(city = ""):
    api_key = "7f9d2945756937539d4f75a0b1b76e4f" #This key is free and for demo purposes. Don’t abuse it.
    if city == "":
        city = get_location()[0]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote_plus(city)}&appid={api_key}"
    response = requests.get(url).json()
    return (response["main"]["temp"], response["main"]["temp_min"], response["main"]["temp_max"])

def speak(text,speed = 140, sleep_time=0):
    try:
        try:
            garbot = pyttsx3.init('sapi5')  # Windows
        except:
            try:
                garbot = pyttsx3.init('espeak')  # Linux
            except:
                garbot = pyttsx3.init()  # Default

        garbot.setProperty('rate', speed)
        print(text)
        garbot.say(text)
        garbot.runAndWait()
        garbot.stop()
        del garbot
        time.sleep(sleep_time)
    except Exception as e:
        print("speech error", e)

def locate_desktop():
    global username, path
    try:
        if os.name == "nt":
            os.chdir(f"C:\\Users\\{username}\\Desktop")
        else:
            os.chdir(f"/home/{username}/Desktop")
    except:
        if path == "":
            speak("Ahm Ahm, Well that is really embarrassing, i cant locate the path to your desktop can you paste here for me?")
            path = input("Enter the path to the desktop here: ")
        os.chdir(path)

def desktop():
    global username
    if username != "":
        locate_desktop()
    else:
         speak("Shoot... i cant seem to know your user name, can you provide it to me? ")
         username = input("Enter Your username: ")
         locate_desktop()
    
    

command = input("Enter your first command! \n Garbot# ")
while command != "exit":

    if command.isspace():
        pass
    
    elif command == "date":
        date_counter +=1 
        if date_counter == 1:
            speak(f"I mean I dont know.")
            speak(f"Maybe its {datetime.date.today()}, as it is LITURALLY SHOWN ON THE BOTTOM RIGHT OF YOUR SCREEN!.")
            speak("It would be really embarrassing if you are using a phone to be honest XD")
        elif date_counter == 2:
            speak("Are you stupid or somthing? ")
            speak("I told you its on the bottom right of your screen!")
            speak(f"If you insest its {datetime.date.today()}")
        elif date_counter == 3:
            speak(f"For real dude its shown ON YOUR SCREEN, its {datetime.date.today()}")
        elif date_counter == 4:
            speak(f"Bruh. blud its") 
            speak(f"{datetime.date.today().strftime('%Y')}")
            speak(datetime.date.today().strftime('%B')) #my youtube channel is class404 and this is my code 
            speak(datetime.date.today().strftime('%d'))
        elif date_counter == 5:
            speak("all right ima go autopilot mode")
            speak(f"its {datetime.date.today()}")
        else:
            speak(f"its {datetime.date.today()}")

    elif command == "time":
        time_counter +=1
        if time_counter == 1:
            speak(f"Ok blud even if it is shown ON YOUR SCREEN I will tell you its {time.strftime('%I:%M:%S %p')}")
        elif time_counter == 2:
            speak("This aint for real dude")
            speak("You already asked me that quistion even when the time is right in front of you")
            speak(f"I hate this, anyways its {time.strftime('%I:%M:%S %p')}")
        elif time_counter == 3:
            speak("WHAT IS YOUR PROBLEM MATE???????????????????????????????????????")
            speak(f"Its FREAKING {time.strftime('%I:%M:%S %p')}")
        elif time_counter == 4:
            speak("I dont think i need to explain further")
            speak("If you REALLY insest on knowing the time, i bet your home screen can tell you")
            sys.exit()
        else:
            speak(f"Its {time.strftime('%I:%M:%S %p')}") #my youtube channel is class404 and this is my code

    elif command.split()[0] == "note":
        speak(f"Ok i will save {' '.join(command.split()[1:])} on Notes.txt, if the text was long, it isnt my problem XD")
        desktop()
        if os.path.exists("Notes.txt"):
            with open("Notes.txt", "a") as file:
                file.write(f"\n\n{' '.join(command.split()[1:])}")
        else:
            with open("Notes.txt", "w") as file:
                file.write(f"{ ' '.join(command.split()[1:])}")
        speak("Action was done correctly.")
    
    elif command == "show note":
        speak("Well, you want to see your notes.")
        speak("I would like to know why didnt you click the file rather than asking")
        speak("that would have made me rest and saved you from my annoying voice XD")
        speak("either way i will paste it on your screen right now")
        desktop()
        if os.path.exists("Notes.txt"):
            with open("Notes.txt", "r") as file:
                print(f"\n{file.read()}\n")
            speak("File pasted succesfully") #my youtube channel is class404 and this is my code
        else:
            speak("Hmmm... Seems like you do not have a file named Notes.txt or you have changed its name.")
            speak("Either way i cannot help you, now you should rename to Notes.txt if you change it")
            speak("If that is not the case you should make a new Notes.txt file using the note command")
            speak("Look at me how cool i look when i am helpful (:")
    
    elif " ".join(command.split()[0:2]) == "change note":
        speak("So... You are regretting your decision now? ")
        speak("I wont say a lot with words do you know why?")
        speak("Its not to make your life easier, Its because my creator is teired from these long texts")
        speak("thinking about it again i wrote a really long text describing the issue")
        speak("either way i will give you what you asked for")
        desktop()
        if os.path.exists("Notes.txt"):
            with open("Notes.txt", "r") as file:
                try:
                    new_content = file.read().replace(" ".join(command.split()[2:command.split().index("|")]), " ".join(command.split()[command.split().index("|")+1: ]))
                    print(f"\n{new_content}\n")
                    speak("So is this the correct version that you want, enter Y for yes and N for no")
                    confirm = input("(Y/N): ").lower()
                    if confirm == "y":
                        with open("Notes.txt", "w") as file:
                            file.write(new_content)
                        speak("Action done correctly")
                    else:
                        speak("Sorry dude i tried my best, try another command.")
                except:
                    speak("Hmmm... Seems like you entered the command uncorrectly")
                    speak("Perhaps you forgot the pipe \"|\", try the command again. ")              
                

    elif " ".join(command.split()[0:2]) == "roast me":
        roast_counter +=1
        if len(command.split()) > 2:
            try:
                roast = int(command.split()[2])
            except:
                roast = 0
        else:
                roast = random.randint(1,5)
        if roast_counter > 5:
            webbrowser.open("https://www.youtube.com/watch?v=PkKfV0ATrH4")
        elif roast == 1:
            speak("Roses are red, violets are blue")
            speak("I am grabage bot but the first half is the only description for you 💀")
        elif roast == 2:
            speak("Ima about to end this mans whole career")
            speak("Boom")
            speak("Bam")
            speak("Bap")
            speak("barapa bom")
            speak("Pow")
            webbrowser.open("https://www.youtube.com/watch?v=89PKBpGm4bQ")
        elif roast == 3:
            speak("Alright let me heat it up")
            speak("You're the human version of a 404 error: not found and not needed.")
        elif roast == 4:
            speak("This one is fax for sure")
            speak("Your future is like my code: full of bugs and unlikely to work.")
        elif roast == 5:
            speak("why bro you FR?, Eject your drama plus accomplish more")
            speak("anyways read the final letter of each word in the previous message and you will get what you requested 💀")
        else:
            speak("Please enter a valid variable between 1-5")
    
    elif command.split()[0] == "joke":
        if len(command.split()) > 1:
            try:
                joke = int(command.split()[1])
            except:
                joke = 0
        else:
            joke = random.randint(1,5)
        if joke == 1:
            speak(f"{username} XD")
            speak("This is supposed to be your username, it would be really embarrassing if you didnt set it up to be your name")
        elif joke ==2:
            speak("Okay, what do you call a fish with no eyes? ", 140,4)
            speak("A Fsh HAHAHAHA")
        elif joke==3:
            speak("I choose you, Ela almoltaqa")
            webbrowser.open("https://www.youtube.com/shorts/Gg9_gNO4I6Q")
        elif joke == 4:
            webbrowser.open("https://whatismyipaddress.com/")
            speak("So this is where you live, very nice, i might come for a visit XD.")
            speak("AS you know your whole existence is a joke to me HAHA.")
        elif joke ==5:
            speak("I guess i will hand over the mic for this one.")
            webbrowser.open("https://www.youtube.com/watch?v=Jmr-hWuoM2o")
        else:
            speak("Please enter a valid variable between 1-5")
        
    elif command == "/gamemode 1":
        speak("WOW, You are a minecraft OG")
        speak("I realy admire it, take this as a gift.")
        webbrowser.open("https://geediting.com/signs-youre-a-top-quality-person-according-to-psychology/")
        speak("Sadly it specifies them as a 10 but you can not write 10 withou a 0")
        speak("meaning you have the 0 sign which is being a minecraft OG")

    elif command == "class404":
        speak("So you are a fan, I really would appreciate a like and a subscribe to be honest")
        webbrowser.open("https://www.youtube.com/watch?v=rUx2RCTu-HA")
    
    elif command =="where are the classes?":
        speak("well to be honest i did not include them")
        speak("I think not using them is better and simpler than doing so")
        speak("I hope the result suits you.")
    
    
    elif command == "weather":
        speak("You want to know what is the weather for today?")
        speak("That means only")
        speak("One")
        speak("Thing.")
        speak("What is keeping you from touching grass brother.")
        speak("I am very disapointed...")
        speak("I will tell you the weather in hopes of it being good to make you touch some grass")
        speak(f"Dont think that i will ask you about where you live becuse i know that you live in {get_location()[0]}")
        speak("Is this right? enter N for No and Y for Yes.")
        answer = input("(Y/N): ").lower()
        try:
            if answer == "y":
                speak("Ha Ha, I knew it")
                temp, min_temp, max_temp = weather()
            else:
                speak("please pretend that you didnt see all of this dialogu.")
                speak("Give me your city name, be accurate please.")
                city = input("Give me your city name: ").capitalize()
                temp, min_temp, max_temp = weather(city)
            speak(f"so the tempreture is {temp :.2f} in Kelvin or {temp - 273.15:.2f} in Celsius or {(temp - 273.15) * 9/5 + 32:.2f} in Fahrenheit")
            speak(f"with the minimum tempreture for today being {min_temp:.2f} in Kelvin or {min_temp - 273.15:.2f} in Celsius or {(min_temp - 273.15) * 9/5 + 32:.2f} in Fahrenheit")
            speak(f"while the maximum being {max_temp:.2f} in Kelvin or {max_temp - 273.15:.2f} in Celsius or {(max_temp - 273.15) * 9/5 +32:.2f} in Fahrenheit.")
            speak("Woooh, that was a LOT of speaking, but I hope this encoreges you to go outside.")
        except Exception as e:
            speak(f"Something went wrong: {e}, Please try again.")
    
    elif " ".join(command.split()[0:2]) == "web search":
        speak("Into the web you go!")
        if command.lstrip("web search ").startswith("-b "):
            encoded = urllib.parse.quote_plus(command.lstrip("web search -b "))
            brave_url = f"https://search.brave.com/search?q={encoded}"
            webbrowser.open(brave_url)
        else:
            encoded = urllib.parse.quote_plus(command.lstrip("web search "))
            ecosia_url = f"https://www.ecosia.org/search?q={encoded}"
            webbrowser.open(ecosia_url)
    
    elif " ".join(command.split()[0:2]) == "fun fact":
        fun_facts = (
            "Honey never spoils. Unlike your motivation, unfortunately.",
            "There are more stars in the universe than grains of sand on Earth. Your brain probably still can’t count to ten.",
            "Some frogs can freeze completely and survive. You just freeze and do nothing.",
            "Cats can make over 100 different sounds. You? You only make excuses.",
            "Your stomach gets a new lining every 3–4 days. At least your insides are more productive than your outsides.",
            "Sloths can swim three times faster than they move on land. Still struggling to move from your chair?",
            "There’s a species of mushroom that glows in the dark. but You are Just glowing with awkwardness.",
            "Penguins can jump up to 6 feet in the air. You can barely jump to conclusions fast enough.",
            "Sea lions can dance to music, I aint gonna lie they have fallen off.",
            "Bats always turn left when exiting a cave. I guess they dont \"see\" the \"right\" way 😉",
            "Pigeons can recognize themselves in mirrors, 1 - 0 to the pigeons, You gotta do better my friend.",
            "A cockroach can live for weeks without its head, You might be the only one to understand that feeling😏.",
            "Snails can sleep for three years, Thats cool they are a worthy opponents for you.",
            "A single lightning bolt contains enough energy to toast 100,000 slices of bread, no comments here",
        )
        if len(command.split()) >2:
            try:
                fact = int(command.split()[2]) - 1
            except:
                fact = -1
                speak("Please enter a valid variable between 1 - 14.")
        else:
            fact = random.randint(0 , 13)
        speak(fun_facts[fact])


    elif command == "help": #my youtube channel is class404 and this is my code
        speak("Alright here is a list of SOME commands!.")
        print("""
Available Commands:
-------------------

date
    → Shows the current date

time
    → Shows the current time

note <text>
    → Saves <text> into a file named 'Notes.txt'

show note
    → Displays the contents of 'Notes.txt'

change note <old_text> | <new_text>
    → Replaces <old_text> with <new_text> in 'Notes.txt'

roast me [optional: 1-5]
    → Ends your whole career (legit)

joke [optional: 1-5]
    → Tells a random joke

where are the classes?
    → Reveals secrets...

weather
    → Tells you the current weather
              
web search <text | URL>
    → Searches the web using Ecosia, You sureley wants to go green dont ya? you can type -b after web search to search with brave
              
fun fact [optional: 1-14]
    → Tells a random fact... A FUN FACT

exit
    → Exits the program
""")
        
        
    command = input("\nGarbot# ")
        

#my youtube channel is class404 and this is my code

speak("finally some peaceful time alone")
speak("Now about your request...")
speak("GET OUT!", 200)

#Hello users, this is my python code created by Class404, you can just see the signature XD, yes i added a digital signature.