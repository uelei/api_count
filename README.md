#API Count

Api to count words from a given url


## Setup

the code was writing using python3, and all requirements is on requirements.txt

```bash
virtualenv --python=/usr/local/bin/python3 env

source env/bin/activate

pip install -r requirements.txt
```

## Runing Server

```bash
bash run.sh
```
## Usage

arguments

* word
* url
* ignore_case (optional) find all words ignoring case

```bash
curl --request GET \
  --url 'http://127.0.0.1:8000/?word=president&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDonald_Trump'

```

## Runing tests

```bash
pytest test
```