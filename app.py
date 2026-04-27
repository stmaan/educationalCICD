from flask import Flask
import os
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    # Читаем переменную, которую нам подкинет Kubernetes
    env_type = os.getenv('APP_ENV', 'unknown')
    return f"""
    <h1>Environment: {env_type.upper()}</h1>
    <p>Success! CI/CD is working for {env_type}.</p>
    <p>Python version: {sys.version}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
