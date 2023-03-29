from app import db
from app.models.chat_model import ChatUser

class UsetText:
    def __init__(self):
        self.model = ChatUser
    
    def create(self, data):
        try:
            
            new_record = self.model.create(**data)
            db.session.add(new_record)
            db.session.commit()
            return {
                "message": "Se grabo con exito el texto"
            }, 201
            
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error en la grabacion del texto',
                'error': str(e)
            }, 500

    def delete(self, data):
        try:
            phone = data["phone"]
            record = self.model.where(phone=phone).all()
            if record:
                for element in record:
                    element.update(status=False)
                    db.session.add(element)
                    db.session.commit()
                return {
                         'message': f'La conversacion ha finalizado'
                    }, 200
            return {
                 'message': 'No se encontro conversaciones activas con el telefono'
             }, 404
         
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

