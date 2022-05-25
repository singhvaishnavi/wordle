import requests
import random

def checkPresence(word_list,word):
    ctr=0
    for i in word_list:
        if i==word:
            ctr=ctr+1
            break
    if ctr==1:
        return True
    return False

def getInput():
    l=0
    word=""
    while l!=5:
        word=input("Enter word: ")
        l=len(word)
        if l!=5:
            print("only 5 letter word, try again")
    return (word)

ul = "https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"
r = requests.get(ul)
r=str(r.text)
ll=r.split()
given_word=random.choice(ll)
found=False
turn=1
print("The following letters indicates:")
print("g: letter is in the right place")
print("y: letter exists in the guess word but is in the wrong place")
print("b: letter does not exist")
word=getInput()
res=""
while found==False and turn<6:
    print("Turn no: ",turn)
    if checkPresence(ll,word)==True:
        res=""
        for i in range(0,5):
            if word[i]==given_word[i]:
                res=res+"g"
            elif checkPresence(given_word,word[i]):
                res=res+"y"
            else:
                res=res+"b"
        print(res)
        if res=="ggggg":
            found=True
            print("You won!")
            break
        else:
            print("Try again")
            word=getInput()
            turn=turn+1
    else:
        print("Word does not exists")
        print("Try again")
        word=input("Enter a word: ")
if turn>=6:
    print(given_word)
