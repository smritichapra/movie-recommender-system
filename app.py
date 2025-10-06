import pickle
import streamlit as st

# Load saved movie list and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movie_names

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Gradient background & heading style
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #8e2de2, #4a00e0, #00f0ff, #ff00ff);
        background-size: 400% 400%;
        animation: gradientAnimation 20s ease infinite;
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    @keyframes gradientAnimation {
        0% {background-position:0% 50%}
        50% {background-position:100% 50%}
        100% {background-position:0% 50%}
    }
    h1 {
        text-align: center;
        font-size: 3em;
        font-weight: 900;
        background: linear-gradient(90deg, #ff4b4b, #ff9f1c, #2ec4b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .intro {
        text-align: center;
        background-color: rgba(31, 31, 31, 0.7);
        padding: 15px;
        border-radius: 12px;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .movie-card {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 16px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
    }
    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 255, 255, 0.3);
    }
    </style>
    <h1>🎬 Movie Recommender System</h1>
    <p class="intro">Discover your next favorite movie!</p>
    """, unsafe_allow_html=True
)

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

    st.markdown("<h3 style='color:#ffbd59;'>Top 5 Recommended Movies:</h3>", unsafe_allow_html=True)

    # Display movies in columns with gradient cards
    cols = st.columns(5)
    gradient_colors = [
        "linear-gradient(135deg, #ff4b4b, #ff758c)",
        "linear-gradient(135deg, #ff9f1c, #ffcc33)",
        "linear-gradient(135deg, #2ec4b6, #00f0ff)",
        "linear-gradient(135deg, #e71d36, #ff4b4b)",
        "linear-gradient(135deg, #011627, #2ec4b6)"
    ]

    for col, movie_name, gradient in zip(cols, recommended_movie_names, gradient_colors):
        col.markdown(
            f"""
            <div class="movie-card" style="background: {gradient};">
                {movie_name}
            </div>
            """,
            unsafe_allow_html=True
        )
