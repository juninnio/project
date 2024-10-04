Meal Recommender Project WebApp with Machine Learning, Flask, Jinja, HTML, CSS, and JavaScript (Ongoing Project).
------------------------------------------------------------------------------------------------------------------------------------
Machine Learning used: Item-item Collaborative Filtering (Cosine Similarity) & User-Item Coollaborative Filtering (SVD).<br>
Project goal is to recommend meal to users by using hybrid approach with cosine similarity and SVD.
<br><br>
Files Link: [https://drive.google.com/drive/folders/1hwElfg1APxlig3Npo1PSw3H9gzNwzFEh?usp=sharing](url)
<br>
code.ipynb are used to preprocess the datasets in parent folder (Meal Recommender).
<br>
The preprocessed datasets are saved in ml folder inside website folder along with ml pipeline script and sql script to create and insert data into database.
<br><br>
The workflow of the application:
1. User will be promopted to login/sign up to obtain user id.
2. After logging in, user will be asked to choose from a set of options, minimal 5 choices.
3. The choices and user id will then be appended into preprocessed dataset (user_rating.csv inside ml folder) to be trained with svd.
4. The choices are then fed into cosine similarity function to get similar recipes
5. After some filtering, a list of recipe_id will be passed back to backend
6. With the recipe_id, backend will query the database.

<br><br>
The preprocessing steps for the dataset:<br>
1. The recipe dataset contains a lot of column but the ones used for preprocessing were: ingredients, reviews, and nutritions
  - The ingredients column is one-hot encoded and reduced using Truncated SVD.
  - The reviews column is used to extract user reviews and append it into existing user review dataset (user_recipe.csv)
  - Nutritions column is One-Hot Encoded and scaled
2. User recipe dataset has added rows from recipe dataset and the user ids are rescaled to prevent unused ids.
