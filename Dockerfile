FROM python:3.6

WORKDIR /app

COPY . /app

ENV PATH $PATH:/root/google-cloud-sdk/bin

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN curl https://sdk.cloud.google.com | bash

EXPOSE 80

CMD ["python3", "./deployment/startup.py"]
