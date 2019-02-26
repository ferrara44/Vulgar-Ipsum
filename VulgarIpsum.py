import os

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
        #print(''.join(word),end=",")
        word = []
    print(y,"words added to Dictionary")
        
def sortlen():
    
    f=open("result.txt","r")
    w=open("sorted.txt","a+")
    wordlist = [[] for x in range(20)]
    length = 0
    current_length = 0
    while (current_length < 20):
        word = f.readline()
        word.rstrip()
        while(word!=''):
            if (len(word)-1==current_length):
                wordlist[current_length].append(word.rstrip('\n'))
            word = f.readline()
        current_length+=1
        f.seek(0)
    print (wordlist)
    w.write(str(wordlist))


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
