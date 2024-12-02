echo "FROM python" > Dockerfile
echo "COPY flask_app /home/myapp" >> Dockerfile
echo "RUN pip install -r /home/myapp/requirements.txt" >> Dockerfile
echo "EXPOSE 5000" >> Dockerfile
# Ejecutar al instalarS
echo "CMD python3 /home/myapp/main.py" >> Dockerfile

docker build -t examen .