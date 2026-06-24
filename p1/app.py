
import streamlit as st
import pandas as pd
import pickle#pcikle saves pyhton obj to file
#hum as it is pandas ka df pickle karke yaha use nhi kar sakte
# to df ko dict banado vo to har jagah accesible

st.title("Movie Recommender System")

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended=[]
    for i in movie_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

movies_dict = pickle.load(open("movies_dict_final.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open("similarity.pkl","rb"))

selected_movie = st.selectbox(
    "Which movie do you want similar to?",
    movies["title"].values
)

if st.button("Recommend"):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)

        # coded
        
    