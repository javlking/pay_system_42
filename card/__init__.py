from pydantic import BaseModel


# Класс для валидации добавления карты
class CardAddModel(BaseModel):
    pass


# Класс для валидации изменения дизайна карты
class EditCardModel(BaseModel):
    pass
