import tkinter as tk
import random
import num2words
import datetime
import wikipedia
from googletrans import Translator
import pyttsx3

engine = pyttsx3.init()
# engine.setProperty('rate', 100)
# engine.setProperty('volume', 0.5)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

dictionary = {}

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 8:
        speak("Good Morning sir!")
        print("Good Morning sir!")
    elif hour >= 9 and hour <= 16:
        speak("Good Afternoon sir!")
        print("Good Afternoon sir!")
    else:
        speak("Good Night sir")
        print("Good Night sir!")
    print('''I am your AI friend
I can be your dictionary,game,gist buddy and much more.''')
    speak("I am your AI friend I can be your dictionary,game,gist buddy and much more")


def nameVerifier(realname_blocker,pre_input,user_name):
    while realname_blocker == False:
        speak(f"{pre_input}{user_name}is real name? ")
        name_verifier = input( f"{pre_input}{user_name} is real name? ").lower()
        if name_verifier in positive_statements:
            taken_names.append(user_name)
            print("okay just checking")
            speak("okay just checking")
            realname_blocker = True
            break
        elif name_verifier in negative_statements:
            name_var = " real "
            print('okay')
            speak('okay')
            realname_blocker = True
        elif name_verifier == "":
            print(random.choice(blank_lines_complainer))
            pre_input = "i said "
            break
        elif name_verifier.upper() == "Q":
            print('Q is a key word which means back/exit')
            speak('Q is a key word which means back/exit')
            break
        else:
            print('Sorry thats an invalid input.')
            speak('Sorry thats an invalid input.')
            pre_input = "i said "
            break

def clashing(AI_name,user_name):
    while True:
        if AI_name == user_name:
            clashing_names_brain = ["nothing", "no special reason", "i just felt like naming you that", "i dont know",
                                    "humm,i dont know", "i just felt like", "i just felt like naming you that", "because i felt like naming you that"]
            speak('But why did you choose to name me your own name? ')
            clash_names = input('But why did you choose to name me your own name? ').lower()
            if clash_names in clashing_names_brain:
                print('Okay,no problem\nI was just curious.')
                speak('Okay,no problem\nI was just curious')
                print('Now,lets make a password to secure your information\nPlease ensure its a strong password')
                speak('Now,lets make a password to secure your information\nPlease ensure its a strong password')
                break
            else:
                print('''Ummph,I don't know what that means.\nProbably you made a typo error or maybe you typed something irrelevant to my question.\nAnyways,lets continue that name stuff wasn't so important anyways.''')
                speak('''Ummph,I don't know what that means.\nProbably you made a typo error or maybe you typed something irrelevant to my question.\nAnyways,lets continue that name stuff wasn't so important anyways.''')
                print('Lets make a password to secure your information.\nPlease ensure its a strong password.')
                speak('Lets make a password to secure your information\nPlease ensure its a strong password')
                break
        else:
            print('Now,lets make a password to secure your information.\nPlease ensure its a strong password.')
            speak('Now,lets make a password to secure your information\nPlease ensure its a strong password')
            break

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.resizable(False, False)
        
        self.result = tk.StringVar()
        self.result.set('')
        
        self.entry = tk.Entry(self.root, textvariable=self.result, width=30, font=('Arial', 20), bd=5, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        self.row, self.column = 1, 0
        for button in self.buttons:
            if button == '=':
                tk.Button(self.root, text=button, width=10, height=2, font=('Arial', 15), command=self.calculate).grid(row=self.row, column=self.column, columnspan=2, padx=5, pady=5)
                self.column += 2
            elif button in ['+', '-', '*', '/']:
                tk.Button(self.root, text=button, width=5, height=2, font=('Arial', 15), command=lambda b=button: self.update_result(b)).grid(row=self.row, column=self.column, padx=5, pady=5)
            else:
                tk.Button(self.root, text=button, width=5, height=2, font=('Arial', 15), command=lambda b=button: self.update_result(b)).grid(row=self.row, column=self.column, padx=5, pady=5)
            self.column += 1
            if self.column > 3:
                self.column = 0
                self.row += 1
        
        self.root.mainloop()
    
    def update_result(self, value):
        self.result.set(self.result.get() + value)
        
    def calculate(self):
        try:
            self.result.set(str(eval(self.result.get())))
        except:
            self.result.set('Error')


def word_to_number(word):
    try:
        return int(word)
    except ValueError:
        pass

    try:
        return float(word)
    except ValueError:
        pass

    keywords = {'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10,'eleven': 11,'twelve': 12,'thirteen': 13,'fourteen': 14,'fifteen': 15,'sixteen': 16,'seventeen': 17,'eighteen': 18,'nineteen': 19,'twenty': 20,'thirty': 30,'forty': 40,'fifty': 50,'sixty': 60,'seventy': 70,'eighty': 80,'ninety': 90,'hundred': 100,'thousand': 1000,'million': 1000000,'billion': 1000000000,'trillion': 1000000000000,'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'11': 11,'12': 12,'13': 13,'14': 14,'15': 15,'16': 16,'17': 17,'18': 18,'19': 19,'20': 20,'30': 30,'40': 40,'50': 50,'60': 60,'70': 70,'80': 80,'90': 90,'100': 100,'1000': 1000,'1000000': 1000000,'1000000000': 1000000000,
    }

    if word in keywords:
        return keywords[word]

    try:
        return float(num2words(word))
    except ValueError:
        pass

    raise ValueError('Invalid word: ' + word)

def evaluate_expression(expression):
    tokens = expression.split()
    result = word_to_number(tokens[0])
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = word_to_number(tokens[i+1])
        if operator in ('plus', 'add', 'addition','+'):
            result += operand
        elif operator in ('minus', 'subtract', 'subtraction','-'):
            result -= operand
        elif operator in ('times', 'multiplied', 'by', 'multiply', 'x','*'):
            result *= operand
        elif operator in ('divided', 'over','/'):
            result /= operand
        elif operator in ('percent', 'modules', '%'):
            result %= operand
        else:
            raise ValueError('Invalid operator: {}'.format(operator))
    return result

def play_game():
    # generate a random number between 1 and 100
    number = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    # loop until the user guesses the correct number or runs out of guesses
    guesses = []
    max_guesses = 7
    for i in range(max_guesses):
        guess = get_guess(guesses)
        guesses.append(guess)

        if guess == number:
            print("Congratulations! You guessed the number in", i+1, "guesses.")
            return
        elif i == max_guesses - 1:
            print("Sorry, you ran out of guesses. The number was", number)
            return
        else:
            hint = get_hint(guess, number)
            print("Wrong! Try again.", hint)

def get_guess(guesses):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess in guesses:
                print("You already guessed that number. Try again.")
            elif guess < 1 or guess > 100:
                print("Your guess must be between 1 and 100. Try again.")
            else:
                return guess
        except ValueError:
            print("Invalid input. Your guess must be a number.")

def get_hint(guess, number):
    if guess < number:
        return "The number is higher than your guess."
    else:
        return "The number is lower than your guess."

languages = {
    "afrikaans": "af","albanian": "sq","amharic": "am","arabic": "ar","armenian": "hy","azerbaijani": "az","basque": "eu","belarusian": "be","bengali": "bn","bosnian": "bs","bulgarian": "bg","catalan": "ca","cebuano": "ceb","chichewa": "ny","chinese (simplified)": "zh-cn","chinese": "zh-tw","china": "zh-tw","corsican": "co","croatian": "hr","czech": "cs","danish": "da","dutch": "nl","english": "en","esperanto": "eo","estonian": "et","filipino": "tl","finnish": "fi","french": "fr","frisian": "fy","galician": "gl","georgian": "ka","german": "de","greek": "el","gujarati": "gu","haitian creole": "ht","hausa": "ha","hawaiian": "haw","hebrew": "he","hindi": "hi","hmong": "hmn","hungarian": "hu","icelandic": "is","igbo": "ig","indonesian": "id","irish": "ga","italian": "it","japanese": "ja","javanese": "jw","kannada": "kn","kazakh": "kk","khmer": "km","kinyarwanda": "rw","korean": "ko","kurdish": "ku","kyrgyz": "ky","lao": "lo","latin": "la","latvian": "lv","lithuanian": "lt","luxembourgish": "lb","macedonian": "mk","malagasy": "mg","malay": "ms","malayalam": "ml","maltese": "mt","maori": "mi","marathi": "mr","mongolian": "mn","myanmar (burmese)": "my","nepali": "ne","norwegian": "no","nyanja": "ny","odia": "or","pashto": "ps","persian": "fa","polish": "pl","portuguese": "pt","punjabi": "pa","romanian": "ro","russian": "ru","samoan": "sm","scots gaelic": "gd","serbian": "sr","sesotho": "st","shona": "sn","sindhi": "sd","sinhala": "si","Sinhalese"	:"si","slovak": "sk","slovenian": "sl","somali": "so","spanish": "es","sundanese": "su","swahili": "sw","swedish": "sv","tajik": "tg","tamil": "ta","tatar": "tt","telugu": "te","thai": "th","turkish": "tr","turkmen": "tk","ukrainian": "uk","urdu": "ur","uyghur": "ug","uzbek": "uz","vietnamese": "vi","welsh": "cy","xhosa": "xh","yiddish": "yi","yoruba": "yo","zulu": "zu"
}

def language(lan):
    if lan in languages:
        return languages.keys()

translator = Translator()
taken_names = ["wonderperk"]
negative_statements = ["no", "na", "nope", "capital no", "nada"]
positive_statements = ["yes", "yeah", "yup",
                       "yeah baby", "yes please", "uuhun", "eehen"]

blank_lines_complainer = ['''
please stop entering blank lines''', '''
i dont understand blank lines''']

# user name
user_input = ""


if __name__ == "__main__":
    wishMe()
    name_var = " "
    while True:
        speak(f"what's your{name_var}name? ")
        user_name = input(f"What's your{name_var}name? ").lower()
        if user_name in taken_names:
            print("Sorry that name is taken")
            speak("sorry that name is taken")
        elif len(user_name) in range(10, 20):
            print('Jesse thats a long name !!!')
            speak('Jesse thats a long name !!!')
            realname_blocker = False
            pre_input = ""
            nameVerifier(realname_blocker,pre_input,user_name)
        elif user_name == "":
            print("lol! You can't possibly have a blank name")
        elif len(user_name) > 20:
            name_var = " real "
            print('Name too long!')
            speak('Name too long!')

        else:
            taken_names.append(user_name)
            print(f'Hello {user_name}')
            speak(f'hello {user_name}')
            break

    # AI name
    while True:
        name_var = " "
        speak(f'''what{name_var}would you like to name me? ''')
        AI_name = input(f'''what{name_var}would you like to name me? ''')
        if AI_name == "":
            print('''sorry that's an invalid name''')
            speak('''sorry that's an invalid name''')
        elif len(AI_name) in range(10, 20):
            speak('''Jesse thats a long name !!!''')
            print('''Jesse thats a long name !!!''')
            # speak(f"{AI_name} is that what you really want to name me? ")
            realname_blocker = False
            nameVerifier(realname_blocker,name_var,AI_name)
        else: 
            print(f'''Beautiful\nYou have named me "{AI_name}" ''')
            speak(f'''Beautiful You have named me "{AI_name}" ''')
            break

    # clashing names
    clashing(AI_name,user_name)

    # password master

    Ablock = True
    while Ablock == True:
        while Ablock == True:
            speak('''Create a password''')
            password = input('''Create a password: ''').lower()
            if len(password) > 4:
                speak("confirm password ")
                password_confirmer = input("Confirm password: ").lower()
                if password == password_confirmer:
                    print('''Your password was succesfully saved.''')
                    speak('''Your password was succesfully saved.''')
                    Ablock = False
                    break
                else:
                    print('''Sorry,You need to try again\nThe password did not match.''')
                    speak('''Sorry,You need to try again\nThe password did not match.''')
            elif len(password) < 5:
                while True:
                    speak('''Password too short.It must be at least 5 characters long Create another password: ''')
                    new_password = input('''Password too short.\nIt must be at least 5 characters long.\nCreate another password: ''').lower()
                    if len(new_password) > 4:
                        speak("Confirm password: ")
                        new_password_confirmer = input("Confirm password: ").lower()
                        if new_password == new_password_confirmer:
                            print('''Your password was succesfully saved.''')
                            speak('''Your password was succesfully saved.''')
                            Ablock = False
                            break
                        else:
                            print('''Sorry,you need to try again.\nThe passwords did not match.''')
                            speak('''Sorry,you need to try again.\nThe passwords did not match.''')
                            break

    user_options = ""

    # recurring custom message

    while True:
        if user_options == 'Q':
            print('                  ****************************************************                   ')
            break
        speak(f'''{user_name},what would you like to do?
Enter D to use a dictionary
Enter C to use a calculator
Enter T to Talk with me
Enter G to play games
Enter W to search on wikipedia
Enter TR to use translator
Enter Q anytime you wish to go back, quit
>> ''')
        user_options = input(f'''{user_name},what would you like to do?
Enter D to use a dictionary:
Enter C to use a calculator:
Enter T to Talk with me:
Enter G to play games:
Enter W to search on wikipedia:
Enter TR to use translator
Enter Q anytime you wish to go back/quit:
>> ''').upper()

    # teaching dictionary

        if user_options == "D":
            name_var = " "
            while True:
                user_input = input(f'''
welcome{name_var}to the main dictionary section
Enter T to teach me a new word and its definition
Enter R to retrive a definition  when you input a word (normal dictionary)
Enter G to get a word when you input a definition (reverse dictionary)
Enter V to view all the content of your dictionary
>> ''').upper()
                if user_input == "T":
                    print(f'''
Below is an examplary format for inputing/retrieving words

word:{AI_name}
definition:this is the best english dictionary in the world''')
                    while True:
                        new_word = input('''word: ''').lower()
                        if new_word == "q":
                            name_var = " back "
                            print('''Q is a keyword which means back/exit''')
                            break
                        elif new_word == "":
                            print("no blank line please")
                        else:
                            definition = input("definition: ").lower()

                            if len(definition) > 1:
                                dictionary[new_word] = definition
                                print('''word and definition successfully saved!
    ''')
                            else:
                                print('''sorry,thats an invalid format
    ''')

        # retriving a definition of a word

                elif user_input == "R":
                    while True:
                        search_word = input('''
Enter a word to get its definition
Word: ''').lower()
                        if search_word == "q":
                            name_var = " back "
                            print('''Q is a keyword which means back/exit
    ''')
                            break
                        unknown_word = (search_word in dictionary)
                        if unknown_word == True:
                            print(f'''definition:{dictionary[search_word]}
    ''')
                        elif search_word == "":
                            print("no blank lines please")
                        else:
                            print(f'''Sorry {user_name},
You haven't thaught me the definition of {search_word} ''')

        # viewing all  words learnt by al
                elif user_input == "G":
                    while True:
                        search_definition = input('''
Enter a definition to get its key word
Definition: ''').lower()
                        if search_definition == "q":
                            name_var = " back "
                            print('''Q is a key word which means back/exit
    ''')

                            break
                        elif search_definition == "":
                            print("no blank lines please")
                        else:
                            checked_items = 1
                            condition = False
                            for item in dictionary:
                                while condition == False:
                                    if search_definition == (f"{dictionary[item]}"):
                                        print(f"word: {item}")
                                        condition = True
                                        break
                                    elif checked_items == len(dictionary):
                                        print(f'''sorry {user_name},
You haven't thaught me the key word for '{search_definition}' ''')
                                        condition = True
                                        break
                                    else:
                                        checked_items += 1
                                        break

                elif user_input == "V":
                    print(f'''
Your dictionary knows {len(dictionary)} words in total''')
                    for diction in dictionary:
                        name_var = " back "
                        print(f'''{diction}:  {dictionary[diction]}''')

                elif user_input == "Q":
                    print('''
Back to main menu
    ''')
                    break

    # guess game

        elif user_options == "G":
            while True:
                game_select = input('''
Which game would you like to play?
Enter G1 to play a guess game
Enter G2 to play truth or dare anonymously with a random person
>> ''').upper()
                if game_select == "G1":
                    name_var = " "
                    print(f'''
{user_name.title()},welcome{name_var}to guess the number game 😂
All you have to do is pick a number between 0 and 99
You have seven trials.GOOD LUCK !''')
                    play_again = "y"
                    while play_again.lower() == "y":
                        play_game()
                        play_again = input("Do you want to play again? (y/n) ")
                    print("Thanks for playing!")
                        

                elif game_select == "G2":
                    while True:
                        user_input = input('''
Connecting to server...
>> ''').upper()
                        if user_input == "Q":
                            print('''Q is a key word which means back/exit
    ''')
                            break
                        elif game_select == "":
                            print(random.choice(blank_lines_complainer))
                        else:
                            print("wrong input")
                elif game_select == "":
                    print(random.choice(blank_lines_complainer))
                elif game_select == "Q":
                    print('''Q is a key word which means back/exit
            ''')
                    break
                else:
                    print("invalid option")

                # chat part
        elif user_options == "T":
            active_conversation = ["what would you like to discuss with me?"]
            topics_brain = {
                "i'm depressed": False,
                "nothing": False}

            booleanholder_0 = False
            anonymous_topic = []
            while True:
                if booleanholder_0 == True:
                    pre_input = "i said "
                else:
                    pre_input = ""
                made_talks_starter = input(f'''
{pre_input}what would you like to discuss with me?
>> ''')
                if made_talks_starter in topics_brain:
                    topics_brain[made_talks_starter] = True
                    active_conversation.append(made_talks_starter)
                    break
                elif made_talks_starter == "":
                    print(random.choice(blank_lines_complainer))
                    booleanholder_0 = True
                else:
                    active_conversation.append(made_talks_starter)
                    while user_input != "Q":
                        topics_brain[made_talks_starter] = False
                        user_input = input('''
Oops, I don't know what to say in that line of discussion
Enter C to chat with a real person:
Enter Q to exit:
    ''').upper()

                        if user_input == "":
                            print(random.choice(blank_lines_complainer))
                        elif user_input == 'C':
                            print('''
conversation line would be referred to someone else.(posted on a notice board for volunteerwho would like to engage in a conversation with you) dont worry it would banonimymous................''')
                            anonymous_chat = []
                            users = ["ai", "?"]
                            user_flipper = 0
                            for item in active_conversation:
                                while True:
                                    try:
                                        anonymous_topic.append(
                                            f"{users[user_flipper]}: {item}")
                                        user_flipper += 1
                                        break
                                    except:
                                        user_flipper = 0
                            print(anonymous_topic)
    # anonymous topic is then posted and when complete is appended to topics and somehow addeto the ifs major blood codes

                            break
                    break

                    # major loops
            if topics_brain.get("i'm depressed") == True:
                made_talks_starter = '''
                what happened?'''
                made_talks = [["wrecked my car", "sorry about that", "you are the fault", "me?"], ["lost my uncle", "sorry for your loss", "thaks", "sure"], [
                    "ost my uncle", "sorry for your loss", "thanks", "sure", "oko"], ["st my uncle", "sorry for your loss", "thanks", "sure"]]
                made_talks_count = 0
                made_talks_list_scroller = 0
                max_made_talks = len(made_talks[made_talks_list_scroller])
                booleanholder_1 = False
                booleanholder_2 = False
                # booleanholder_3 = ""    unused for now
                booleanholder_4 = False
                booleanholder_5 = False
                while booleanholder_5 == False:
                    while booleanholder_1 == False:
                        if booleanholder_4 == True:
                            print(random.choice(blank_lines_complainer))
                            user_input = input(f'''i said {made_talks_starter.strip()}
>> ''').lower()
                            booleanholder_1 == True
                        elif booleanholder_4 == False:
                            user_input = input(f'''{made_talks_starter}
>> ''').lower()
                            booleanholder_1 == True

                        while True:
                            selected_list = made_talks[made_talks_list_scroller]
                            if user_input == selected_list[made_talks_count]:

                                made_talks_count += 1
                                booleanholder_2 = True
                                try:
                                    print(f'''
{selected_list[made_talks_count]}''')
                                    active_conversation.append(
                                        selected_list[made_talks_count])
                                except:
                                    booleanholder_5 = True
                                    booleanholder_1 = True
                                    break
                                if max_made_talks - made_talks_count == 1:
                                    booleanholder_5 = True
                                    booleanholder_1 = True
                                    break
                                else:
                                    user_input = input(">> ").lower()
                                    while True:
                                        if user_input == "":
                                            print(random.choice(
                                                blank_lines_complainer))
                                            user_input = input(f'''i said {selected_list[made_talks_count]}
>> ''').lower()
                                        elif user_input != "":
                                            active_conversation.append(
                                                user_input)

                                            made_talks_count += 1

                                            break
                            elif user_input == "":
                                booleanholder_4 = True
                                break
                            else:
                                if booleanholder_2 == True:
                                    booleanholder_5 = True
                                    booleanholder_1 = True
                                    break
                                else:
                                    if made_talks_list_scroller < len(made_talks)-1:
                                        try:
                                            made_talks_list_scroller += 1
                                        except:
                                            booleanholder_5 = True
                                            booleanholder_1 = True
                                            break
                                    else:
                                        booleanholder_5 = True
                                        booleanholder_1 = True
                                        break

                user_input = input('''
Sorry you have reached a terminal point of the conversation.
Enter C to continue chat with a real person:
Enter Q to exit:
>> ''').upper()
                if user_input == "":
                    print(random.choice(blank_lines_complainer))
                elif user_input == 'C':
                    print('''
conversation line would be referred to someone else.(posted on a notice board for volunteerwho wouldlike to engage in a conversation with you) dont worry it would banonymous..........''')
                    anonymous_chat = []
                    users = ["ai", "?"]
                    user_flipper = 0
                    for item in active_conversation:
                        while True:
                            try:
                                anonymous_chat.append(
                                    f"{users[user_flipper]}: {item}")
                                user_flipper += 1
                                break
                            except:
                                user_flipper = 0

                    print(anonymous_chat)
    # anonymous chat is then posted and when complete is appended to the made talks

    # word calculator

        elif user_options == "C":
            speak(f"HI,{user_name}. This is a multi language format calculator It supports words,digits,symbols and/or mathemathical expressions Enter C to continue: ")
            calculator_type = input(f"HI,{user_name}.\nThis is a multi language format calculator.\nIt supports words,digits,symbols and/or mathemathical expressions.\nEnter C to continue: \n").lower()
            if 'c' in calculator_type:
                while True:
                    expression = input("Enter an expression (e.g., 'one plus two'): \nEnter q to back:\n")
                    if 'q' in expression:
                        print("Good bye sir!")
                        speak("Good bye sir!")
                        break
                    else:
                        try:
                            result = evaluate_expression(expression)
                            print(result)
                        except Exception as e:
                            print('Invalid expression. Please try again.')

            elif 'g' in calculator_type:
                Calculator()

            else:
                print("Check you spellings and try again")

        elif user_options == 'W':
            while True:
                speak("Enter what you want to search on wikipedia Enter q to back ")
                query = input("Enter what you want to search on wikipedia: \nEnter q to back:\n")
                if 'q' in query:
                    break
                else:
                    print('Searching Wikipedia......')
                    speak('Searching wikipedia')
                    try:
                        query = query.replace("Wikipedia","")
                        result = wikipedia.summary(query,sentences=4)
                        print("Acording to wikipedia.........")
                        speak("Acording to wikipedia.........")
                        print(result)
                        speak(result)
                    except Exception as e:
                        print("Error searching Wikipedia!\nCheck you Spelling\nTry Again!")
                        speak("Error searching Wikipedia!\nCheck you Spelling\nTry Again!")

        elif user_options == 'TR':
            while True:
                text = input("Enter quit to exit:\nEnter the text you want to translate:\n")
                if 'quit'in text:
                    print("Good bye sir!")
                    print("                    **********************************                    ")
                    break
                lan_type = input("Enter language type: ").lower()
                language(lan_type)
                try:
                    text = translator.translate(text, dest=lan_type).text
                    print(text)
                except Exception as e:
                    print("Check you spellings and Try again!")

        
            

