FROM python:3.10-slim-bullseye

WORKDIR /app

COPY ./main.py .
COPY ./requirements.txt .
RUN ls -la *
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD [ "main.py" ]
