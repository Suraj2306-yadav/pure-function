from exception import(
    validate_name,
    validate_age,
    validate_email,
    validate_file,
    check_permission,
    vaildationeError,
    PermissionError,
    AppError
)

def register_user(name: str, age: int, email:str, admin: str)-> str:
    name = validate_name(name)
    age = validate_age(age)
    email= validate_email(email)
    admin  = check_permission(admin) 

    return f" User {name} registered successfully !"

def main():
    try:
        name=input("enter name: ")
        age=int(input("enter age: "))
        email=input("enter email: ") 
        admin=input("Who are you ?")
        
        result=register_user(
            name=name,
            age=age,
            email=email,
            admin=admin
            )
        print(result)
        
        file_result=validate_file("log.txt")
        print("file content:\n",file_result)
        
    except PermissionError as e:
        print(e)
    except vaildationeError as e:
        print(e)
    except AppError as e:
        print(e)
    finally:
        print("\n program finished")

if __name__ == "__main__":
    main()      
        

