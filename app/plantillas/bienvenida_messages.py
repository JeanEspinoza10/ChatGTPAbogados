from app.utils.openai import GetResponse

def TextPresentacion(number, name,text):
    data = []
    message = GetResponse(text)
    data_presentacion = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"Bienvenido, *{name}*"
                },
                
        }

    data_opciones = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
                "body": f"{message}"
                },
    }

    
    


    data.append(data_presentacion)
    data.append(data_opciones)
  

    return data