FROM python:3.10-slim

WORKDIR /app

# Install CPU-only torch first to avoid GPU version being pulled
RUN pip install --no-cache-dir \
    torch==2.1.0+cpu \
    --extra-index-url https://download.pytorch.org/whl/cpu

# Install all other dependencies
RUN pip install --no-cache-dir \
    flask==3.0.3 \
    groq==0.9.0 \
    llama-index-core==0.10.57 \
    llama-index-llms-groq==0.1.4 \
    llama-index-embeddings-huggingface==0.2.2 \
    llama-index-vector-stores-chroma==0.1.10 \
    chromadb==0.5.3 \
    python-dotenv==1.0.1 \
    pypdf==4.2.0 \
    python-docx==1.1.2 \
    sentence-transformers==2.7.0 \
    transformers==4.37.2 \
    tokenizers==0.15.2 \
    huggingface-hub==0.23.4

COPY . .

EXPOSE 7860

ENV PORT=7860

CMD python ingest.py && python app.py
