# For small documents
file_read = open("NOTE")
file_write = open("NOTE[Copy]", "w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()

# For large documents
file_read = open("NOTE")
file_write = open("NOTE[Copy]", "w")

while True:
    # read a line
    text = file_read.readline()

    # determine if the text is blank
    if not text:
        break

    file_write.write(text)

file_read.close()
file_write.close()
