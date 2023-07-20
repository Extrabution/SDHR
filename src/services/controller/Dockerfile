FROM python:3.10.6

ADD requirements.txt /
RUN pip install -r requirements.txt
ADD services/controller/app.py /
ADD services/controller/concat_timestamp.py /
ADD services/controller/decision_processor.py /
ADD services/controller/history_dto.py /
ADD services/controller/message_dto.py /