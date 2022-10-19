# Youtube Data Analyser

## Introduction
Youtube Data Analyzers is a project with an objective of having a finding our own data source and analysing it.

Tools that were created for this uses are:
- Giant Bomb Scrapper (For list of game names)
- Streams Charts Scrapper (For a list of Twitch streamers)

## Getting started
## __Installation__
### Juypter Notebook
```
$ pip3 install -r requirements.txt
```

### GUI (Flask)
Enter `flask` folder

#### Set Up for `Windows` 
Install modules via `VENV` (windows) 
```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```
<br />

Set Up Flask Environment
```bash
$ # CMD 
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```
<br />

Start the app
```bash
$ flask run
```

For future startups
```bash
$ .\env\Scripts\activate
$ flask run
```


#### Set Up for `Unix` / `MacOS` 
Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```
<br />

Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```
<br />

Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 
<br />

## __Usage__
### GUI (Flask)
Create a user and login.
