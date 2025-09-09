A Python project to analyze my chess performance on Lichess.org via API.
It extracts user statistics, visualizes preferred game modes, and downloads the last 300 rapid games in PGN format.

🚀 Features
Secure connection to the Lichess API using a personal token.

Extraction of performance metrics by game mode (bullet, blitz, rapid, etc.).

Data visualization with bar plots.

Download of the last 300 rapid games in PGN format.

Estimation of Winning rates by opening and by color.

Statistical test to compare win rates of black and white.

🛠️ Technologies Used
Python

berserk – to connect to the Lichess API.

dotenv – for secure token management.

pandas – for data manipulation.

matplotlib – for data visualization.

scipy.stats - for statistical tests

🔮 Future Goals
Estimate the average amount of blunders by game
