FROM python:3.6

WORKDIR /test_env

COPY . .

RUN pip install -r requirements.txt

CMD ["python3.6", "-m", "pytest" , "--alluredir=/test_env/tmp/allure"]
RUN ["python3.6", "-m", "allure" , "/test_env/tmp/allure"]