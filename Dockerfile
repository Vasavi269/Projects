FROM python:3.9.5

#make a directory for our application
WORKDIR /task_helloworld

#install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get -qy update && apt-get -qy install libc6-dev && rm -rf /var/lib/apt/lists/*

#copy the source code
COPY helloworld.py .


CMD ["python", "helloworld.py"]
