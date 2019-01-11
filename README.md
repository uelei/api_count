#API Count

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c6b88fb1c31946fc89c5a8c460d90670)](https://www.codacy.com/app/uelei/api_count?utm_source=github.com&utm_medium=referral&utm_content=uelei/api_count&utm_campaign=badger)

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