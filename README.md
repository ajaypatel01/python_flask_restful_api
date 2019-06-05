# restful-api-python-flask
### Build and run docker container with Flask RESTful API
git clone https://github.com/ajaypatel01/python_flask_restful_api.git

Change directory `cd restful-api-python-flask`

Build image `docker build -t restful-api .` 
  
Run container in detached mode and publish port 5000 `docker run -d -p 5000:5000 restful-api`
  
API should be accessible on port 5000 `curl -i localhost:5000/vault/v1.0/users`
