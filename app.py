from flask import Flask
import sys
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Hello from CI/CD Pipeline!</h1>
    <p><b>Status:</b> Running in Kubernetes (Kind)</p>
    <p><b>Time:</b> {now}</p>
    <p><b>Python version:</b> {sys.version}</p>
    """

if __name__ == '__main__':
    # Слушаем на порту 80 внутри контейнера
    app.run(host='0.0.0.0', port=80)
