import time

print("Hello from CI/CD pipeline!")
print("App is now running as a background service...")

# Заставляем контейнер жить вечно
while True:
    time.sleep(60)
