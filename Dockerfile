
FROM python:3.11

RUN apt-get update && \
    apt-get install -y \
    cron supervisor

WORKDIR /app
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY . .
RUN pip install -U --no-cache-dir -r requirements.txt

EXPOSE  8080 8501

CMD ["bash", "-c", "python3 main.py & streamlit run app.py"]
