# Twitter Clone App

## Description
This Twitter Clone App is a simple social media application built using Flask, it allows users to post tweets and view tweets from other users.
It features a RESTful API for managing tweets and user accounts.

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask
- Flask-Migrate
- Flask-SQLAlchemy
- PostgreSQL

### Setup
1. Clone the repository:
https://github.com/anthony-vlrd/Twitter-Clone

2. Install the required packages:
pip install -r requirements.txt

3. Set up the PostgreSQL database:

4. Run the database migrations:

5. Start the application:


## API Endpoints

### Tweets
- `GET /tweets`: Retrieve all tweets.
- `GET /tweets/<int:id>`: Retrieve a specific tweet by ID.

### Users
- `GET /users`: Retrieve all users.

## Models
- **User**: Represents the user with username, password, and associated tweets.
- **Tweet**: Represents a tweet with content, creation date, and reference to the user.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests to the main branch. Ensure you write tests for new features and document changes accordingly.


