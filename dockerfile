FROM python:3.8-slim
COPY Game.py /Game.py
CMD ["python", "Game.py"]