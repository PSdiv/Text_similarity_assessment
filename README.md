## About The Project



The application developed here takes two texts as input in a web service and produces text similarity between them on a scale of 0 to 1. 

![alt text](https://github.com/PSdiv/Text_similarity_assessment/blob/main/WebApp_text_similarity.jpg)

Here's what it does:
* If the two texts are exactly same meaning all the words are same in both the texts. Then the output will be 1.0.
* If the two texts are different, then it calculates similarity and outputs the similarity score
* If the two texts don't have any common words, it produces 0.0 as the output score.


### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Docker Images](https://www.docker.com/)
* [DockerHub](https://www.docker.com/)
* Html,CSS

### Solution involes

* Preprocessing of text
- * Removing Punctuations
** Make text case insensitive
** Expand Contractions. Eg: I'm => I am
* Generating TF-IDF vectors from scratch without using Scikit learn
* Cosine similarity metric for calculating similarity scores.


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

There are three ways to test this program:
* Clone the repo and run flask application locally.
* Build docker image and run the docker image locally.
* Pull the docker image and run from docker hub.



### 1. Run Flask application locally.

1. Clone the repo
   ```sh
   git clone https://github.com/PSdiv/Text_similarity_assessment.git
   ```
2. Install Flask
   ```sh
   pip install Flask
   ```
3. Go to the path where you cloned the repo and run below command
   ```sh
   python app.py
   ```
  Possible output: 
 ``` * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 262-475-265 
 ```
4. Try testing using curl 
   ```sh
   curl http://127.0.0.1:5000/results -d '{"text1": "text one","text2":"text two"}' -H 'Content-Type: application/json'
   ```
5. Open your browser and type in "http://127.0.0.1:5000/" \
   If done correctly you will see the screen as shown above.

   
### 2. Build and run Docker Image locally.

1. Clone the repo
   ```sh
   git clone https://github.com/PSdiv/Text_similarity_assessment.git
   ```
2. Go to the path where you cloned the repo and run below command
   ```sh
   docker build -t text_similarity .
   ```
3. In the same path
   ```sh
   docker run -d -p 5000:5000 text_similarity
   ```
4. Try testing using curl 
   ```sh
   curl http://127.0.0.1:5000/results -d '{"text1": "text one","text2":"text two"}' -H 'Content-Type: application/json'
   ```
5. Now the docker is running in port 5000. Open your browser and type in "http://127.0.0.1:5000/" \
   If done correctly you will see the screen as shown above.
   
   
### 3. Pull and run Docker Container from DockerHub.

1. Pull the Docker Image from Docker hub
   ```sh
   docker pull divyadbscience/text_similarity:v2
   ```
2. Run the docker with below command
   ```sh
   docker run -d -p 5000:5000 divyadbscience/text_similarity:v2
   ```
3. Try testing using curl 
   ```sh
   curl http://127.0.0.1:5000/results -d '{"text1": "text one","text2":"text two"}' -H 'Content-Type: application/json'
   ```
4. Now the docker is running in port 5000. Open your browser and type in "http://127.0.0.1:5000/" \
   If done correctly you will see the screen as shown above.


<!-- CONTACT -->
## Contact

Your Name - [Sridivya Pagadala] - divyadbscience@gmail.com

Project Link: [https://github.com/PSdiv/Text_similarity_assessment](https://github.com/PSdiv/Text_similarity_assessment)

