content = input("Enter text to write to the file: ")
with open('output.txt','w') as myfile:
    myfile.write(content)
    print("Data successfully written to output.txt.")
newcontent = input("Enter additional text to append: ")
with open('output.txt','a') as myfile:
    myfile.write(f"\n{newcontent}")
    print("Data successfully appended.")
with open('output.txt','r') as myfile:
    print("Final content of output.txt:")
    allcontent = myfile.readlines()
    for i in allcontent:
        print(i)
