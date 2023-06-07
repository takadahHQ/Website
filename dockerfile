FROM python:3.11

WORKDIR /Takadah

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000

CMD ["python", "remote.py", "runserver", "0.0.0.0:8000"]