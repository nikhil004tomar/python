# Question no.1: create a new file "pratic.txt" using python. Add the following data in it:
#                     Hi everyone
#                     we are larning File I/O
#                     using Java.
#                     I like programming in Java.

f = open("practic.txt", "w")
data = f.write("Hi everyone\nwe are learning File I/O\nusing Java. ")
data = f.write("\nI like programming in Java.\n")
print(data)

# Question no.2: WAF that replace all occurrences of "java" with "python" in above file.
with open("practic.txt", "r")as f:
    data = f.read()
    print(data)
    new_data = data.replace("Java", "Python")
    print("new_data\n", new_data)
    with open("practic.txt", "w")as f:
        f.write(new_data)

# Question no.3: Search if the word “learning” exists in the file or not.
word = input("enter the string: ")
with open("practic.txt", "r")as f:
    data = f.read()
    if (data.find(word) != -1):
        print("founded")
    else:
        print("not founded")

# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.


def check_for_line():
    words = input("enter the string: ")
    data = True
    line_no = 1
    with open("practic.txt", "r") as f:
        while data:
            data = f.readline()
            if (words in data):
                print(line_no)
                return
            line_no += 1
        return -1


check_for_line()
