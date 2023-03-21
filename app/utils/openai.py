import openai
import os
def GetResponse(text):
    try:
        openai.api_key= os.getenv("ACCES_TOKEN_CHAT")
        result = openai.Completion.create(
            model="text-davinci-003",
            prompt = text,
            n=1,
            max_tokens=500)
        response = result.choices[0].text
        return response
    except Exception as e:
        print(e)
        return e


