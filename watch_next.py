import spacy
nlp = spacy.load('en_core_web_md')

def find_watch_next(description, movies):
    description = description.lower()
    doc = nlp(description)

    # removing punctuation from the description
    description = [token.text for token in doc if not token.is_stop and not token.is_punct]

    # creating an empty list to store there all the similarities
    similarities = []
    for movie in movies:
        movie = movie.lower()
        movie_doc = nlp(movie)
        # removing punctuation from each movie description in the list
        movie = [token.text for token in movie_doc if not token.is_stop and not token.is_punct]

        # doing the similarity comparisons
        similarity = doc.similarity(nlp(" ".join(movie)))
        similarities.append(similarity)

    # finding the index of the movie that has the highest score in similarity
    index = similarities.index(max(similarities))
    return movies[index]

# reading the text file 'movies.txt'
with open("movies.txt", "r") as f:
    movies = f.readlines()

# removing newline symbols from each movie
movies = [movie.strip() for movie in movies]

# employing the Planet Hulk description
description = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
watch_next = find_watch_next(description, movies)
print(f"""Here is what you should watch next: 

{watch_next}""")
