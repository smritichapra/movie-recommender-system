🎬 Content-Based Movie Recommender System:
A Content-Based Movie Recommender System built using Python, scikit-learn, and Streamlit.This application recommends movies similar to a selected title by analyzing movie content features like genres, keywords, cast, and descriptions.The system leverages Cosine Similarity and K-Nearest Neighbors (KNN) algorithms to compute similarity scores between movies and deliver personalized recommendations.

🚀 Features:
🎯 Content-Based Filtering — Recommends movies based on feature similarity (genres, cast, overview, etc.)
💡 Cosine Similarity & KNN — Measures closeness between movies using NLP and vectorization techniques
🧠 Data Preprocessing — Cleaned and vectorized movie metadata for efficient model performance
🌐 Streamlit Web App — Interactive, user-friendly web interface for real-time recommendations
💾 Model Persistence — Pickle used for saving/loading preprocessed data and trained models

📊 Dataset:
Source: TMDb Movie Metadata Dataset

🛠️ Tech Stack & Libraries:
Programming Language: Python 3.x
Libraries Used:
pandas → Data cleaning & manipulation
numpy → Numerical computations
scikit-learn → Cosine similarity, KNN, feature vectorization
streamlit → Web application framework
pickle → Model serialization and deserialization

⚙️ How It Works:
Data Preprocessing->Clean and combine relevant columns (genres, keywords, cast, overview) into a single textual feature.
Feature Extraction->Use TF-IDF Vectorization or CountVectorizer to transform movie metadata into numerical vectors.
Similarity Computation->Compute Cosine Similarity or KNN distance matrix between movie vectors.
Recommendation Generation->Retrieve top 5 movies with the highest similarity scores to the selected movie.
Streamlit Interface->Display recommendations interactively through a clean and responsive UI.

💻 Installation & Setup:
1️⃣ Clone the Repository
git clone https://github.com/yourusername/content-based-movie-recommender.git
cd content-based-movie-recommender

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

🧩 Project Structure:
├── app.py                   # Streamlit main application
├── movie_recommender.ipynb  # Jupyter notebook for model training
├── movies.csv               # TMDb movie dataset
├── similarity.pkl           # Precomputed similarity matrix
├── movies_dict.pkl          # Serialized movie metadata
├── requirements.txt         # Required Python packages
└── README.md                # Project documentation

🎥 Demo:

