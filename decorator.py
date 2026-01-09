#calculate time taken to execute a program 
import time
from functools import wraps
import logging
from typing import TypedDict


logging.basicConfig(level=logging.INFO,format ="%(asctime)s | %(levelname)s | %(message)s")

# duration check
def times(func):
    @wraps(func)
    def wrapper(*args, **kwargs): 
        try:
            start = time.time()
            logging.info(f"{func.__name__} start at : {start}")
            result=func(*args, **kwargs)
            end =time.time()
            duration = end -start
            logging.info(f"{func.__name__} End at : {end} and total duration is {duration}")
            return result
        except Exception as e:
            logging.exception("{func.__name__ }Error occurred while executing the function")
            raise
    return wrapper

@times
def original_function( a: int , b : int ):
    c : int = a+b
    print(c)
original_function(3,4)
 
 # logging detail 
def log_in(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
       st = time.time()
       logging.info(f" Starting {func.__name__}... args = {args}, kwargs = {kwargs}")
       try:
          result = func(*args,**kwargs)
          return result 
       except Exception as e:
          logging.exception(f"{func.__name__} has {e}")
          raise RuntimeError(e)
       finally:
          end = time.time()
          logging.info(f"{func.__name__} end at {end-st:.4f}s")      
    return wrapper

@log_in
def original_function( a: int , b : int ):
    c : int = a+b
    print("output : ",c)
original_function(3,4)

# check performance
def performance(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
      st = time.time()
      try:
        result = func(*args,**kwargs)
      except Exception as e:
         logging.exception(f"{func.__name__} is crashed : {e}")
         return
      finally:
         duration = time.time() - st
         if duration > 0.5:
            logging.warning(f"{func.__name__} slow:{duration:.3f}s")
         else:
            logging.info(f"{func.__name__} fast: {duration:.3f}s")   
      return result
   return wrapper

def userdata(TypeDict):
   name: str
   age : int
   city: str

@performance
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

# output using cache 
def cache(func):
    store = {}
    @wraps(func)
    def wrapper(*args):
        if args in store:
            return store[args]
        result= func(*args)
        store[args]= result
        return result
    return wrapper

@cache
def sq(n: int) -> int:
    print(" calculating...")
    return n*n

print(sq(3))
print(sq(22))

# permission check 
def required_roles(allowed_roles):
    def deco(func):

        @wraps(func)
        def wrap(user,*args,**kwargs):
            role = user.get("role")
            if role not in allowed_roles:
                logging.warning(f"access denied | user_role= {role} | Function name = {func.__name__}")
                raise PermissionError("Access Denied")
            logging.info(f"Access Granted | user_role = {role} | func = {func.__name__}")
            result = func(user,*args,**kwargs)
            return result
        return wrap
    return deco
@required_roles(["admin","modefier"])
def user_del(User):
    print("User Deleted")

admin = {"role":"admin"}
mod = {"role":"modefier"}   
user = {"role": "user"}
user_del(admin)
user_del(mod)
user_del(user)

# n time run prodram
def timer(times):
    def deco(func):
        @wraps(func)
        def wrap(*args,**kwargs):
            for i in range(1,times+1):
                try:
                    result = func(*args,**kwargs)
                except Exception as e:
                    logging.exception(f"Attempts {i} failed :{e}")
                    raise
                if i == times:
                    raise 
                time.sleep(1)
                return result
            return wrap
        return deco

# rate limit
def rate_limit(max):
    calls= []
    def deco(func):
        @wraps(func)
        def wrap(*args,**kwargs):
            now= time.time()
            while calls and now -calls[0] >60:
                calls.pop(0) 
            if len(calls) >= max:
                raise RuntimeError("rate limit exceeded")
            calls.append(now)
            return func(*args,**kwargs)
        return wrap
    return deco

@rate_limit(2)
def hello():
    print("Hello")
hello()
hello()
hello()   




