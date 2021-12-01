#Pseudo functions
def Initialize():
    pass

def ReadSensor():
    pass

def DataAcquisition():
    pass

def Alert():
    pass

def Display():
    pass

def Timer():
    pass

def Interrupt():
    #Implement interrupt request
    return False

def Delay():
    callable(Timer())
    callable(Terminate())

def Terminate():
    if Interrupt() == False:
        return False


#Pseudo code
callable(Initialize())
def Main():
    while True:
        callable(ReadSensor())
        callable(DataAcquisition())
        callable(Alert())
        callable(Display())
        callable(Delay())

