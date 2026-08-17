import pickle as p
import streamlit as st
from rapidfuzz import process, fuzz

# Loading ml
moviesList = p.load(open('movies.pkl', 'rb'))
vector = p.load(open('vector.pkl', 'rb'))
knn = p.load(open('knn.pkl', 'rb'))

# movieTitle = moviesList['title'].dropna().tolist() #chance of movie loss due to unique function

movieTitle = (moviesList['title'].fillna('') + " (" +moviesList['year'].fillna('').astype(str) + ")").tolist()

def fetchPoster(id):
    posters = moviesList[moviesList['id'] == id]

    if len(posters) > 0:
        return posters.iloc[0]['poster_url']

    return None


def recommendation(ind):
    # ind = moviesList[moviesList['title'].str.lower() == movie.lower()].index[0]

    dist, indices = knn.kneighbors(vector[ind])

    recomm_movies = []
    recomm_poster = []

    for i in indices[0][1:6]:
        id = moviesList.iloc[i]['id']
        name = moviesList.iloc[i]['title']
        year = moviesList.iloc[i]['year']

        posters = fetchPoster(id)
        recomm_movies.append(name + " (" + str(year) + ")")
        recomm_poster.append(posters)

    return recomm_movies, recomm_poster


st.title("MovieMate", text_alignment="center")
st.subheader("Find your next favourite movie", text_alignment="center")
# selected_movie = st.selectbox("Type or Select a movie", moviesList)

with st.form("movie_search"):
    movieInput = st.text_input(
        "Type a movie name",
        placeholder="Search for a movie..."
    )
    submitted = st.form_submit_button("Search")

if submitted and movieInput:
    matches = process.extract(movieInput.lower(), [movie.lower() for movie in movieTitle], scorer = fuzz.WRatio, limit = 15, score_cutoff = 50)

    if matches:
        matchedMovies = []
        for match in matches:
            ind = match[2]
            matchedMovies.append(ind)
        st.session_state["matchedMovies"] = matchedMovies
    else:
        st.session_state["matchedMovies"] = []


if "matchedMovies" in st.session_state:
    if st.session_state["matchedMovies"]:
        selectedMovies = st.selectbox("Select Movie", st.session_state["matchedMovies"], format_func=lambda x: movieTitle[x])
        if st.button("Show Recommendation"):
            names, posterUrl = recommendation(selectedMovies)
            st.subheader("Movie Recommendation", text_alignment="center")

            columns = st.columns(5)

            for col, name, poster in zip(columns, names, posterUrl):
                with col:
                    if poster:
                        st.image(poster, caption=name, use_container_width=True)
                    else:
                        st.write("Poster Unavailable")
                    # st.write(name)
    else:
        st.warning("Movie Not Found")


