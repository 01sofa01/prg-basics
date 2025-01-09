try:
    with open('08-FileHandling/pets.txt') as file:
        file_content = file.read()
        print(file_content)
        file_content = file_content.split()
        print(len(file_content))
except:
    print("niema takiego pliku")
