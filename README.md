## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The application developed here takes two texts as input in a web service and produces text similarity between them on a scale of 0 to 1. 

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
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install Flask
   ```sh
   pip install Flask
   ```
4. Go to the folder where you cloned the repo and run below command
   ```sh
   python app.py
   ```
   #### Possible output: 
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

5. Open your browser and type in "http://127.0.0.1:5000/"
   If done correctly you will see the screen as shown above.


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

