
# SDK Design for The Lord of the Rings API

## Introduction

This document outlines the design for a Python SDK to access The Lord of the Rings API, which provides data related to The Lord of the Rings movies and qoutes. The SDK will provide an easy-to-use interface for developers to retrieve data from the API, with minimal setup required. I have named it **GandalfAPI** 😇

  
# Goals
The goals of this SDK are to:

Provide a Pythonic interface to The Lord of the Rings API
Be easy to install and use for developers
Follow best practices for Python package development
Allow developers to access movie and quote data from the API

# Architecture

The SDK will consist of the following components:

**BaseAPI class:** This will be an abstract base class that provides common functionality to both the `MovieAPI` and `QuoteAPI` classes, such as making API requests and handling authentication.

**MovieAPI class:** This class will provide methods to retrieve movie data from the API, such as getting all movies or quotes for a specific movie.

**QuoteAPI class:** This class will provide methods to retrieve quote data from the API, such as getting all quotes or a specific quote.

## Details:
In my SDK design, the **init**.py file initializes two classes, `MovieAPI` and QuoteAPI, and a GandalfAPI class that combines these two classes.

The `MovieAPI` class has three methods that allow for fetching movie data from the API: `all(**params)`, `get(id=movie_id)`, and `quotes(movie_id, **params)`. The `all()` method returns a list of all movies, while the `quotes()` method returns a list of quotes for a specific movie identified by the movie_id. The `quotes()` method can also take optional limit and offset parameters to limit the number of quotes returned and set the starting index, respectively. The get() method fetches data for a specific movie based on the movie_id parameter.

Similarly, the `QuoteAPI` class has two methods that allow for fetching quote data from the API: `all(**params)` and `get(id)`. The `all()` method returns a list of all quotes, while the `get()` method returns a single quote identified by the id parameter.

Finally, the `GandalfAPI` class initializes the `MovieAPI` and `QuoteAPI` classes and combines their functionality. It takes an api_key parameter and has movie and quote attributes that can be used to access the methods in their respective classes. This allows users to fetch both movie and quote data from the API using a single API key. Example usage of the `GandalfAPI` class could include fetching a list of all movies, fetching quotes for a specific movie, or fetching a specific quote by ID.
