FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libsdl2-dev \
    libsdl2-image-dev \
    libjpeg-dev \
    zlib1g-dev \
    xvfb \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader -d /usr/share/nltk_data \
    punkt \
    vader_lexicon \
    averaged_perceptron_tagger \
    stopwords

COPY paintmypoem/ .

ENV SDL_VIDEODRIVER=dummy \
    SDL_AUDIODRIVER=dummy \
    DISPLAY=:99 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p /app/output /app/backgrounds
CMD ["python", "main.py"]
