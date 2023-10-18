import redis

# Создать подключение к редису
redis_db = redis.from_url('redis://redis_db')

# Создать запись в базе данных
# redis_db.set("spam", 10)  # {'spam': 10}

# Получить значение из базы
data = redis_db.get("spam")
print(data)

# Задать время существования переменной
redis_db.set("spam2", "Hello")
data2 = redis_db.get("spam2")
print(data2)



