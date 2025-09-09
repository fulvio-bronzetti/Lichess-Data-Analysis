from functions import find_games,extract_rapid_games,clean_and_csv
import pandas as pd
import matplotlib.pyplot as plt
#this script extracts the user performance from Lichess and saves it as a csv file
#then we analize the number of games played by mode and create a barplot to determine the most played mode
#it also extracts the rapid games and saves them as a csv file
def main():
    data = find_games()
    data.to_csv("user_performance.csv")
    #extract the subset of the dataframe with only the game modes and number of games played
    df=data.loc['bullet':'classical','games']
    #create a barplot of the game modes with respective number of games
    plt.bar(df.index,df.values)
    plt.xlabel("Game Modes")
    plt.ylabel("Number of Games Played")
    plt.title("Number of Games Played by Mode")
    plt.savefig("games_by_mode.png")
    plt.show()
    #rapid is the most played mode
    #so we extract the rapid games and save them as a csv file
    game_generator = extract_rapid_games("Baelor99",format='pgn')
    clean_and_csv(game_generator)
if __name__ == "__main__":
    main()