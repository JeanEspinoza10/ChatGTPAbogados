import openai
import os

def createMessages(text_user):
    systemas = "Leyes peruanas"
    
    messages =[
            {"role": "system", "content": f"Eres un asistente legal.{systemas}"}
        
        ]



def GetResponse(messages):
    try:
        openai.api_key = os.getenv("ACCES_TOKEN_CHAT")    
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= messages
            )
        respuesta = result['choices'][0]['message']['content']
        return respuesta
    except Exception as e:
        print(e)

