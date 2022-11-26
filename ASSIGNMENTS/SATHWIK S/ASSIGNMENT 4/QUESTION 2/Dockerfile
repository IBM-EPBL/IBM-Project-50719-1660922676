FROM python:3.8
WORKDIR /app
ADD . /app
ENV LISTEN_PORT=8080
EXPOSE 8080
COPY requirements.txt /app
RUN pip install --upgrade pip setuptools
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install ibm-db
EXPOSE 5000
CMD ["python3", "app.py"]