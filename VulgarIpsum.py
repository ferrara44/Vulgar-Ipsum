import os
from random import randint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import psutil

#Firefox Headless Settings#
options = Options()
gecko = 'geckodriver.exe'
options.add_argument('-headless')

def manual():
    print("manual() to show this list again")
    print("print_file() to print source.")
    print("print_dic() to print dictionary file.")
    print("addwords() to add words to the dictionary from your source copied directly from vulgar.")
    print("newdict() to create a dictionary file from your source copied directly from vulgar. This automatically overwrites all previously stored words.")
    print("sentence()/text()/paragraph() to get text of the desired length.")
    print("clear() to delete dictionary files.")
    print("getLang() to get a new language from VulgarLang")
manual()
    
def print_file():
    if os.path.exists("source.txt"):
        f = open("source.txt","r", encoding="utf-8")
        print(f.read())
    else:
        print("source.txt does not exist")
    
    
def print_dic():
    f = open("dictionary.txt","r", encoding="utf-8")
    print(f.read())
    
def newdict():
    clear()
    f = open("source.txt","r", encoding="utf-8")
    w = open("dictionary.txt","a+", encoding="utf-8")
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

def addWords():
    f = open("source.txt","r", encoding="utf-8")
    w = open("dictionary.txt","a+", encoding="utf-8")
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

def getDictionary():
    
    f=open("dictionary.txt","r", encoding="utf-8")
    wordList = [[] for x in range(25)]
    currentLength = 0
    while (currentLength < 25):
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
    wordList = getDictionary()
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
                if (randint (0,15)==15):
                    print(word,end='? ')
                elif (randint (0,15)==15):
                    print(word,end='! ')
                else: print(word,end='. ')
            else:
                if(randint(0,10)==10):
                    print (word,end=', ')
                else:print (word,end=' ')
        else:
            x-=1

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
    if os.path.exists("dictionary.txt"):
        os.remove("dictionary.txt")
        print("dictionary.txt cleared")
    else:
        print("dictionary.txt does not exist")
    if os.path.exists("source.txt"):
        os.remove("source.txt")
        print("source.txt cleared")
    else:
        print("source.txt does not exist")

def getLang():
    
    browser = webdriver.Firefox(options=options)
    print("Firefox Initialized successfully")
    browser.get('http://vulgarlang.com')
    print("Accessing VulgarLang...")
    submit = browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/main/article/div[1]/div[1]/center/button")
    submit.click()
    print("Generating new language...")
    wordList = browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/main/article/div[1]/div[3]/div[1]/div[4]/ul").text
    # At this point the whole language is in wordList
    print("Acquired list of words...")
    browser.close()
    for proc in psutil.process_iter():
        if proc.name() == gecko:
            proc.kill()
    print("Firefox and gecko closed.")
    
    clear()
    w = open("source.txt","a+", encoding="utf-8")
    w.write(wordList)
    w.close()
    print('wordList content:')
    print(wordList)
    print('source file content:')
    print_file()
    addWords()
    print("Printing test paragraph:")
    paragraph()
