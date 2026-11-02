FROM python:3.11-slim

WORKDIR /app
COPY app/ /app/
COPY content/ /app/content/
ENV PORT=8000 CONTENT_FILE=/app/content/message.txt DATA_FILE=/data/visits.txt
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s CMD python -c "import os,urllib.request; urllib.request.urlopen('http://127.0.0.1:%s/health' % os.environ['PORT'], timeout=2)"
CMD ["python", "main.py"]
