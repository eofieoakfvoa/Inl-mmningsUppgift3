import Uppgift2Modul
def Main():
    running = True
    while running:
        print("Skriv en ett namn på en systemvariable inom os.environ")
        userInput = input()
        Uppgift2Modul.PrintEnivorn(userInput)
Main()