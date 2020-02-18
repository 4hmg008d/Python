def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

# effect of adding a '*'
print(args)
print(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


# effect of adding a '*'
print(kwargs)
print(*kwargs)

# This would give error because **kwargs is internally translated as:
# arg1=Geeks, arg2=for, arg3=Geeks
# but *kwargs and *args will work fine for tuple
# print(**kwargs)
