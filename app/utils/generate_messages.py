from app.plantillas import bienvenida_messages

def GenerateMessage(number, name, messageUser):
    
    
    data = None
    data = bienvenida_messages.TextPresentacion(number, name, messageUser)

    return data
    