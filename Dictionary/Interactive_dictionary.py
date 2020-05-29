import json
from difflib import get_close_matches

data=json.load(open("data.json","r"))

def val_dict(input_string):
        input_string=input_string.lower()
        if input_string in data:
            return data[input_string]

        elif input_string.title()in data:
            return data[input_string.title()]

        elif input_string.upper() in data :
            return data[input_string.upper()]

        elif len(get_close_matches(input_string,data.keys()))>0:
            word_guesssed=(get_close_matches(input_string,data.keys())[0]).upper()
            yn=input("Did you mean %s instead? Enter Y is yes, or N if no: "%word_guesssed)
            if yn=="Y" or yn=="y":
                return data[get_close_matches(input_string,data.keys())[0]]
            elif yn=="N" or yn=="n":
                return "The word doesn;t exist. Please Try again!!"
            else:
                return "We didn't understand your entry."
        else:
            return "The word doesn't exist. Please try again!!"

user_input=input("\nEnter the word: ")
meaning=val_dict(user_input)

if type(meaning)==list:
    for i in meaning:
        print(i)
else:
    print(meaning)
