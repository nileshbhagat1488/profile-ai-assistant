FROM python:3.10-slim

WORKDIR /app

RUN pip install torch==2.1.0 --extra-index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt .
RUN pip install --no-deps sentence-transformers==2.7.0 && \
    pip install flask==3.0.3 llama-index-core==0.10.57 llama-index-llms-groq==0.1.4 \
    llama-index-embeddings-huggingface==0.2.2 llama-index-vector-stores-chroma==0.1.10 \
    chromadb==0.5.3 python-dotenv==1.0.1 pypdf==4.2.0 python-docx==1.1.2 \
    transformers huggingface-hub

COPY . .

EXPOSE 7860

ENV PORT=7860

CMD python ingest.py && python app.py