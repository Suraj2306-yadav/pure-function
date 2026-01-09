from typing import Generator

#print n number
def number(n:int)->Generator[object]:
    for i in range(1,n+1):
        yield i  
n:int = int(input("Enter a number: "))
print(*number(n))

#print even number of list
def even_num(n : list)-> Generator[int]:
    for i in n:
        if i%2==0:
            yield i
n = [1,2,3,4,5,6,7,8,9,10]
print(*even_num(n))

#count total no. of line in file
def file(filename:str)->Generator[str,None]:
    try:
        with open (filename,"r") as f:
            for i in f:
                yield i.strip()
    except FileNotFoundError:
        return   
filename:str =input("Enter file name: ")
lines:int=0
for i in file(filename):
    lines+=1
print("total line: ",lines)

# #print Only containing ERROR  
def print_error(filename: str) -> Generator[object]:
    try:
        with open(filename,'r') as f:
            for i in f:
                yield i
    except FileExistsError:
        return
filename : str = input("enter file name : ")
for i in print_error(filename):
    if "ERROR" in i:
        print(i)   

# # count the number of words i
def count (file:str)->Generator[object]:
    try:
        with open(file,"r")as A:
            for i in A:
                yield i 
    except:
        print("file not found")
        return
file:str=input("enter file name:")
word: int=0
for i in count(file):
    word+=(i.split())
print("total word in entered file:",word)

# # stop reading after 10 lines

def read_line(file:str)->Generator[object]:
    try:
        with open(file,"r")as A:
            for i in A:
                yield i 
    except FileNotFoundError:
        print("file not found")
        return
    
file:str=input("enter file name:")
count = 0
for i in read_line(file):
    if count == 10:
        break
    print(i)
    count+= 1

# # skip empty lines
def skip_empty_lines(file:str)->Generator[object]:
    try:
        with open (file,"r")as f:
            for i in f:
                if i.strip():
                    yield i
    except:
        print("file not found")
        return
file:str=input("enter file name:")
for i in skip_empty_lines(file):
    print(i,end="")

# # print yield + content 
def yield_lines(file:str)->Generator[object]:
    try:
        with open (file,"r")as f:
            for i,j in enumerate(f,start = 1):
                       if j.strip():
                          yield i,j.strip()
    except FileNotFoundError:
        print("file not found")
        return
file:str=input("enter file name:")
for i,j in yield_lines(file):
    print(i,j)
     
        
