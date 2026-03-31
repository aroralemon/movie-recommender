# Movie Recommendation System

## Project Overview
This project is a Movie Recommendation System that suggests similar movies based on a given movie title. It uses a content-based filtering approach and basic machine learning techniques to generate recommendations.

The system analyzes movie genres and recommends movies that are most similar to the selected input movie.

---

## Objective
The objective of this project is to demonstrate the application of machine learning concepts in building a simple recommendation system.

---

## Technologies Used
- Python  
- Pandas  
- Scikit-learn  

---

## Machine Learning Concepts Used
- Content-Based Filtering  
- One-Hot Encoding  
- Cosine Similarity  

---

## Project Structure
```
movie-recommender/
│── main.py  
│── movies.csv  
│── README.md  
│── requirements.txt  
```

---

## Dataset
The dataset used in this project is a small custom dataset containing movie titles and their corresponding genres.

Example:

```
title,genre
Batman Begins,Action
Inception,Sci-Fi
Titanic,Romance
```

---

## How to Run the Project

### Step 1: Clone the Repository
```
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### Step 2: Install Dependencies
```
pip install -r requirements.txt
```

### Step 3: Run the Program
```
python main.py
```

---

## Usage
1. Run the program  
2. Enter a movie name from the dataset  
3. The system will display recommended movies  

---

## Features
- Simple and easy to use  
- Fast recommendations  
- Uses basic machine learning techniques  
- Lightweight implementation  

---

## Troubleshooting

### 1. Module Not Found Error
If you see errors like:
```
ModuleNotFoundError: No module named 'pandas'
```
Run:
```
pip install pandas scikit-learn
```

---

### 2. File Not Found Error
If you see:
```
FileNotFoundError: movies.csv not found
```
Make sure:
- `movies.csv` is in the same folder as `main.py`
- File name is correct (case-sensitive)

---

### 3. Movie Not Found
If the program prints:
```
Movie not found!
```
- Enter a movie exactly as in the dataset  
- Example: `Batman Begins`  

---

### 4. Python Command Not Working
Try:
```
python3 main.py
```

---

## Limitations
- Uses a small dataset  
- Recommendations are based only on genre  
- Does not consider user preferences  

---

## Future Improvements
- Use a larger dataset  
- Incorporate user ratings  
- Improve recommendation accuracy  
- Add a graphical or web-based interface  

---

## Credits
- **Student:** Shreya Arora
- **Registration:** 25bce10621
- **Institution:** Vellore Institute of Technology, Bhopal
- **Course:** Fundamentals of AI & ML
- **Date:** March 2026

---

## Conclusion
This project demonstrates how machine learning techniques such as cosine similarity can be applied to build a basic recommendation system. It serves as a foundation for developing more advanced recommender systems.

---

## License
This project is developed for academic purposes only.
