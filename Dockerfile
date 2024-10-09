FROM python:3.10-slim

WORKDIR /poopoo
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 80
# RUN lol
CMD ["uvicorn", "cpu_app:app", "--host", "0.0.0.0", "--port", "80"]


# uvicorn cpu_app:app --host 0.0.0.0 --port 8080
# curl -X GET http://127.0.0.1:8080/ping