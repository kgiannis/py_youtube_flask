# py_youtube_flask
A sample project in Python using pyTube and Flask

# Installation
Use pip to install pyTube
```sh
$ pip install pytube
```

# Usage
There are eight endpoints available in order to demonstrate the usage of the **pyTube** library.

### Basic information endpoints

| Endpoint                   | Params   | Info |
|----------------------------|----------|------|
| /<movie_id>                | movie_id | aaaa |
| /**basic_info**/<movie_id> | movie_id | bbb  |
| /**streams**/<movie_id>    | movie_id | ccc  |
| /**captions**/<movie_id>   | movie_id | ddd  |
| /**audio**/<movie_id>      | movie_id | eee  |

### Stream downloading endpoints

| Endpoint                                                      | Params         | Info |
|---------------------------------------------------------------|----------------|------|
| /**download**/<movie_id>                                      | movie_id       | eee  |
| /**download**/<movie_id>/**stream_position**/<stream_position>| movie_id,      | dcdc |
|                                                               | stream_position       |
