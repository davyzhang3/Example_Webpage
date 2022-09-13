FROM python:3.7-alpine
RUN pip install flask docker coverage
COPY app.py /opt/
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=80
