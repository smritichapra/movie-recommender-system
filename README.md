# 🎬 Content-Based Movie Recommender System

A **Content-Based Movie Recommender System** built using **Python**, **scikit-learn**, and **Streamlit**.  
This system recommends movies similar to a selected title by analyzing content features like **genres**, **keywords**, **cast**, and **description**.  

The system leverages **Cosine Similarity** and **K-Nearest Neighbors (KNN)** algorithms to compute similarity scores and deliver personalized recommendations.

---

## 🚀 Features

- 🎯 **Content-Based Filtering:** Recommends movies based on similarity of their metadata.  
- 💡 **Cosine Similarity & KNN:** Measures closeness between movies using NLP and feature vectors.  
- 🧠 **Data Preprocessing:** Cleaned and combined relevant columns for effective modeling.  
- 🌐 **Streamlit Web App:** Interactive, user-friendly web interface.  
- 💾 **Model Persistence:** Pickle used for saving/loading preprocessed data and trained models.

---

## 📊 Dataset

**Source:** [TMDb Movie Metadata Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

### Included Data Features

| Feature | Description |
|----------|-------------|
| `title` | Movie name |
| `genres` | Movie genres/categories |
| `overview` | Short description or summary |
| `keywords` | Key phrases describing the movie |
| `cast` | Lead actors/actresses |

---

## 🛠️ Tech Stack & Libraries

- **Programming Language:** Python 3.x  
- **Libraries Used:**
  - `pandas` → Data manipulation  
  - `numpy` → Numerical computations  
  - `scikit-learn` → Cosine similarity, KNN, vectorization  
  - `streamlit` → Web app interface  
  - `pickle` → Model serialization and loading

---

## ⚙️ How It Works

1. **Data Preprocessing:** Clean and merge `genres`, `keywords`, `cast`, and `overview` columns.  
2. **Feature Extraction:** Use `CountVectorizer` or `TF-IDF Vectorizer` to transform text into numerical vectors.  
3. **Similarity Computation:** Compute similarity matrix using **Cosine Similarity** or **KNN**.  
4. **Recommendation Generation:** Retrieve top N most similar movies to the selected one.  
5. **Streamlit Interface:** Interactive UI to display recommendations.

---

## 💻 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/content-based-movie-recommender.git
cd content-based-movie-recommender

