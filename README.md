# 🎬 MovieMate - Movie Recommendation System

MovieMate is a machine learning based movie recommendation website that recommends movies similar to the movie selected by the user.

The project uses **content-based filtering** with **TF-IDF vectorization** and **K-Nearest Neighbors (KNN)** to find movies with similar characteristics.

Users can search for movies using different capitalization or minor spelling mistakes.

---

## 🚀 Features

- 🔍 Search movies by title
- 🔤 Case-insensitive movie search
- ✏️ Typo-tolerant search using RapidFuzz
- 🎯 Multiple matching movie suggestions
- 📅 Displays movie release year
- 🤖 Content-based movie recommendations
- 🧠 KNN-based similarity search
- 📊 TF-IDF text vectorization
- 🎬 Movie posters for recommendations
- 🖥️ Interactive Streamlit web interface
- ⚡ Pre-trained ML model using `.pkl` files

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation |
| Scikit-learn | Machine learning |
| TF-IDF | Text vectorization |
| KNN | Finding similar movies |
| RapidFuzz | Fuzzy movie title search |
| Streamlit | Web application |
| Pickle | Saving and loading ML models |

---

## 🧠 How It Works

MovieMate uses a **content-based recommendation system**.

### 📊 Movie Dataset

Movie information such as:

- Movie ID
- Movie title
- Movie overview
- Genres
- Keywords
- Director
- Cast
- Release year

is combined into a `tags` column.

### ⚡ Machine Learning Approach
```text
Movie Dataset
      ↓
Data Cleaning
      ↓
Create Tags
      ↓
TF-IDF Vectorization
      ↓
Movie Vectors
      ↓
K-Nearest Neighbors
      ↓
Cosine Distance
      ↓
Similar Movies
      ↓
Movie Posters
```
## 📁 Project Structure

```text
MovieMate/
│
├── main.py              # Streamlit application
│
├── movies.pkl           # Processed movie dataset
├── vector.pkl           # TF-IDF movie vectors
├── knn.pkl              # Trained KNN model
├── poster.pkl           # Movie poster data
│
├── .gitignore           # Files excluded from Git
└── README.md            # Project documentation
```
## ⚙️ Installation

```bash
git clone https://github.com/your-username/MovieMate.git
```
```bash
cd MovieMate
```
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```
```bash
source .venv/bin/activate
```
```bash
pip install streamlit pandas scikit-learn scipy rapidfuzz
```
```bash
streamlit run main.py
```
```bash
http://localhost:8501
