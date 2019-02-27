import os
from random import randint

def help():
    print("print_file() to print source")
    print("print_res() to print result file")
    print("process() to create a result file from a result copied directly from vulgar")
    print("order() to sort words by lenght")
    
def print_file():
    f = open("source.txt","r")
    print(f.read())
    
def print_res():
    f = open("result.txt","r")
    print(f.read())
    
def process():
    f = open("source.txt","r")
    w = open("result.txt","a+")
    y = 0
    word = []
    print("Adding Words to Dictionary:")
    while True:
        buffer = f.readline()
        if (buffer == ''):
            break
        for x in range(0,len(buffer)):
            word.append(buffer[x])
            if (buffer[x+1]==" "):
                break
        w.write(''.join(word))
        w.write("\n")
        y+=1
        word = []
    print(y,"words added to Dictionary")
        
def sortlen():
    
    f=open("result.txt","r")
    wordList = [[] for x in range(20)]
    currentLength = 0
    while (currentLength < 20):
        word = f.readline()
        word.rstrip()
        while(word!=''):
            if (len(word)-1==currentLength):
                wordList[currentLength].append(word.rstrip('\n'))
            word = f.readline()
        currentLength+=1
        f.seek(0)
    return (wordList)

def sentence():
    lengthInWords = randint(1,8) + randint(0,8) + randint(0,8)
    wordList = sortlen()
    for x in range(0,lengthInWords):
        wordLength = randint(1,5) + randint(0,4)
        if (wordLength == 9):
            wordLength += randint(0,4)
        if (wordLength == 13):
            wordLength += randint(0,4)
        if (len(wordList[wordLength])>0):
            word = wordList[wordLength][randint(0,(len(wordList[wordLength])-1))]
            if (x==0):
                print(word.capitalize(),end=' ')
            elif (x==lengthInWords-1):
                print(word,end='. ')
            else:
                print (word,end=' ')

def paragraph():
    sentences = randint(1,2)+randint(0,4)
    for x in range(sentences):
        sentence()
    print('\n')

def text():
    paragraphs = randint(2,7)
    for x in range(paragraphs):
        paragraph()

def clear():
    if os.path.exists("result.txt"):
        os.remove("result.txt")
        print("result.txt cleared")
    else:
        print("result.txt does not exist")
    
    if os.path.exists("sorted.txt"):
        os.remove("sorted.txt")
        print("sorted.txt cleared")
    else:
        print("sorted.txt does not exist")
