import spacy

nlp = spacy.load("en_core_web_md")

# The movie that will be used to compare with other movies
last_watched_movie = "Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for the"\
                     "Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a" \
                     "planet where the Hulk can live in peace. Unfortunately, Hulk land on the" \
                     "planet Skaar where he is sold into slavery and trained as a gladiator."

nlp_last_watched_movie = nlp(last_watched_movie)

# Stores the information of other movies
movies = []
movie_names = []
similarity_score =[]

# Reads the lines of movie.txt and appends the relevant information to the relevant lists.
with open("movies.txt", "r") as movies_file:
    for line in movies_file:
        new_line = line.replace(":", "").replace("\n", "").split(" ")
        movies.append(" ".join(new_line[2:]))
        movie_names.append(" ".join(new_line[0:2]))


with open("movies.txt", "r") as movies_file:
    for sentence in movies:
        similarities = nlp(sentence).similarity(nlp_last_watched_movie)
        similarity_score.append(similarities)


best_match = similarity_score.index(max(similarity_score))

print(f"Since you watched {last_watched_movie[0:11]}, we think you would love to watch {movie_names[best_match]}.")


