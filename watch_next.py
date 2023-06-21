# This program is a function that recommends which movie to watch next by
# comparing similarities between a given movie name and description
# To a list of other movies with their description. The function must return
# The title of the most similar movie's description.

import spacy

# Loading my language model
nlp = spacy.load("en_core_web_md") 

# Defining my function
def watch_next (description): 

  movies  = "movies.txt"
# Building an empty list to store my movie list
  movie_list = []

# Reading my text file
  with open (movies,"r") as file:
    lines = file.read().splitlines()

# Tokenising the movie from my file
    for line in lines:
      doc = nlp(line)
      line_token = [token.text for token in doc]
      movie_list.append(line_token)
  
# Tokenising the description of my movie
  description = "Planet Hulk : Will he save their world or destroy it?When the Hulk becomes too dangerous to the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."     
  model_movie = nlp(description)

# Building an empty dictionnary to store the result between the model_movie and each movie
  similarity_score = { }

# Iterating to the movie list 
  for movie in movie_list:
    movie_description = " ".join(movie)
    movie_token = nlp(movie_description)

# Calculating similarity my model movie and each movie      
    similarity = model_movie.similarity(movie_token)
    similarity_score[movie_description] = similarity
  most_similar_movie = max(similarity_score, key= similarity_score.get)
            
  return most_similar_movie      

description = "Planet Hulk :Will he save their world or destroy it?When the Hulk becomes too dangerous to the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
most_similar_movie = watch_next(description)
print(most_similar_movie)
     


 

      
