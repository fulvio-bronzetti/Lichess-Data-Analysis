# load the berserk package to connect to the API, and the dotenv function to retrieve my token
import berserk 
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt

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

def bar_plot(data):
    """
    Creates a bar plot for the given DataFrame.
    """
    # Create the bar plot
    data.plot(kind='bar', figsize=(12, 6))
    plt.title("Game Performance")
    plt.xlabel("Game Mode")
    plt.ylabel("Number of Games")
    plt.legend(title="Statistics", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def extract_rapid_games(username):
    """
    Connects to the Lichess API and returns the last 500 Rapid games of the user in PGN format.
    """
    # load the token
    load_dotenv()
    token = os.getenv("token")
    if token is None:
        raise ValueError("Token not found. Make sure you have the 'token' environment variable set.")
    
    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    # extract games
    game_generator = client.games.export_by_player(username, as_pgn=True, max=500, perf_type='rapid')
    return list(game_generator)


def main():
    data = find_games()
    # Select only the desired modes
    categories = ['blitz', 'rapid', 'classical', 'bullet','puzzle']
    filtered_data = data.loc[categories, ['games']]

    # bar_plot(filtered_data)

if __name__ == "__main__":
    main()