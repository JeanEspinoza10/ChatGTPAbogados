def TextChat(number,text):
  
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"{text}"
                },
                
        }

  

    return data

