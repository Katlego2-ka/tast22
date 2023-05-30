import spacy
from spacy import displacy
from spacy.matcher import PhraseMatcher

# Loading the English language model
nlp = spacy.load("en_core_web_sm")

def find_similar_movie(description):
    # Reading  the movies from the text file
    with open("movies.txt", "r") as file:
        movies = file.readlines()

    # Processing  the description and movies using the language model
    doc_desc = nlp(description)
    processed_movies = [nlp(movie) for movie in movies]

    
    matcher = PhraseMatcher(nlp.vocab)
    matcher.add("MOVIE", None, *processed_movies)


    matches = matcher(doc_desc)
    
    # Calculating  the similarity scores and get the most similar movie
    similarity_scores = []
    for match_id, start, end in matches:
        span = doc_desc[start:end]
        similarity_scores.append((span.text, span.similarity(doc_desc)))
    
    # Sorting the similarity scores in descending order
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Returning the title of the most similar movie
    return similarity_scores[0][0] if similarity_scores else None


description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
most_similar_movie = find_similar_movie(description)
print("Next movie to watch:", most_similar_movie)
