from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# Creando tabla para realizar guardar las conversaciones

class ChatUser(BaseModel):
    __tablename__ = "chatusers"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    phone = Column(String(120))
    text = Column(String(120))
    status = Column(Boolean, default=True)

