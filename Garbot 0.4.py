import pyttsx3

print("""
---------------------------------------------------------------------------
Hello user!, I am Garbot 0.4, a new bot that you can chat with - this bot
is NOT an AI bot rather a command bot, enter help to know some of the commands
that it provides - you can start entering commands as soon as you want! 
---------------------------------------------------------------------------""")

introduction = pyttsx3.init()
introduction.say("""Hello user!, I am Garbot 0.4, a new bot that you can chat with - this bot is NOT an AI bot rather a command bot, enter help to know all the commandsthat it provides - you can start entering commands as soon as you want!""" )
introduction.runAndWait()
introduction.stop()



import time
import datetime
import sys
import os
import random
import webbrowser
import getpass

date_counter = 0
time_counter = 0
username = getpass.getuser()
roast_counter = 0

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
        print("speach error", e)

def desktop():
    if username != "":
        if os.name == "nt":
            os.chdir(f"C:\\Users\\{username}\\Desktop")
        else:
            os.chdir(f"/home/{username}/Desktop")
    else:
         raise Exception

command = input("Enter your first command! \n Garbot# ")
while command != "exit":
    
    if command == "help":
        speak("Alright here is a list of SOME commands!.")
        print("""
date ---> shows current date
time ---> shows current time
note <text> ---> used to make a file named Notes.txt which saves the text you entered
show note ---> shows the Notes.txt file
change note <old_text> | <new_text> ---> removes certin text from the Notes.txt file
roast me ---> he will end your whole career with this one
joke ---> will tell you a random joke
where are the classes? ---> reveales answers
exit ---> its pretty obvious it stops the program
            """)
        
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
            speak(f"{datetime.date.today().strftime("%Y")}")
            speak(datetime.date.today().strftime("%B"))
            speak(datetime.date.today().strftime("%d"))
        elif date_counter == 5:
            speak("all right ima go autopilot mode")
            speak(f"its {datetime.date.today()}")
        else:
            speak(f"its {datetime.date.today()}")

    elif command == "time":
        time_counter +=1
        if time_counter == 1:
            speak(f"Ok blud even if it is shown ON YOUR SCREEN I will tell you its {time.strftime("%I:%M:%S %p")}")
        elif time_counter == 2:
            speak("This aint for real dude")
            speak("You already asked me that quistion even when the time right in front of you")
            speak(f"I hate this, anyways its {time.strftime("%I:%M:%S %p")}")
        elif time_counter == 3:
            speak("WHAT IS YOUR PROBLEM MATE???????????????????????????????????????")
            speak(f"Its FREAKING {time.strftime("%I:%M:%S %p")}")
        elif time_counter == 4:
            speak("I dont think i need to explain further")
            speak("If you REALLY insest on knowing the time, i bet your home screen can tell you")
            sys.exit()

    elif command.split()[0] == "note":
        speak(f"Ok i will save {" ".join(command.split()[1:])} on Notes.txt, if the text was long, it isnt my problem XD")
        desktop()
        if os.path.exists("Notes.txt"):
            with open("Notes.txt", "a") as file:
                file.write(f"{" ".join(command.split()[1:])}")
        else:
            with open("Notes.txt", "w") as file:
                file.write(f"\n\n{" ".join(command.split()[1:])}")
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
            speak("File pasted succesfully")
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
                new_content = file.read().replace(" ".join(command.split()[2:command.split().index("|")]), " ".join(command.split()[command.split().index("|")+1: ]))
                print(f"\n{new_content}\n")
                speak("So is this the correct version that you want, enter Y for yes and N for no")
                confirm = input("(Y/N): ")
                if confirm == "Y":
                    with open("Notes.txt", "w") as file:
                        file.write(new_content)
                    speak("Action done correctly")
                else:
                    speak("Sorrey dude i tried my best, try another command.")

    elif command == "roast me":
        roast_counter +=1
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
    
    elif command == "joke":
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
    command = input("\nGarbot# ")

speak("finally some peaceful time alone")
speak("Now about your request...")
speak("GET OUT!", 200)