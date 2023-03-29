def TextFinalizar(number):
  
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"Le comunicamos que su conversacion fue finalizada. Si quiere continuar realize su primera consulta."
                },
                
        }

  

    return data