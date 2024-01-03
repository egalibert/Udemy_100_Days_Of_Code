# from flask import Flask, jsonify, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# import sqlite3
# import random


from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('cafes.db')
cursor = conn.cursor()

conn.commit()

# Close the connection after creating the table
conn.close()

@app.route('/')
def index():
    # Retrieve cafes from the database
    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cafe')  # Adjust the table name
    cafes = cursor.fetchall()
    conn.close()

    return render_template('index.html', cafes=cafes)

@app.route('/add_cafe', methods=['POST'])
def add_cafe():
    # Add a new cafe to the database
    name = request.form.get('name')
    location = request.form.get('location')

    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cafes (name, location) VALUES (?, ?)', (name, location))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete_cafe/<int:cafe_id>')
def delete_cafe(cafe_id):
    # Delete a cafe from the database
    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cafes WHERE id = ?', (cafe_id,))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)