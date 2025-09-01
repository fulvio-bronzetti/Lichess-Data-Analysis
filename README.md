A Python project to analyze my chess performance on Lichess.org via API.
It extracts user statistics, visualizes preferred game modes, and downloads the last 500 rapid games in PGN format.

🚀 Features
Secure connection to the Lichess API using a personal token.

Extraction of performance metrics by game mode (bullet, blitz, rapid, etc.).

Data visualization with bar plots.

Download of the last 500 rapid games in PGN format.

🛠️ Technologies Used
Python

berserk – to connect to the Lichess API.

dotenv – for secure token management.

pandas – for data manipulation.

matplotlib – for data visualization.

🔮 Future Goals
Estimate winning rates by opening.
Analysis of games to identify the most effective openings in terms of results.

Calculate the average number of blunders per game.
Assessment of game quality by extracting and classifying blunders.

Build a multinomial logistic model.
Prediction of game outcomes (win, loss, draw) based on key strategic variables such as opening, rating, number of moves, and more.
