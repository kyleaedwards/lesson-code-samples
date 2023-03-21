# Lesson 2a

## (IMPORTANT!) Create a virtual environment

A virtual environment allows you to install third-party Python dependencies in a way that doesn't interfere with your global environment.

```sh
python3 -m venv env
source env/bin/activate
```

Once you run this, the `python` and `pip` commands in your shell will use this local environment.

## Usage

This program generates a CSV called `pokemon.csv` containing the name and first type of the original 150 pokemon.

```sh
python3 main.py
```
