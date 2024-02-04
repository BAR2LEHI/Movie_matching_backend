from main import *


test_user = {
    'movies': [86320],
    'score': [5]
}

recommender = Recommender()
recommendations = recommender.model_recommendations(
                                                test_user['movies'], #id просмотренных фильмов
                                                test_user['score'], #оценки фильмов
                                                N=10 
                                                )
print(recommendations) #id рекоммендаций


# вот так, если передаёшь imdb id:
test_user = {
    'movies': [86320],
    'score': [5]
}

imdb_map = load_imdb_map()
recommendations = recommender.model_recommendations(
                                                imdb_map.from_imdb(test_user['movies']), #imdb id просмотренных фильмов
                                                test_user['score'], #оценки фильмов
                                                N=10 
                                                )

print(imdb_map.to_imdb(recommendations))


    