# указываем язык программирования
FROM python:3.10

#
WORKDIR /pay_system

# Копировать все папки/фалы в Докер
COPY . /pay_system

# установка необходимых компонентов
RUN pip install -r requirements.txt

# команда для запуска
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]



