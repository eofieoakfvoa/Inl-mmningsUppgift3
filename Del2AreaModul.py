import math #används för att få t.ex math.pi

#dokumentation:
#Denna modul är för att få area av vissa former

#extra info:
#jag använder mig av : float för det gör det lättare att se vad den förväntar sig när man använder sig av den,
#t.ex så står det istället för base = any så står det base = float, så då vet man ungefär vad den förväntar sig. (det står när man skriver funktionen)
#Jag har ingen error handling eftersom jag tror det är bättre ifall man förväntar sig att där den används har error handling istället

#Vad som kan förbättras : 
#ett problem kan vara problem med floating point error, jag vet inte hur man fixar det och jag vet inte hur fel svaren är pågrund av det, 
#det skulle gå att avrunda svaret så borde det vara mer accurate
def GetAreaOfTriangle(base : float, height : float):
    return (base * height) / 2

def GetAreaOfRectangle(base : float, height : float):
    return base * height

def GetAreaOfParallelltrapets(baselength : float, toplength : float, height : float):
    return (height * (baselength + toplength)) / 2

def GetAreaOfCircleRadius(radien : float):
    return math.pi * radien**2

def GetAreaOfCircleDiameter(diameter : float):
    return (math.pi * diameter**2) / 4

def GetAreaOfCirclesektor(radien : float, vinkel : float, arc = None):
    if arc == None:
        if vinkel == None:
            print("please provide an angle or an arc")
            return
        arc = GetArc(vinkel, radien)
    return (arc*radien) / 2
def GetArc(vinkel : float, radien : float):
    return (vinkel / 360) * 2*math.pi*radien