# Youtube Data Analyser
Youtube Data Analyzers is a project with an objective of having a finding our own data source and analysing it.

Tools that were created for this uses are:
- Giant Bomb Scrapper (For list of game names)
- Streams Charts Scrapper (For a list of Twitch streamers)

## Getting started

### Installation
#### Juypter Notebook
Installing requirements
```
$ pip3 install -r requirements.txt
```

Download the dataset from [here](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset)

Extract any one of the region dataset and save it as `Youtube_dataset.csv`

Transfer the file into the `data` folder

---

#### GUI (Flask)
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

## Usage
### GUI (Flask)
Create a user and login.

## Credits
[__Youtube Dataset__](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset) - Dataset for Youtube data

[__Atlantis Dark Flask__](https://github.com/app-generator/flask-atlantis-dark) - For flask template