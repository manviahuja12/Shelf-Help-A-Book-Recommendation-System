<h1 align="center"> Shelf-Help-A-Book-Recommendation-System </h1>

<p align="center">
  <img src="Website_Files/static/banner.jpg" width="300px" height="250px">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

Shelf Help is a book recommendation system that suggests books based on user input, leveraging both collaborative filtering and popularity-based recommendations. By analyzing similarities between books and considering their popularity, it provides personalized and widely favored suggestions from a dataset.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2>:scroll: Objective </h2>

The main objective is to create a book recommendation system for users. Recommender systems are really critical in some industries as they can generate a huge
amount of income when they are efficient or also be a way to stand out significantly from competitors. 

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

### Methods Used
* Descriptive Statistics
* Machine Learning
* Web Development

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :floppy_disk: Data </h2>

The Book-Crossing dataset comprises 3 files (Click [here](https://drive.google.com/drive/folders/184irGJPi73xYu_eMgI3JBCc-okIOTUIF?usp=sharing) to access the Data)

* Users : 
Contains the users. Note that user IDs (User-ID) have been anonymized and map to
integers. Demographic data is provided (Location, Age) if available. Otherwise, these
fields contain NULL values.

* Books : 
Books are identified by their respective ISBN. Invalid ISBNs have already been removed
from the dataset. Moreover, some content-based information is given (Book-Title,
Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web
Services. Note that in the case of several authors, only the first is provided. URLs linking
to cover images are also given, appearing in three different flavors (Image-URL-S,
Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the
Amazon website.

* Ratings :
Contains the book rating information. Ratings (Book-Rating) are either explicit,
expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit,
expressed by 0.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :clipboard: Project Description </h2>

* Importing Libraries: Loaded essential Python libraries like flask, numpy and pandas for data manipulation, building the recommender system, and web development.

* Loading the Dataset: Loaded the book rating dataset (books.pkl) and performed initial data checks to ensure the data was clean and suitable for modeling.

* Preliminary Analysis: Conducted a brief analysis to understand the dataset, including checking distributions, identifying missing values, and summarizing key statistics.

* Building Recommender System:
      - Popularity Based: Developed a recommender system based on book popularity, suggesting the most highly rated books to users.
      - Collaborative Filtering Based: Built a collaborative filtering-based model that recommends books to users based on the preferences of similar users.
  
* Exporting Data through Pickle: Saved the trained recommender model and other necessary data into .pkl files for easy loading and use on the web application.

* Created a Website: Designed a simple web application using Flask to present the recommender system, allowing users to get book recommendations based on either popularity or collaborative filtering.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :book: Popularity Based Recommender </h2>

It is a type of recommendation system which works on the principle of popularity and or anything
which is in trend. These systems check about the books which are in trend or are most popular
among the users and directly recommend them.

<h2> :book: Collaborative-based Filtering </h2>

Collaborative based filtering recommender systems are based on past interactions of users and
target items. In simple words here, we try to search for the look-alike customers and offer products
based on what his or her lookalike has chosen. Let us understand with an example. X and Y are
two similar users and X user has watched A, B, and C movie. And Y user has watched B, C, and D
movie then we will recommend A movie to Y user and D movie to X user.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :clipboard: Future Scope </h2>

Given more information regarding the books dataset, namely features like Genre, Description etc., we could implement a content-filtering based recommendation system and compare the results with the existing collaborative-filtering based system.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h2> :clipboard: Summary </h2>

Shelf Help is a book recommendation system that suggests books using popularity-based and collaborative filtering methods. It leverages a dataset with user ratings, book details, and demographics. The system was built using Python libraries like Flask, NumPy, and scikit-learn.

It offers two types of recommendations:

Popularity-Based: Recommends popular books.
Collaborative Filtering: Recommends books based on similar users’ preferences.
