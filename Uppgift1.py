import os

def GetEnvironmentPaths():
    Path = os.environ["PATH"] # eftersom os.environ är en dictionary där keys är string så kan man bara skriva in den man vill ha ifall man printar ut allt så ser man att den heter 'PATH'
    #string.split(separator, maxsplit) - från w3schools, seperator är vad den ska kolla för, maxsplit är automatiskt -1 som gör att den gör så många som möjligt ifall man inte sätter själv
    seperatedPath = Path.split(";")
    for index in range(1, len(seperatedPath)):
        print(f"[{index}] : ", seperatedPath[index])
GetEnvironmentPaths()