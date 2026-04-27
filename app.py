from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"<h1>Успех! CI/CD работает!</h1><p>Контейнер запущен в Kind.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
# Staging environment update
