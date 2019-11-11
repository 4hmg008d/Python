# anything obtained from 'input' is treated as 'strings'
price = input("Please enter your price: ")
print('Your price is: ' + price)

weight = input('Please enter the weight: ')
print('Your weight is: ' + weight)

# if we need to convert variables type: use 'int()' and 'float()'
price = float(price)
weight = float(weight)

total = price * weight
print('Total cost is: ')
print(total)




