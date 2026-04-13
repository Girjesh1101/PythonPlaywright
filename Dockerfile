FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps chromium

RUN apt-get install -y default-jre wget && \
    wget -O allure.tgz https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz && \
    tar -zxvf allure.tgz -C /opt && \
    ln -s /opt/allure-2.27.0/bin/allure /usr/local/bin/allure

COPY . .

WORKDIR /app/eventhub

CMD ["pytest", "tests/", "--alluredir=../allure-results", "--clean-alluredir"]