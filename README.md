# API Usage

Developers will need to authenticate with their API key before using the SDK. Once authenticated, they can use the `GandalfAPI`  class to retrieve data from the API for movies and quotes.

### Install:

    pip install GandalfAPI

### Example Code:

```

from  GandalfAPI  import  GandalfAPI

api_key = "YOUR_API_KEY"
# Initialize the GandalfAPI object
api = GandalfAPI(api_key)

# Get all movies
movies = api.movie.all()
for  movie  in  movies["docs"]:
	print(movie["name"])

```
