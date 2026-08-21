from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Fester Termin
KURS_DATUM = datetime(2026, 8, 26, 15, 0)

@app.route("/")
def startseite():
    jetzt = datetime.now()

    # Lektion automatisch anhand der vergangenen Wochen berechnen
    if jetzt < KURS_DATUM:
        lektion = 1
    else:
        wochen = (jetzt.date() - KURS_DATUM.date()).days // 7
        lektion = wochen + 2

    return render_template(
        "index.html",
        lektion=lektion
    )

if __name__ == "__main__":
    app.run(debug=True)
