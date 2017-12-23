# flask_api_skeleton

This repository was made to store a simple template of a rest API using Flask.

## Installation.

Run the following command:

```
pip install -r requirements.txt
```

## How to run and use.

Go to the api folder and run the following command:

```
python www.py
```

Now open a new terminal to check if the api is working.

Use this command to check the *GET* method.

```
curl -i -X GET localhost:80/cats
```

Use this command to check the *PUT* method.

```
curl -H "Content-Type: application/json" -i -X PUT -d '{"name":"don gato","age":"13"}' localhost:80/cat
```