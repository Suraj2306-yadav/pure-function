from typing import TypedDict
from typing import Optional

# vowel counter
def count_vowels(text:str)-> str:    
    count : int= 0
    for i in text.lower():
        if i in "aeiou":
            count+=1
    return f"vowels : {count}"  
print(count_vowels("Hello World"))

 #NAME FORMATION
def name (firstname:str,lastname:str )-> str:
   firstname.strip().capitalize()
   lastname.strip().capitalize()
   return firstname +""+ lastname
print(name("vidya","jha"))

# #vaild Email checker 
def vaildemail(email : str) -> str:
    if "@" in email and "." in email and email.index("@") < email.rindex("."):
        return "vaild email" 
    else:
        return "not vaild email"
print(vaildemail("vidyajha13@gmail.com"))
print(vaildemail("vidyajha.gmail@com"))

# # print only allowed list 
class userdata(TypedDict): 
    name:str
    age:int 
    city:str
    
def filter_dict(data: userdata,allowed_keys:list[str])-> userdata:
    new_dict: userdata = {}
    for i in allowed_keys:
        if i in data:
            new_dict[i] = data[i]
    return new_dict
data = {'name': 'vidya', 'age': 21, 'city': 'bhagalpur'} 
allowed_keys = ['name', 'city'] 
result = filter_dict(data, allowed_keys)
print(result)

# #division 
def division (a : int,b : int)-> float | str:
    try:
        if b==0:
            return "division by zero is not allowed"
        return a/b
    except TypeError:
        return "invalid input type"
print("division:10/0",division(10,0)) 

# file handling 
def readfile()-> Optional[str]:     
    try:
        file = open("vidya.txt","w")
        file.write("hello ")
        file.close()
        file = open("vidya.txt","r")
        data:str =file.read()
        file.close()
        return data
    except:
        return "error in file handling"
print(readfile()) 

# #missing number in list
def find_num(num : list[int,None],n: int)-> str:
    new: set[list[int]]= set(num)
    for i in range(1,n+1):
        if i not in new:
            new.add(i)
    return f"list : {new}"

num = [1,2,4,5,7,9]
n=10
print(find_num(num,n))
 
# count word frequency 
def count(text:str)->dict[str,int]:
    words=text.lower().split()
    f:dict[str,int]={} 
    for i in words:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f
print(count("python python is good and humam readable langauage python is a good and powerful language "))    
