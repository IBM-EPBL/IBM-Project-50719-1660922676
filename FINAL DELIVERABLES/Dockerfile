FROM python:3.8
WORKDIR /app
ADD . /app
ENV LISTEN_PORT=5000
EXPOSE 5000
COPY requirements.txt /app
RUN pip install --upgrade pip setuptools
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install ibm-db
EXPOSE 5000
CMD ["python3", "app.py"]