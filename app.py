from flask import Flask, render_template, request
import sqlite3

from utils.sql_generator import generate_sql

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():

    sql_query = ""
    results = []

    if request.method == "POST":

        user_input = request.form["query"]

        # GENERATE SQL
        sql_query = generate_sql(user_input)

        try:

            conn = sqlite3.connect("database.db")

            cursor = conn.cursor()

            cursor.execute(sql_query)

            results = cursor.fetchall()

            conn.close()

        except Exception as e:

            results = [str(e)]

    return render_template(
        "index.html",
        sql_query=sql_query,
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)