FROM python:3.12.1-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8889
CMD ["python", "app.py"]
