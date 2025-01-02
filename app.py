import streamlit as st
import pickle

movie_df = pickle.load(open('movies.pkl', 'rb'))
movies = movie_df['title'].values

similarity_metrics = pickle.load(open('similarity_metrics.pkl', 'rb'))

def recomend(movie):
    movie_index = movie_df[movie_df['title'] == movie].index[0]
    similarity_value = similarity_metrics[movie_index]
    
    # for preserving index we need to do enumerete and convert it into list
    index_list_movies = sorted(list(enumerate(similarity_value)), reverse=True, key=lambda x:x[1])[1:6]
    movie_names = []
    for i in index_list_movies:
        movie_names.append(movie_df.iloc[i[0]]['title'])
    return movie_names

st.title('MOVIE RECOMENDATION SERVICE')
selected_movie = st.selectbox('Select Movie', movies)


if st.button('RECOMEND'):
    for i in recomend(selected_movie):
        st.write(i)