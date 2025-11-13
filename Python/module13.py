import json
from flask import Flask, Response
import mysql.connector

app = Flask(__name__)


@app.route('/prime_check/<num>')
def check_prime(num):
    n = int(num)
    prime_status = True

    if n < 2:
        prime_status = False
    else:
        for factor in range(2, n):
            if n % factor == 0:
                prime_status = False
                break

    result = {"Number": n, "isPrime": prime_status}
    return Response(json.dumps(result), mimetype="application/json")



@app.route('/airport_info/<icao_code>')
def airport_lookup(icao_code):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Said2006",
        database="flight_game"
    )
    cur = db.cursor()

    query = """
        SELECT airport.name, country.name
        FROM airport
        JOIN country ON airport.iso_country = country.iso_country
        WHERE airport.ident = %s
    """
    cur.execute(query, (icao_code,))
    record = cur.fetchone()

    if record:
        response = {
            "ICAO": icao_code.upper(),
            "Name": record[0],
            "Country": record[1]
        }
    else:
        response = {"Error": "No matching airport found"}

    db.close()
    return Response(json.dumps(response), mimetype="application/json")



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
