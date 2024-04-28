# READING A FILE
f = open('Python programs/myfile.txt', 'r') 
text = f.read()# here we are uisng 'r' for reading the file similarly we can use "w" for writing and 'a' for append
print(text)
f.close()
#WRITING TO A FILE
f = open('myfile1.txt', 'w')
f.write("hello, world!")
f.close()