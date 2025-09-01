Un progetto in Python per analizzare le mie performance di gioco su [Lichess.org](https://lichess.org) tramite API.  
Estrae statistiche utente, visualizza le modalità di gioco preferite e scarica le ultime 500 partite Rapid in formato PGN.

## 🚀 Funzionalità
- Connessione sicura all'API Lichess con token personale
- Estrazione delle performance per modalità di gioco (bullet, blitz, rapid, ecc.)
- Visualizzazione dei dati con barplot
- Download delle ultime 500 partite Rapid in formato PGN

## 🛠️ Tecnologie utilizzate
- Python
- [berserk](https://pypi.org/project/berserk/) – per connettersi all'API Lichess
- dotenv – per gestire il token in modo sicuro
- pandas – per la manipolazione dei dati
- matplotlib – per la visualizzazione

## 🔮 Obiettivi futuri

- **Stimare il tasso di vittoria per apertura**  
  Analisi delle partite per identificare le aperture più efficaci in termini di risultati.

- **Calcolare la quantità media di errori gravi (blunder) per partita**  
  Valutazione della qualità del gioco attraverso l’estrazione e la classificazione degli errori.

- **Costruire un modello logistico multinomiale**  
  Previsione dell’esito della partita (vittoria, sconfitta, patta) in base a variabili strategiche da definire, come apertura, rating, numero di mosse, ecc.
