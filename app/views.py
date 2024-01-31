import sqlite3
from flask import render_template, request, redirect, url_for, g
from app import app

DATABASE = 'vocabulary.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    cur.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query:
        # Assume you have a function to search the dictionary API
        results = search_dictionary_api(query)
        # Save the result to the database
        for res in results:
            insert_db('INSERT INTO vocabulary (word, part_of_speech, definition) VALUES (?, ?, ?)',
                      [res['word'], res['part_of_speech'], res['definition']])
        return render_template('search.html', results=results)
    else:
        return redirect(url_for('index'))

# Assume you have a function that calls the dictionary API
def search_dictionary_api(word):
    # This function would actually make the API call to the dictionary service
    # For now, it's just a placeholder that returns an empty list
    return []