file = open("NOTE")

text = file.read()
print(text)
print("-" * 50)
text2 = file.read()
print(text2)

file.close()
