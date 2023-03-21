# Lesson 2a

## (IMPORTANT!) Create a virtual environment

A virtual environment allows you to install third-party Python dependencies in a way that doesn't interfere with your global environment.

```sh
python3 -m venv env
source env/bin/activate
```

Once you run this, the `python` and `pip` commands in your shell will use this local environment.

## Usage

This program retrieves the types of a given pokemon and displays it to the user. It takes a command line argument string that is passed to the PokeAPI. This accepts a number representing a pokemon's index in the Pokedex, or the name of a pokemon like so:

```sh
python3 main.py pikachu
python3 main.py 5
```
