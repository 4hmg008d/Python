file = open("NOTE")

while True:
    text = file.readline()
    print(text)
    if not text:
        break

file.close()