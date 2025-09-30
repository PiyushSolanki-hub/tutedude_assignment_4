try:
    with open('sample.txt','r') as myfile:
        content = myfile.readlines()
        print("Reading file content:")
        line=1
        for i in content:
            print(f"Line {line}: {i}")
            line+=1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")