import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest
#this script analyzes the rapid games saved in rapid_games.csv and calculates statistics such as win rate, win rate by ECO and win rate by color
#it then tests if the difference in win rate between white and black is statistically significant using a z-test for two proportions
def main():
    # Load the CSV file into a DataFrame
    df = pd.read_csv("rapid_games.csv")
    #calculate total win rate
    total_games=len(df)
    print("Total games played: ",total_games)
    #print the game results counts, we want to see how many wins, losses and draws and then calculate the win rate
    results=df['Result'].value_counts()
    #print a barplot of the results using matplotlib
    plt.bar(results.index,results.values)
    plt.xlabel("Result")
    plt.ylabel("Count")
    plt.title("Game Results")
    plt.savefig("game_results.png")
    plt.show()
    #calculate win rate: we extract the number of wins from the results and then divide it by the total number of games played
    wins=results['Win']
    print("Total wins: ",wins)
    print("Win rate: ",(wins/total_games)*100)
    #now we want to see the win rate by ECO
    #we use the groupby function to group the dataframe by ECO and then we count the number of wins, losses and draws for each ECO 
    #and then calculate the win rate
    table=df.groupby('ECO')['Result'].value_counts().unstack(fill_value=0)
    table['Total']=table.sum(axis=1)
    table['Win Rate']=(table['Win']/table['Total'])*100
    table.to_csv("win_rate_by_eco.csv")
    #make a barplot of the win rate by ECO but only for the those with at least 15 games played
    filtered_table=table[table['Total']>15]
    print(filtered_table)
    plt.bar(filtered_table.index,filtered_table['Win Rate'])
    plt.xlabel("ECO")
    plt.ylabel("Win Rate (%)")
    plt.title("Win Rate by ECO")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("win_rate_by_eco.png")
    plt.show()
    #now we want to see if i play better as white or black
    color_stats=df.groupby('Color')['Result'].value_counts().unstack(fill_value=0)
    color_stats['Total']=color_stats.sum(axis=1)
    color_stats['Win Rate']=(color_stats['Win']/color_stats['Total'])*100
    print(color_stats)
    #white has a higher win rate than black, we want to test if this is statistically significant
    #we extract n1 and n2, the number of games played as white and black respectively
    total_by_color=color_stats['Total'].values
    #extract the number of wins as white and black respectively
    wins_by_color=color_stats['Win'].values
    #we use the formula for the z-test for two proportions
    zstat,pval=proportions_ztest(wins_by_color,total_by_color)
    print("Z-statistic: ",zstat)
    print("P-value: ",pval)
    #pvalue is 0.45, we cannot reject the null hypothesis, there is no statistically significant difference between the win rate as white and black
if __name__ == "__main__":
    main()
