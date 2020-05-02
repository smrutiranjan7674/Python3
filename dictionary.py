import json
import difflib
from difflib import get_close_matches

#loading and opening the json file
data=json.load(open('data.json'))

#function that takes the user input,checks it in data.json & returns the O/P accordingly
def read(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),n=1)) > 0:
        yn=input("Did you mean {}?,Enter Y for Yes N for No: ".format((get_close_matches(w,data.keys(),n=1)[0])))
        if yn == "Y":
            return data[get_close_matches(w,data.keys(),n=1)[0]]
        elif yn == "N":
            return "word not found,please try again"
        else:
            return "Invalid Entry"
    else:
        return "The word doesnt exist"

#taking user input and converting it into lowercase as our data.json is in lowercase
word=input("enter a word:")
word=word.lower()

#making thr o/p more readable
output=read(word)
if type(output) == str:
    print(output)
else:
    for i in output:
        print(i)