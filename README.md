A Python project to analyze my chess performance on Lichess.org using the official API. It extracts user statistics, visualizes preferred game modes, and downloads the last 300 rapid games in PGN format for further analysis.

 Features
 Secure connection to the Lichess API via personal token

📊 Extraction of performance metrics by game mode (bullet, blitz, rapid, etc.)

📈 Data visualization using bar plots

📥 Download of the last 300 rapid games in PGN format

♜ Estimation of win rates by opening and by color

📐 Statistical test to compare win rates between playing as White and Black

🛠️ Technologies Used
Library	Purpose
berserk	Connects to the Lichess API
dotenv	Manages API token securely
pandas	Data manipulation and analysis
matplotlib	Data visualization
scipy.stats	Statistical testing (e.g., z-test)

🔮 Future Goals
Estimate the average number of blunders per game
Visualize Glicko-2 rating progression
