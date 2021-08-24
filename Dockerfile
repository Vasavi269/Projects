FROM python:3.9.5

#make a directory for our application
#WORKDIR /WavePointGen

#install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy the source code
COPY WPG.py .


CMD ["python", "WPG.py"]
