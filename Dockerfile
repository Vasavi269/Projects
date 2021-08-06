FROM python:3.9.5

#make a directory for our application
WORKDIR /task_helloworld

#install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy the source code
COPY helloworld.py .


CMD ["python", "helloworld.py"]
