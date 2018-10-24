[![Build Status](https://travis-ci.org/RachealN/API-Store-Manager-EndPoints.svg?branch=develop)](https://travis-ci.org/RachealN/API-Store-Manager-EndPoints)
[![Coverage Status](https://coveralls.io/repos/github/RachealN/API-Store-Manager-EndPoints/badge.svg?branch=develop)](https://coveralls.io/github/RachealN/API-Store-Manager-EndPoints?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/0ac41a5a5c76fbb23519/maintainability)](https://codeclimate.com/github/RachealN/API-Store-Manager-EndPoints/maintainability)


#TITLE
 API-Store-Manager

#PREREQUISITES

Requirements

-Python 2.7+ or 3.3+
-Flask 0.10+

Installation
install using pip
```pip install Flask-API```


#API ENDPOINTS

***Admin can add a product***'/api/v2/resources/product/'

***Admin/store attendant can get all products***'/api/v2/resources/products/all'

***Admin/store attendant can get a specific product***'/api/v2/resources/products/<pk>/'

***Store attendant can add a sale order***'/api/v2/resources/sale/'

***Admin/store attendant can get all sale order records***'/api/v2/resources/sales/all'

***Admin can update the product***'/api/v2/resources/product/<int:product_id>'

***Admin can delete the product***'/api/v2/resources/product/<int:product_id>'


#RUNNING TESTS

Run ```pytest``` in the commandline

Do ```pip install pytest``` to install it

#DEPLOYMENT

This app is deployed on heroku, how to get started on deploying on heroku

```-install Heroku CLI 
-pip install gunicorn
-Create a file in the root directory
-commit and push changes
-Go a head to heroku sign up 
-connect the repo to heroku
-In the terminal type heroku login to login to your account.
-Go to heroku,  on the dashboard,choose the branch and deploy
-And go to view```



#AUTHOR
NAMAARA RACHEAL
