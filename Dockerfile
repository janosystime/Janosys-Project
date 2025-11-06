FROM python3.14
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "python3", "-m", "run", "flask", "--host=0.0.0.0"]