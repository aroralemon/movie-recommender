import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder

movies = pd.read_csv("movies.csv")

enc = OneHotEncoder()
genre_data = enc.fit_transform(movies[["genre"]]).toarray()

sim_matrix = cosine_similarity(genre_data)

def get_recommendations(name):
    if name not in list(movies["title"]):
        print("Movie not found")
        return

    idx = movies[movies["title"] == name].index[0]
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores.sort(key=lambda x: x[1], reverse=True)

    print("\nYou might also like:")
    c = 0
    for i in sim_scores:
        if i[0] != idx:
            print(movies.iloc[i[0]]["title"])
            c += 1
        if c == 3:
            break

print("Movie Recommender")
user_movie = input("Enter movie name: ")
get_recommendations(user_movie)
