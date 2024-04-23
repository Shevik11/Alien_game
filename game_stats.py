import mysql.connector

# Replace these values with your MySQL server information
host = 'localhost'
user = 'root'
password = '904496Vfrc'
database = 'cosmic_game'

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

record_query = "SELECT max_score FROM score WHERE top = 65;"
cursor.execute(record_query)

# Fetch the result using fetchone()
record = cursor.fetchone()

# Close the cursor and connection when done
cursor.close()
connection.close()

# Check if record is not None before using it
max_score = record[0] if record else 0.0

class Game_Stats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = float(max_score)  # Convert to float

        self.ships_left = 3

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
