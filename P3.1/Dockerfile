FROM python
COPY flask_app /home/myapp
RUN pip install -r /home/myapp/requirements.txt
EXPOSE 5000
# Ejecutar al instalarS
CMD python3 /home/myapp/main.py