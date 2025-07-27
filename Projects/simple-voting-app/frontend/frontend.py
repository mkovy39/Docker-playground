from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)
DB_NAME = 'votes.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected = request.form.get('country')
        if selected in ['Bangladesh', 'Canada']:
            conn = sqlite3.connect(DB_NAME)
            c = conn.cursor()
            c.execute("INSERT INTO votes (country) VALUES (?)", (selected,))
            conn.commit()
            conn.close()
        return redirect('/results')

    return '''
        <h1>Vote for Your Country</h1>
        <form method="post">
            <button type="submit" name="country" value="Bangladesh">Bangladesh</button>
            <button type="submit" name="country" value="Canada">Canada</button>
        </form>
    '''

@app.route('/results')
def results():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT country, COUNT(*) FROM votes GROUP BY country")
    results = dict(c.fetchall())
    conn.close()

    bd_votes = results.get('Bangladesh', 0)
    ca_votes = results.get('Canada', 0)

    if bd_votes > ca_votes:
        winner = 'Bangladesh 🇧🇩'
    elif ca_votes > bd_votes:
        winner = 'Canada 🇨🇦'
    else:
        winner = 'It\'s a tie! 🤝'

    return render_template_string('''
        <h1>Voting Results</h1>
        <ul>
            <li>Bangladesh: {{ bd_votes }} votes</li>
            <li>Canada: {{ ca_votes }} votes</li>
        </ul>
        <h2>🏆 Winner: {{ winner }}</h2>
        <a href="/">Vote Again</a>
    ''', bd_votes=bd_votes, ca_votes=ca_votes, winner=winner)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
