from app.plantillas import bienvenida_messages

def GenerateMessage(messageUser, number, name):
    
    
    data = None
      

    data = bienvenida_messages.TextPresentacion(number, name)
    return data
    