import os
def GetFilesInDirectory(path):
    if not _DirectoryExists(path): #tycker detta är mer läsbart även fast det bara är en line av kod
        print("Kontrollera att du skrev rätt där det inte finns någon katalog på :", path)
        return
    return os.listdir(path) #https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory #listdir returnar en lista med ALLT i den directoryn, så då returnar jag också det
def _DirectoryExists(path):
    return os.path.isdir(path) #https://stackoverflow.com/questions/8933237/how-do-i-check-if-a-directory-exists-in-python , isdir returnar bara true ifall det är en directory och inget annat