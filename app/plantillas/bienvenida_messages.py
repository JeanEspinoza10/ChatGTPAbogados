def TextPresentacion(number, name):
    data = []
    
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
                "body": f"Mi nombre es Juan Mendoza"
                },
    }

    data_marca = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
                "body": f"1) Tickets de atencion 📝\n2) Accesos a sistemas informaticos Migraciones\n3) Accesos a sisteams informaticos Pasaporte\n4) Comunicarse con agente de mesa de serivicios 🕵\n5) Retorno de vaciones ✈"
                },

    }
    


    data.append(data_presentacion)
    data.append(data_opciones)
    data.append(data_marca)

    return data