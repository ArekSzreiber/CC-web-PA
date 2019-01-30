# Codecool Series DB
A system to help you store your favourite TV shows. 

## The story
This is a basic practice session to go through the basics of WEB technologies with python backend, postgres and some code on front-end.

A dumb wireframe is provided in the `design.html` file with will help you mix'n'match elements without lot of styling work.

## Setup

1. Clone this repo
1. Open a terminal in the root folder of the cloned repository.
1. Create a _virtualenv_: `virtualenv venv`
1. Activate the _virtualenv_: `source venv/bin/activate`
1. Install pip dependencies: `pip install -r requirements.txt`
1. Create a Postgres database for this project
1. Set the environment variables which the code uses to connect to the database. For this you have two ways:
   1. Using the IDE: for example if you use pyCharm, then editing the configuration you can set environment variables. The necesssary ones you can find in `setenv.sh.template`
   1. Set the environment variables from the terminal. For this you can use our prewritten sh file (unix (linux) shell executables file):
      1. Make a copy of the `setenv.sh.template` file in the new name of `setenv.sh`
      1. Fill out the `setenv.sh` with **YOUR** details
      1. Source the `setenv.sh` file in the command line with the `source setenv.sh` command. You have to do it from the same terminal where you start main.py later.
1. To create your database structure follow list below:
   1. Run the `data/db_schema/01_create_schema.sql` SQL file to create empty tables
   1. Unzip the `data/dump_1000_shows.zip` file
   1. Run the unzipped sql files in the following order:
      1. genres
      1. shows
      1. show_genres
      1. seasons
      1. episodes
      1. actors
      1. show_characters
1. Run the server with: *`python main.py`*
1. After you stop the server run: *`deactivate`* in the command line to clean up the variables used

## Database

![Relational model](data/db_schema/relational_model.png?raw=true "Relational model")
