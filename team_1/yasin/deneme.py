import json
movie_liste = {
    'The Lord of The Rings - The Fellowship of the Rings': {
        'Movie Year': 2001,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'The Lord of The Rings - The Two Towers': {
        'Movie Year': 2002,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'The Lord of The Rings - The Return of the King': {
        'Movie Year': 2003,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'Kingdom of Heaven': {
        'Movie Year': 2005,
        'Director': 'Ridley Scott',
        'Movie Genre': 'Action-History-War'
    },
    'The Green Mile': {
        'Movie Year': 1999,
        'Director': 'Frank Darabont',
        'Movie Genre': 'Drama-Fantasy'
    },
    'Saving Private Ryan': {
        'Movie Year': 1998,
        'Director': 'Steven Spielberg',
        'Movie Genre': 'History-War'
    },
    'Harry Potter and the Prisoner of Azkaban': {
        'Movie Year': 2004,
        'Director': 'Alfonso Cuaron',
        'Movie Genre': 'Fantasy-Adventure'
    },
    'The Curious Case of Benjamin Button': {
        'Movie Year': 2008,
        'Director': 'David Fincher',
        'Movie Genre': 'Drama'
    },
    'Pearl Harbor': {
        'Movie Year': 2001,
        'Director': 'Michael Bay',
        'Movie Genre': 'War-Drama'
    }
}
with open("movies.json", "w") as file:
    json.dump(movie_liste, file, indent=4)
