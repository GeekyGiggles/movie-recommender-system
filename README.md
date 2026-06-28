# Movie Recommender System

A content-based movie recommendation system built using Python, Pandas, Scikit-Learn and Streamlit.

The system recommends movies similar to a selected movie using:

* NLP preprocessing
* Bag of Words
* Count Vectorization
* Cosine Similarity

## Features

* Select a movie from a dropdown menu
* Get top 5 similar movie recommendations
* Built with Streamlit for an interactive web interface

---

## Dataset

This project uses the TMDB 5000 Movies Dataset.

Download:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Required files:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

---

## Project Structure

```text
Movie-Recommender/
│
├── app.py
├── movie_recommender.ipynb
├── movies_dict_final.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
│
├── content/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Movie-Recommender
```

Create a virtual environment (optional):

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Streamlit App

From the project directory:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Regenerating the Pickle Files

If you wish to recreate the recommendation model:

1. Download the dataset from Kaggle.
2. Place both CSV files inside the `content` folder.
3. Open `movie_recommender.ipynb`.
4. Run all notebook cells.
5. The notebook will generate:

```text
movies_dict_final.pkl
similarity.pkl
```

These files are used by the Streamlit application.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Streamlit

---

## Recommendation Method

The recommendation engine uses:

1. Data preprocessing
2. Feature extraction from:

   * genres
   * keywords
   * cast
   * crew
   * overview
3. CountVectorizer
4. Cosine Similarity

Movies with the highest cosine similarity scores are recommended.


<!-- test -->