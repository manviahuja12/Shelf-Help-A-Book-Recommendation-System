from flask import Flask, jsonify, render_template, request
import pickle
import numpy as np

# Load the pickle files
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),  # Used for Top 50 Books
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values),
                           carousel_books=list(pt.index[:15]),  # Renamed for Carousel Books
                           carousel_images=[books.loc[books['Book-Title'] == title, 'Image-URL-M'].values[0] for title in pt.index[:15]],
                           carousel_authors=[books.loc[books['Book-Title'] == title, 'Book-Author'].values[0] for title in pt.index[:15]]
                           )

@app.route('/top_books')
def top_books():
    return render_template('top_books.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values))  # Create this file in templates

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

   # Check if user input is empty
    if not user_input:
        error_message = "Please enter a book name."
        error_type = "empty"
        return render_template('recommend.html', error_message=error_message, error_type=error_type)

    # Check if the book exists in the index (pt.index)
    if user_input not in pt.index:
        error_message = "No recommendations found for this book."
        error_type = "not_found"
        return render_template('recommend.html', error_message=error_message, error_type=error_type)

    try:
        # Get index of the book from the pivot table
        index = np.where(pt.index == user_input)[0][0]
        
        # Calculate similar items
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        # Prepare data for the recommendations
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)

        print(data)

        return render_template('recommend.html', data=data)
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('recommend.html', error_message=error_message)

@app.route("/books")
def get_books():
    """Returns all books as JSON."""
    book_list = [{"title": title} for title in pt.index]  # Convert to JSON-friendly format
    return jsonify(book_list)

if __name__ == '__main__':
    app.run(debug=True)
