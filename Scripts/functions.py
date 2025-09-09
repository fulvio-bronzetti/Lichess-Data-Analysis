# load the berserk package to connect to the API, and the dotenv function to retrieve my token
import berserk 
from dotenv import load_dotenv
import os
from datetime import datetime
import io
import pandas as pd
import matplotlib.pyplot as plt
import chess.pgn

def find_games():
    """
    Extracts user performance from Lichess and returns it as a DataFrame.
    Rows: game modes (bullet, blitz, rapid, etc.)
    Columns: games, rating, rd, prog, prov
    """
    # load the token
    load_dotenv()
    token = os.getenv("token")
    if token is None:
        raise ValueError("Token not found. Make sure you have the 'token' environment variable set.")
    
    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    # user details
    user_data = client.account.get()
    modes = user_data['perfs']
    data = pd.DataFrame.from_dict(modes).T
    return data

def extract_rapid_games(username,format='pgn'):
    """
    Connects to the Lichess API and returns an iterator of the last 300 Rapid games of the user in JSON format.
    """
    # load the token
    load_dotenv()
    token = os.getenv("token")
    if token is None:
        raise ValueError("Token not found. Make sure you have the 'token' environment variable set.")
    #connect to the API
    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    # extract games pgn or json depending on the format parameter
    # check if format is valid and if games exist
    if(format=='pgn'):
        game_iterator = client.games.export_by_player(username, as_pgn=True, max=300, perf_type='rapid')
    elif(format=='json'):
        game_iterator = client.games.export_by_player(username, as_pgn=False, max=300, perf_type='rapid')
    else:
        raise ValueError("Invalid format. Use 'pgn' or 'json'.") 
    if(game_iterator is None):
        raise ValueError("No games found for the user.")
    #return the iterator
    return game_iterator

def clean_and_csv(game_iterator):
#cleans the data and saves as a csv file
    all_rows = []
    for x in game_iterator:
        #transform the game from pgn in order to read it with chess.pgn
        pgn_io = io.StringIO(x)
        game = chess.pgn.read_game(pgn_io)
            
        dict_game = dict(game.headers)
        # Determine the player's color from the game headers
        # "Baelor99" is my username, so we want to analyze games from my perspective
        if(dict_game.get('White')=="Baelor99"):
            color = 'White'
        else:
            color='Black'
        # Determine the game result from my perspective
        # Win if:
        #   - I am White and the game result is '1-0', OR
        #   - I am Black and the game result is '0-1'
        # Loss if:
        #   - I am White and the game result is '0-1', OR
        #   - I am Black and the game result is '1-0'
        # Otherwise, the game is a Draw
        if((dict_game.get('Result') == '1-0' and color == 'White') or (dict_game.get('Result') == '0-1' and color == 'Black')):
            result = 'Win'
        elif((dict_game.get('Result') == '0-1' and color == 'White') or (dict_game.get('Result') == '1-0' and color == 'Black')):
            result = 'Loss'
        else:
            result = 'Draw'
        # Get my and my opponent's Glicko ratings from the game headers
        # Logic:
        #   - If I am White: my rating is WhiteElo, opponent's rating is BlackElo
        #   - If I am Black: my rating is BlackElo, opponent's rating is WhiteElo
        if(color=='White'):
            OpponentGlicko=dict_game.get('BlackElo')
            UserGlicko=dict_game.get('WhiteElo')
        else:
            OpponentGlicko=dict_game.get('WhiteElo')
            UserGlicko = dict_game.get('BlackElo')
        # Create a dictionary to represent a single game
        # Extract the information needed for analysis:
        #   - ID: unique identifier for the game
        #   - TimeControl: the time mode of the game (e.g., rapid, blitz)
        #   - Date: when the game was played
        #   - ECO: opening code used in the game
        #   - Color: whether I played as White or Black
        #   - Result: outcome from my perspective (Win/Loss/Draw)
        #   - OpponentGlicko: rating of my opponent at the time
        #   - UserGlicko: my rating at the time
        #   - Termination: how the game ended (checkmate, resignation, timeout, etc.)

        #read the date from the pgn as a string
        #convert the string into a datetime object
        #change datetime format yy.mm.dd into yy-mm-dd
        wrong_date=dict_game.get("Date")
        wrong_date= datetime.strptime(wrong_date, "%Y.%m.%d")
        correct_date=wrong_date.strftime("%Y-%m-%d")

        row = {
                    "ID": dict_game.get('GameId'),
                    "TimeControl": dict_game.get("TimeControl"),
                    "Date": correct_date,
                    "ECO": dict_game.get("ECO"),
                    "Color": color,
                    "Result": result,
                    "OpponentGlicko": OpponentGlicko,
                    "UserGlicko": UserGlicko,
                    "termination": dict_game.get('Termination')
                }
        
        #append the dictionary to a list
        all_rows.append(row)
    
    #create a dataframe from the list of dictionaries
    data = pd.DataFrame(all_rows)
    # Save the DataFrame to a CSV file
    # This ensures that all game data is preserved even if the program is closed
    # or if new games are added to the iterator, preventing data loss
    data.to_csv("rapid_games.csv", index=False)
