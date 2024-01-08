FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir flask numpy scipy

EXPOSE 8080

ENV NAME World

CMD ["python", "sample_analysis.py"]
