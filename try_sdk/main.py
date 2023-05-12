from GandalfAPI import GandalfAPI

api_key = "AaXJ-bZqz2JhFIvb76dQ"

# Initialize the GandalfAPI object
api = GandalfAPI(api_key)

# Get all movies
movies = api.movie.all()
for movie in movies["docs"]:
    print(movie["name"])

# # Get quotes for a specific movie
# movie_id = "5cd95395de30eff6ebccde56"
# quotes = api.movie.quotes(movie_id)
# print(quotes)

# # Get all quotes
# all_quotes = api.quote.all()
# print(all_quotes)

# # Get a single quote by ID
# quote_id = "5cd96e05de30eff6ebcce7e9"
# quote = api.quote.get(quote_id)
# print(quote)
