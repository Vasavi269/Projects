FROM python:3.9.5

#make a directory for our application in the docker environment
WORKDIR /app

#install dependencies

RUN pip freeze > requirements.txt
#COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install numpy
RUN pip install matplotlib


#copy the source code
COPY WPG.py .


CMD ["python", "WPG.py"]
