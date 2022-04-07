# How to Configure development settings

* Create a file ``` dev_settings.py ```
* Add ``` SECRET_KEY ```, ``` DATABASES ```, ``` ALLOWED_HOSTS ```, ``` MEDIA_ROOT ```
* development settings will look somethings like this,
```
SECRET_KEY = 'secretkeyhere'

DATABASES = {
    "default": {
        "ENGINE": "",
        "NAME": "",
        "USER": "",
        "PASSWORD":"",
        "HOST":"",
        "PORT": ""
    }
}


ALLOWED_HOSTS = ['localhost']

MEDIA_ROOT = '/media/`

```