# Lesson 2a

## (IMPORTANT!) Create a virtual environment

A virtual environment allows you to install third-party Python dependencies in a way that doesn't interfere with your global environment.

```sh
python3 -m venv env
source env/bin/activate
```

Once you run this, the `python` and `pip` commands in your shell will use this local environment.

## Install

Since this project uses dependencies outside of the Python standard library, we'll need to import them before we can run the code.

```sh
source env/bin/activate
pip install -r requirements.txt
```

> It's a common convention to put your project's dependency in a `requirements.txt` file, and `pip install` them using the `-r` flag to use a file. Otherwise, you can install individual dependencies without a file like `pip install requests`.

## Usage

This program generates a CSV called `pokemon.csv` containing the name and first type of the original 150 pokemon.

```sh
python3 main.py
```
