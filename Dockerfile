FROM python:3.8-alpine


RUN apk update 
RUN pip install --upgrade pip


RUN mkdir /app
COPY  requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt

COPY ./ ./app
WORKDIR /app
RUN  pip install -r requirements.txt


EXPOSE 5000
CMD ["python3", "main.py"]