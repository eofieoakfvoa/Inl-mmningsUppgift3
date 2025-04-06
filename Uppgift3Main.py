import Uppgift3Modul
def Main():
    running = True
    while running:
        print("Skriv en ett path till en av dina mappar/katalog/directoyr på din dator för att få en lista på alla filer")
        userInput = input()
        Uppgift3Modul.GetFilesInDirectory(userInput)
Main()