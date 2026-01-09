class AppError(Exception):
    pass

class vaildationeError(AppError):
    pass

class PermissionError(AppError): 
    pass

class file_handlingError(AppError):
    pass
 
def validate_name(name:str)->str: 
    name = name.strip() 
    if not name.replace(" ","").isalpha() or name.isspace():  
        raise vaildationeError("Name should be only letters and spaces")
    if name =="": 
        raise vaildationeError("not shows name") 
    if len(name)==1 :
        raise vaildationeError("Name is too short")
    if len(name)>=50:
        raise vaildationeError("name is too long")
    return name

def validate_age(age : int) -> int:
    if age<18:
        raise vaildationeError("You are under age")
    if age>30:
        raise vaildationeError("You are over age")
    return age

def validate_email(email:str)->str:
    email = email.strip().lower()
    if (email.count("@") != 1 or "." not in email.split("@")[1]):
        raise vaildationeError("invaild email")
    return email
 
def check_permission(role:str)-> None:
    if role.lower() != "admin":
        raise PermissionError("Admin permission required")

def validate_file(filename:str)->str:
    try:
        with open (filename,"r")as file:
            return file.read()
    except FileNotFoundError as error: 
        return error


        
           
    