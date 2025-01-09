from flask import Flask, request, jsonify, render_template
import json  # Import the json library for reading/writing JSON files

app = Flask(__name__)

# Load and save data to a JSON file
DATA_FILE = "data.json"

# Function to load data from the JSON file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:       
            return json.load(file)   # Return the data as a Python dictionary
    except FileNotFoundError:
        return {"movies": []}        # Return an empty list of movies if the file is not found


# Function to save data to the JSON file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)        # Save the data as JSON in the file


@app.route("/")
def index():
    # Render the frontend page
    return render_template("index.html")


# Route to get the list of all movies (GET request)
@app.route("/api/movies", methods=["GET"])
def get_movies():
    # Retrieve all movies
    data = load_data()                # Load the movie data
    return jsonify(data["movies"])    # Return the movie list as a JSON response


# Route to create a new movie (POST request)
@app.route("/api/movies", methods=["POST"])
def create_movie():
    # Add a new movie
    data = load_data()                  # Load current data
    new_movie = request.json            # Get the new movie details from the request body
    data["movies"].append(new_movie)    # Add the new movie to the list
    save_data(data)                     # Save the updated data to the file
    return jsonify(new_movie), 201      # Return the new movie as a JSON response with status 201 (Created)


# Route to update a movie (PUT request)
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    #Update movie details
    data = load_data()
    for movie in data["movies"]:       
        if movie["id"] == movie_id:      # Find the movie with the given ID
            movie.update(request.json)   # Update the movie details with the data from the request
            save_data(data)
            return jsonify(movie)
    return jsonify({"error": "Movie not found"}), 404      # Return an error if the movie is not found


# Route to delete a movie (DELETE request)
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    # Delete a movie
    data = load_data()
    movies = data["movies"]    # Get the list of movies

    # Find the movie to delete by ID
    movie_to_delete = next((movie for movie in movies if movie["id"] == movie_id), None)
    if movie_to_delete:
        movies.remove(movie_to_delete)        # Remove the movie from the list
        save_data(data)
        return jsonify({"message": "Movie deleted successfully"})
    return jsonify({"error": "Movie not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
