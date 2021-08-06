FROM python:3.9.5

ADD add.py .

CMD ["python", "./add.py"]
