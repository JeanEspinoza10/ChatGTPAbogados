from app.utils.openai import GetResponse

def TextPresentacion(number, name):
    data = []
    data_presentacion = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"Bienvenido, *{name}* soy un chatbot que te brinda informacion de leyes peruanas"
                },
                
        }

    data_opciones = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
                "body": f"Realiza tus preguntas, tener en cuenta que: \n1) Para dar por concluida una conversacion y comenzar una nueva, escribir la palabra Finalizar"
                },
    }

    
    


    data.append(data_presentacion)
    data.append(data_opciones)
  

    return data