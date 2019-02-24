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
        
def sort():
    f = open("result.txt","r")
    w = open("sorted.txt","a+")
    word = ''
    og_lines = sum(1 for line in open('source.txt'))
    print("Sorting",og_lines,"words...")
    new_lines = 1
    lenght = 0
    word = f.readline()
    new_lines+=1
    buffer=f.readline()
    while (buffer != ''):
        if (len(buffer)>len(word)):
            word=buffer
            print("change")
        new_lines+=1
        buffer=f.readline()
        buffer.rstrip()
    print(new_lines, "lines read")
    lenght = len(word.rstrip())
    print("Longest word is",word.rstrip(),lenght)

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
