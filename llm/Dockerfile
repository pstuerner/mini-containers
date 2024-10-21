FROM python:3.10-alpine

ENV OPENAI_KEY=XXXXXXX

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY llm/ /app/llm/

CMD ["python", "-m", "llm"]