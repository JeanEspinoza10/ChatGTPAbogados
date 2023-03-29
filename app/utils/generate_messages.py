from app.plantillas import bienvenida_messages
from app import db
from app.models.chat_model import ChatUser
from app.utils.openai import GetResponse

class Generate:
    def __init__(self):
        self.model = ChatUser

    def Message(self, number):
        try:
            record = self.model.where(phone=number, status=True).all()
            systemas = "Leyes peruanas"
            messages =[
            {"role": "system", "content": f"Eres un asistente legal.{systemas}"}
        
            ]
            for element in record:
                questions_users = {
                    "role":"user",
                    "content": f"{element.text}"
                }
                messages.append(questions_users)
            data = GetResponse(messages)   
            print(data) 
            return data
        except Exception as e:
            return e
    