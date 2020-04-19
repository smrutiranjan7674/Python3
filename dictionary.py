import json

data=json.load(open("data.json"))

def dict(w):
    w=w.lower()
    if w in data:
        return data[w]
    else:
        return "please check the word you have entered!"

x = input("enter a word: ")

print (dict(x))