This project aims to quantify my skill level as a chess player by analyzing my game history on Lichess.org.. To achieve this, I applied my Python programming and statistical analysis skills to extract, clean, organize, and interpret data from the Lichess API.

After connecting to the Lichess API and extracting my player data in JSON format, I selected and visualized the most relevant variables to build a structured dataset. The resulting file is available at [`Datasets/user_performance.csv`](./Datasets/user_performance.csv).

This dataset allowed me to quantify the number of games played across different time controls. To better visualize this distribution, I created a bar plot, available at [`Figures/games_by_mode.png.`](./Figures/games_by_mode.png.)

As shown in the figure, Rapid is by far the most played mode, with over 350 games. Blitz and Bullet have significantly fewer games, and there are no recorded games in Classical. The reason behind this preference is that Rapid offers a balanced format: it's not as long as Classical—which can be impractical if you're busy—but it's also not as short as Bullet or Blitz. This makes it ideal for developing strategic thinking, which is especially important for a beginner player like myself.

Therefore, the next stage of the investigation was to extract and visualize statistics from my rapid games. The sample consisted of the last 300 rapid games I played, which provided valuable insights into my playstyle. The data were retrieved from the Lichess API in PGN format, then parsed and organized to produce the final dataset [`Datasets/rapid_games.csv`](./Datasets/rapid_games.csv).
