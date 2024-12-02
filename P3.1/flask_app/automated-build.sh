echo "FROM python" > Dockerfile
echo "COPY flask_app /home/myapp" >> Dockerfile
echo "RUN pip install -r /home/myapp/requirements.txt" >> Dockerfile
echo "EXPOSE 5000" >> Dockerfile
# Ejecutar al instalarS
echo "CMD python3 /home/myapp/main.py" >> Dockerfile

# Eliminamos los contenedores previos

docker stop examen_final
docker rm examen_final
docker build -t examen_final .
docker run -t -d -p 5000:5000 --name examen_running examen_final
docker ps -a
