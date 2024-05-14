FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    portaudio19-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY .. .

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "web.py", "--server.port=8501", "--server.address=0.0.0.0"]

