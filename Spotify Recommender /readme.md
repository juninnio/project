Spotify Song Recommender System
--------------------------------
This project creates a content-based song recommendation system using Spotify data and MongoDB for database storage, with PySpark for data preprocessing and recommendation logic. The system retrieves songs from a Spotify playlist, processes artist and genre information, encodes features for similarity analysis, and provides song recommendations based on cosine similarity.

Features
----------------------------
- Spotify Integration: Connects to Spotify API to retrieve and process playlists and song details.
- MongoDB Database: Stores song metadata, artist details, and song features in a MongoDB database.
- Data Processing with PySpark: Prepares and encodes artist and genre data, normalizes song duration, and structures the data for recommendation.
- Recommendation Model: Utilizes cosine similarity to recommend songs based on content features.

Technologies Used
-------------------
- Python and Jupyter Notebooks
- MongoDB with PyMongo for database operations
- Spotify API with Spotipy for retrieving playlists and song details
- PySpark for scalable data preprocessing and analysis
- Pandas and NumPy for data handling and similarity calculations