import random
from time import *
import pyttsx3

print("""WELCOME TO MY SPELLING BEE GAME
THIS IS TO TEST YOUR ABILITY ON SPELLING
NOW YOU ONLY GOT 20 SECONDS AFTER THAT
TIME LIMIT YOU LOSE 
AN EXAMPLE IS BEING DONE FOR YOU TO SHOW YOU HOW IT WORKS""")
class SpellingBeeGame:
    def __init__(self,word_file):
        self.word_list=self.read_word_file(word_file)
        self.engine=pyttsx3.init()
        self.time_limit=20

    def read_word_file(self,filename):
        with open(filename,"r") as file:
            return [line.strip() for line in file]
    def choose_word(self):
        return random.choice(self.word_list)

    def speak_word(self,word):
        self.engine.say(word)
        self.engine.runAndWait()

    def start_game(self):
        currentword=self.choose_word()
        self.speak_word(currentword)
        print(f"word:{currentword}")
    def check_spellings(self,user_input):
        correctword=self.choose_word()
        self.speak_word(correctword)
        start_time=time()

        while True:
            user_word=input("spell the word:").upper()
            elapsed_time=time()-start_time

            if user_word==correctword:
                print(f"Correct! you spelt it right in {elapsed_time:.2f}seconds. ")
                break
            elif elapsed_time > self.time_limit:
                print("Time's up! You took too long",correctword)
                break
            else:
                print("Oops! you missed it,try again")

if __name__=="__main__":
    game=SpellingBeeGame("C:/Users/USER/Desktop/myDICTIONARY.txt")
    game.start_game()
    game.check_spellings(input("enter your word"))

