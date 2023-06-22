
# Movie Recommendation System

This is a simple movie recommendation system that uses natural language processing (NLP) techniques to find the most similar movie based on a given movie description.

## Overview

The movie recommendation system takes a movie description as input and compares it with a collection of movies to find the most similar one. It utilises the spaCy library for tokenization and semantic similarity calculations.

## Requirements

- Python 3.11
- spaCy library (version 1.0.1)
- en_core_web_sm language model for spaCy (v1.0.1)
- Movie data file

## Installation

1. Install Python 3.11 from the official Python website: https://www.python.org/downloads/

2. Install the spaCy library by running the following command:
pip install spacy 

3. Download the en_core_web_sm language model by running the following command:

python -m spacy download
en_core_web_sm

4. Place your movie data file in the same directory as the Python script.

## Usage

1. Open the Python script in a text editor.

2. Modify the `file_path` variable in the script to specify the path to your movie data file.

3. Run the Python script using the following command:
watch_next.py


4. Enter a movie description when prompted.

5. The system will find the most similar movie based on the description and display the result.

## File Structure

- `watch_next.py`: The main Python script that implements the movie recommendation system.
- `movie_data.txt`: A text file containing the movie data. Each line should contain a movie description.



