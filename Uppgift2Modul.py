import os
def PrintEnivorn(string):
    if not _CheckIfKeyExists(string): #ifall den returnar false så körs koden inom if statementen, tycker detta ser bättre ut än att ha den delen av koden i denna del
        print("Det existeran ingen systemvariable med namnet : ", string)
        return # early return
    #den här delen av koden körs bara ifall os.environ[string] existerar
    print(os.environ[string]) #jag kollade igenom fler av sakerna os.environ valuesna och de värkar inte alla ha t.ex ; för att splita så värkar inte direkt vara värt att göra de, vissa värkar också vara lister istället för att vara en string med ; mellan

def _CheckIfKeyExists(string):
    try: #här försöker den ifall det ger en error så callas except delen annars callas else delen
        os.environ[string]
    except:
        return False
    else:
        return True