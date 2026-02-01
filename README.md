🚀 Быстрый запуск (Windows/PowerShell)
1. Установка зависимостей
powershell
pip install -r requirements.txt
2. Запуск тестов + HTML отчет
powershell
python -m pytest tests/ -v -s --html=report.html --self-contained-html
3. Открыть отчет
Открой report.html в браузере — увидишь 5 PASSED тестов с деталями.

🐳 Docker (CI/CD-ready)
powershell
# Сборка
docker build -t saucedemo-tests .

# Запуск тестов
docker run saucedemo-tests pytest tests/ -v --html=report.html

# С Allure (опционально)
docker run -p 8080:8080 saucedemo-tests
Отчет: http://localhost:8080

