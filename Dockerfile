 #Using the base image with python 3.7
 FROM python:3.7
 
 #Set our working directory as app
 WORKDIR /app 
 
 
 #Installing python packages pandas, scikit-learn and gunicorn
 RUN pip install numpy flask gunicorn
 
 # Copy the models directory and server.py files
 ADD ./static ./static
 ADD ./static/css ./static/css
 ADD ./templates ./templates
 ADD model.py model.py
 ADD requests.py requests.py
 ADD app.py app.py
 
 #Exposing the port 5000 from the container
 EXPOSE 5000
 
 #Starting the python application
 CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]