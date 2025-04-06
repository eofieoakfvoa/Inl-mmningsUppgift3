import Uppgift3Modul
def Main():
    running = True
    while running:
        list = None # resettar mellan varje gång
        print("Skriv en ett path till en av dina mappar/katalog/directoyr på din dator för att få en lista på alla filer")
        userInput = input()
        list = Uppgift3Modul.GetFilesInDirectory(userInput)
        if list == None:
            continue # continue gör så att den skippar allt och början från början i while loopen, detta gör så att allt efter här betyder att listan inte är tom
        print(list)
Main()