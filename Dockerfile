FROM python:3.9
WORKDIR /application
COPY . . 
RUN pip3 install -r requirements.txt
RUN python3 create.py
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]