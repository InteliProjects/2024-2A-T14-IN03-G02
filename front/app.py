from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Carrega os times únicos do CSV
df = pd.read_csv('matchess.csv', delimiter=';')
home_team_unique = df['home_team_name'].drop_duplicates()
away_team_unique = df['away_team_name'].drop_duplicates()

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html', home_teams=home_team_unique, away_teams=away_team_unique)

# Rota para a página dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
