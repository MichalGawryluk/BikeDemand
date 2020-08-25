FROM python:alpine3.7
COPY . /appbikedemand
WORKDIR /appbikedemand
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app2.py