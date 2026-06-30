import streamlit as st
import pandas as pd
import pickle
import requests

# Page Title
st.title("Movie Recommender System")


# Load Data
movies_dict = pickle.load(open("movies_dict_final.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


# OMDb API
API_KEY = "1090ea1d"
@st.cache_data
def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True" and data.get("Poster") != "N/A":
            return data["Poster"]

    except:
        pass

    return None



# Recommendation Function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:

        title = movies.iloc[i[0]].title

        recommended_movies.append(title)

        recommended_posters.append(fetch_poster(title))

    return recommended_movies, recommended_posters


# UI
selected_movie = st.selectbox(
    "Which movie do you want similar to?",
    movies["title"].values
)

if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):

        with cols[i]:

            if posters[i]:
                st.image(posters[i], use_container_width=True)
            else:
                st.write("Poster not found")

            st.caption(names[i])

