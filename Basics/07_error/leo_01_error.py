try:
    num = int(input("Type a number: "))
    result = 8 / num
    print(result)

# handle specific errors we known
# except ZeroDivisionError:
#     print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid integer")

# handle unknown errors
except Exception as tip:
    print("Unknown error %s" % tip)

print('-' * 50)

