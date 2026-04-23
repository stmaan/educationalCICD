import subprocess

def test_app_runs():
    # Запускаем app.py и проверяем код выхода
    result = subprocess.run(['python', 'app.py'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "CI/CD" in result.stdout
