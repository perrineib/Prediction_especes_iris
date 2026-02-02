FROM python:3.9-slim

COPY requirements.txt /server/requirements.txt

WORKDIR /server
RUN pip install -r requirements.txt

COPY train.py train.py
COPY app.py app.py

RUN python train.py

CMD ["uvicorn", "--reload","--host", "0.0.0.0","app:app","--port","8000"]