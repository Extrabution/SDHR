FROM python:3.10.6

RUN pip install requests

ADD sensor.py /
WORKDIR /
CMD ["python3", "sensor.py"]
