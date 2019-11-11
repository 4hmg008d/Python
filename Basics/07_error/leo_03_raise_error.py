def input_password():
    # type password
    pwd = input("Type password: ")
    # if length >= 8, return password
    if len(pwd) >= 8:
        return pwd
    # if length < 8, raise error
    print("Raise error")
    # 1. create error object
    ex = Exception("Password too short")
    # 2. raise error
    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)