# s3-payment-tracker

## Features
- Sync all Reservations to loyalty web app throght REST API
- View already sync Reservations
- -----------------------------------------------------------------------------------------
## Start with this steps

#### clone this repository by 

- ```bash
  git clone [link for this repo]
  ```
 ### NOTE: 
- Clone loyalty web app repo first with readme file instructions,and make sure that its container is running 

- Go to the project directory
  ```bash
  cd s3-payment-tracker
  ```
- Build the Docker image
  ```bash
  docker build -t [image name]:[tag name] .      or just    docker build .
  ```
- Build the Docker image using docker-compose
  ```bash
  docker-compose build
  ```
#### To run the server
-   ```bash
    docker-compose up
    ```
 #### check your all images
-   ```bash
    docker images
    ```
 #### check your all containers and running containers by
 
-   ```bash
    docker ps -a     and   docker ps
    ```
- -------------------------------------------------------------------------------

At this point, your price-tracker app should be running at port 9000 on your Docker host. On Docker Desktop for Mac and Docker Desktop for Windows, go to http://localhost:4000 on a web browser to see the website. If you are using Docker Machine, then docker-machine ip MACHINE_VM returns the Docker host IP address, to which you can append the port (<Docker-Host-IP>:4000).
  
- ---------------------------------------------------------------------------------------

#### website will be available now at above url
- login with username = "test1234" and password= "test@1234"
- Django administration page will be appear,click on "view site " 
- ----------------------------------------------------------------------------
## Functionality -----> 

 - on clicking view site you will redirect to actual page
 - there will be 2 sections 1.resrvation which are not sync to loyalty web app 2. which are already synced
 - every detail of particular reservation will be shown with "sync" button
 
 #### NOTE: 
- don't delete db.sqlite3 
- first go your loyalty web app repo-->app-->payment_tracker_app-->views.py---->callapi() method
- now change BASE_URL attribute inside callapi() to your loyalty web URL e.g "http://192.168.99.100:9000/" 
- remove this 2 lines        
-                            #locally
-                            BASE_URL='http://127.0.0.1:8000/'
- save file
- make sure you have that .env file where settings.py resides in loyalty app,make sure that you have "recipient"= "your email id" to get emails
- now run both loyalty and tracker containers
- first go to loyalty website and go to admin panel ,just look at how many Users you have their in loyalty app database
- also look at Guest,Profile,Reservation database,bcoz after sync new entries would be there.
- go to payment-tracker website homepage
- click on sync botton to sync reservation into loyalty app
- resrvation will be shown into "already sync" section after successful sync
- check your Users,Profile,Gust,Reservation database again ,new entries would have been created
- check your email ,email will have email id and password for login that is created automatically


- --------------------------------------------------------------------------


#### Admin data
- RoomType (E.g. Superior, Villa)
- Room (E.g. R1, R2)
- MealPlan  (E.g. EP, CP, MAP)
- PaymentModes (E.g. Cash, Card, Razorpay)
- PaymentType (E.g. Advance, Checkin, Checkout, Food, Shuttle, Misc, Debit)
#### Guest data
- Guest
- RoomAllocation
- Reservations
- Payment
