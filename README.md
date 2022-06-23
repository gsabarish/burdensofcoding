# Docker Python Fast API App

This app uses a file for dataset (data.json)

Go to fastapidocker folder

### Run 

``` docker build -t fastapi_example . ```

``` docker run --name app -p 8000:8000 fastapi_example ```

### Go to Browser
 
 ``` http://localhost:8000 ```

### Available API Endpoints

``` http://localhost:8000 ```

``` http://localhost:8000/about ```

``` http://localhost:8000/get-item/{item_id} ```

### Clean
 
 ``` docker rm ```

# Docker Python FastAPI MongoDB App 

This app uses MongoDB as a dataset

Mongoseed service pre-populates the db on startup with a sample dataset

GET endpoint returns "Price" for a given "Name"

Go to docker-fastapi-app folder

### Run

``` docker-compose up -d --build ```

### Available API Endpoints

``` http://localhost:8000 ```

``` http://localhost:8000/get-item/Milk ```

### Clean

``` docker-compose stop ``` and ``` docker-compose rm ```
 


  


