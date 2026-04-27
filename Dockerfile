FROM python:3.10-slim
WORKDIR /app
# Сначала копируем зависимости
COPY requirements.txt .
# Устанавливаем их
RUN pip install --no-cache-dir -r requirements.txt
# Только потом копируем код
COPY app.py .
EXPOSE 80
CMD ["python", "app.py"]
