## Guide for HORIZONT developers ![alt text](https://github.com/EugeneArt/interactive_map/blob/dev/client/src/img/RD.png "Logo Title Text 1")

## About

Interactive map for sanatorium "Sputnik"

## Installing
### Client
__Open folder client and make instructions:__
* install all required packages;
```javascript
  npm install
```
* run dev server;
```javascript
  gulp serve
```
* build for  production(use only for production);
```javascript
  gulp default
```
#### Options
__Path to API in client, floor id and duration advertisement you can find:__ client/src/config.locale.js


### Server
__Open root folder and make instructions:__
*  __activate virtual environment__

    in interactive_map folder enter this code:
    ```python
      source venv/bin/activate
    ```
    then you should see (venv) in console

* __install all requirements__

    change directory to interactive_map, write follow commands in console:
    ```python
      pip install -r requirements.txt
    ```
* __change directory to imap and write follow commands, where IP: your computer IP and port(for example 8000)__:
    ```python
      python manage.py runserver IP:PORT
    ```

#### Options
__Path to change db options and others you can find:__ imap/imap/settings.py

## Production

__Structure folder:__

imap

__ __client__

____dist

______index.html

______package.json

__ __server__

____api

____imap

____info

____manage.py

__ __media__

__requirements.txt


__Environment:__

* __Client(Angularjs):__ Apache(WAMP)
* __Server(Django):__ Dev server
* __DB(MySQL):__ MySQL


### Authors
__*Eugene Artsiukhevich*__
