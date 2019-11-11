who = 'I am '
appo: str = 'sorry'
print(appo)

# '+' can be used to concatenate strings
# '*' can be used to print multiple strings
print(who + 'so ' * 10 + appo)


p: float = 1638.4 ** (1 / 3)
x: float = 16 - p
y: float = 4 + 0.125 * (x - 16) - (1 / 512) * (x - 16) ** 2
error: float = x ** (1 / 2) - y
print(error)
