file=open ("files.pdf", "w")
file.write("This is python week 4 content it was so amazing.\n")

file=open("files.pdf", "r")
data=file.read()
print(data)

file=open("files.pdf", "a")
file.write("I can't wait for the next session.\n")

file=open('files.pdf', "a")
file.write("I am sure it will even be more intresting.")



try:
 file= open("files.pdf", "r")
 content= file.read()
 print(content)
except FileNotFoundError:
 print("file not found")
 
finally:
 print("file completed")
 file.close()

