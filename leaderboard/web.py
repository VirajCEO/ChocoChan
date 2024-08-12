from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import main
app = Flask(__name__)

@app.route('/')
def home():
    main.extract_data()
    return render_template('index.html')

@app.route('/index')
def index():
    main.extract_data()
    return render_template('index.html')

@app.route('/team')
def get_team():
    team = main.get_data()
    return jsonify(team)


@app.route('/leaderboard')
def leaderboard():
    main.extract_data()
    date_range = main.get_time()
    get_winner = main.get_winner()
    print(date_range)
    return render_template('leaderboard.html',date_range=date_range,winner_wager=get_winner)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
