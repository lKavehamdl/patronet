FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .



ENV FLASK_APP run.py
ENV FLASK_ENV development
ENV DB_TYPE 'mysql' 
ENV DB_HOST 'localhost'
ENV DB_USER 'root'
ENV DB_PASSWORD 'k..h3002'
ENV DB_NAME 'patronet'


EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
