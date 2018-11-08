# INLG hackathon chatbot service template



## Getting Started

These instructions will get you a python service that can be used to host your NLG solution which can communicate with the Flow.ai platform.

### Prerequisites

* Python with virtual environment installed
* Flow.ai account


### Installing service

Get this repo

```
$ git clone https://github.com/flow-ai/hackathon
$ cd hackathon
```

Create and activate virtual environment

```
$ virtualenv service_env
$ source service_env/bin/activate
```

Install the required modules
```
$ pip install -r requirements.txt
```


### Start API service
```
$ python app.py
```

Open a new window and cd to the directory of your project, then use ngrok to tunnel your local service to the web:

```
$ ./ngrok http 5000
```
* Import the json file into Flow.ai (project settings > backup)
* In the actions editor replace the ngrok url with your own and save.

