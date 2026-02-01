FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pytest --alluredir=allure-results

CMD ["allure", "serve", "allure-results"]
