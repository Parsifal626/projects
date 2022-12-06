# TODO

from cs50 import get_string

text = get_string("Text: ")

letters = 0
words = 1
sentences = 0

for i in text:
    if i.isalpha():
        letters +=1
    elif i == " ":
        words +=1
        elif == "." or i == "!" or i == "?"