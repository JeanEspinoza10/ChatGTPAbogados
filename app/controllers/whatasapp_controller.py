from flask import request
import os
from app.utils.obtencion_messages import GetTextUser
from app.utils.generate_messages import Generate
from app.utils.send_messages import SendMessageWhatsapp
from app import db
from app.controllers.chattext_controller import UsetText
from app.plantillas.bienvenida_messages import TextPresentacion
from app.plantillas.finalizando_messages import TextFinalizar
from app.plantillas.respuesta_messages import TextChat
class Webhook:
    def VerifyToken(query):
        try:
            accessToken = os.environ.get("ACCES_TOKEN")
            token = query.args.get("hub.verify_token")
            challenge = query.args.get("hub.challenge")
            suscribe=query.args.get("hub.mode")
            if token != None and challenge != None and token == accessToken:
                challenge = int(challenge)
                return challenge
            else:
                return "No se valido correctamente", 400
        except: 
            return"Error", 400
    
    def ReceiverMessage(query):
        try:
            
            
            #Obtener el texto y el numero telefonico
            body = query.get_json()
            
            entry = (body["entry"])[0]
            changes = (entry["changes"])[0]
            value = (changes["value"])
            message = (value["messages"])[0]
            number = message["from"]
            text = GetTextUser(message)
            text = text.lower()
            # Obtener el perfil
            contacts = (value["contacts"])[0]
            profile = contacts["profile"]
            name = profile["name"]
            
            data = {
                "name":name,
                "phone": number,
                "text": text,
            }
            
            # Evaluando el texto:
            if "finalizar" in text:
                controller = UsetText()
                deshabilitando = controller.delete(data)
                datafinalizar = TextFinalizar(number)
                
                enviar = SendMessageWhatsapp(datafinalizar) 
                return "EVENT_RECEIVED"
            elif "hola" in text:
                # Obtencion del formato de envio
                data = TextPresentacion(number, name)
                for dato in data:
                    #Envio de mensaje
                    enviar = SendMessageWhatsapp(data=dato) 
                return "EVENT_RECEIVED"
            else:
                # Grabando datos en tabla
                controller = UsetText()
                grabando = controller.create(data)
                print(grabando)

            
                # Obtencion del formato de envio
                controller_generate = Generate()
                respuesta_chatbot = controller_generate.Message(number)
                data = TextChat(number, respuesta_chatbot)
                enviar = SendMessageWhatsapp(data)    
                return "EVENT_RECEIVED"

            
        except Exception as e:
            print("Error 1", e)
            return "EVENT_RECEIVED"