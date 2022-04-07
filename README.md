# TakeHome Assignment - Imager

This is a simple django backend which helps the users to upload images with specific name and description and fetch them

## Prerequiesties

* Python version 3.7+ downloaded from [here](https://python.org)
* Pip packages in ``` requirements.txt ```
* IDE, for example VSCode (optional)
* POSTMAN to test API Endpoints (optional)

## How to Configure for Local Machine

* Download latest python from [here](https://python.org)
* Install pip packages using the command

``` pip install -r requirements.txt ```

* Configure development settings as mentioned in ``` takehome/README.md ```
* Make migrations using the command

``` 
python3 manage.py makemigrations
python3 manage.py migrate
```
* Set ```DEBUG = False ``` in ```settings.py ```
* Start server ``` python3 manage.py runserver ```


# API Endpoints

## login/

Obtain the authentication token by POST request to ``` login/ ```

## Request format

### header
``` 
{
    "content-type" : "application/json"
} 
```

### body

```
{
    "username" : "add_username_here",
    "password" : "add_password_here"
}

```
### Response

The response format is

```
{
    "token" : "token_here"
    "user_id" : "user_id_here"
}
```

## add/

To add image, name and description POST request to ```add/```

## Request format

### header
``` 
{
    "content-type" : "application/json"
    "authorization" : "Token {add_token_here}"
} 
```

### body

```
{
    "name" : "add_name_here",
    "desciption" : "add_description_here",
    "image":"upload_image_here"
}

```
### Response

The response format is

```
{
    "id":"id_of_upload"
}
```

To fetch all images send GET request to ``` add/ ```

### header
``` 
{
    "content-type" : "application/json"
    "authorization" : "Token {add_token_here}"
} 
```

### Response

The response format will be set of these format

```
{
    "name" : "name_here",
    "desciption" : "description_here",
    "image":"image_url_here",
    "date" : "date_here",
    "time" : "time_here
}
```

### Note : The response is paginated, header contains the link to previous and next page


## add/<id_here>/


To fetch a specific image, send GET request to ``` add/<id_here>/ ```

### header
``` 
{
    "content-type" : "application/json"
    "authorization" : "Token {add_token_here}"
} 
```

### Response

The response format will be set of these format

```
{
    "name" : "name_here",
    "desciption" : "description_here",
    "image":"image_url_here",
    "date" : "date_here",
    "time" : "time_here
}
```