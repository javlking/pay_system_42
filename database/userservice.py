from datetime import datetime

from database.models import User
from database import get_db


# Регистрация пользователя (name, surname, email, phone_number, reg_date, password, city)
def register_user_db(name, surname, email, phone_number, reg_date, password, city):
    db = next(get_db())

    new_user = User(name=name, surname=surname,
                    email=email, phone_number=phone_number,
                    reg_date=reg_date, password=password, city=city)

    db.add(new_user)
    db.commit()

    return "Пользователь успешно зарегистрирован"


# получить информацию о пользователе (user_id)
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    return exact_user


# проверка данных (email)
def check_user_email_db(email):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    return checker


# изменить данные (user_id, edit_type, new_data)
def edit_user_db(user_id, edit_type, new_data):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'email':
            exact_user.email = new_data

        elif edit_type == 'password':
            exact_user.password = new_data

        elif edit_type == 'city':
            exact_user.city = new_data

        db.commit()

        return "Данные успешно изменены"

    return "Пользователь не найден"


# Удалить пользователя (user_id)
def delete_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        db.delete(exact_user)
        db.commit()

        return "Пользователь успешно удален"

    return "Пользователь не найден"

