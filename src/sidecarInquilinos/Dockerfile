FROM python:3.10

EXPOSE 50052/tcp

COPY sidecar-requirements.txt ./
RUN pip install --no-cache-dir -r sidecar-requirements.txt

COPY . .

CMD [ "python", "main.py" ]