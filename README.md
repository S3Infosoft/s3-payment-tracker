# s3-payment-tracker

#### Initial Steps
- Build the Docker image
  ```
  docker build .
  ```
- Build the Docker image using docker-compose
  ```
  docker-compose build
  ```
- Migrate the models to database
  ```
  docker-compose run --rm app sh -c 'python manage.py makemigrations'
  docker-compose run --rm app sh -c 'python manage.py migrate'
  ```
#### To create a superuser
- ```
  docker-compose run --rm app sh -c 'python manage.py createsuperuser'
  ```
- Login to admin page
  <http://localhost:4000/admin/>

#### To run the server
-   ```
    docker-compose up
    ```
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
