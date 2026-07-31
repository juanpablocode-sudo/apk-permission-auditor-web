"""
app.py
Web app Flask para apk-permission-auditor.
Recibe un APK subido por el usuario, lo analiza con analyzer.py
y muestra el resultado en el navegador.
"""

import os
import uuid
from flask import Flask, render_template, request, flash, redirect

from analyzer import analyze

app = Flask(__name__)
app.secret_key = "cambiar-esto-en-produccion"  # necesario para flash messages

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"apk"}
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MB, los APK pueden pesar bastante

app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result=None)


@app.route("/analyze", methods=["POST"])
def analyze_apk():
    if "apk_file" not in request.files:
        flash("No se envió ningún archivo.")
        return redirect("/")

    file = request.files["apk_file"]

    if file.filename == "":
        flash("No seleccionaste ningún archivo.")
        return redirect("/")

    if not allowed_file(file.filename):
        flash("El archivo debe tener extensión .apk")
        return redirect("/")

    # Nombre único para evitar colisiones si dos usuarios suben a la vez
    temp_filename = f"{uuid.uuid4().hex}.apk"
    temp_path = os.path.join(UPLOAD_FOLDER, temp_filename)
    file.save(temp_path)

    try:
        result = analyze(temp_path)
    except Exception as e:
        flash(f"No se pudo analizar el archivo: {e}")
        return redirect("/")
    finally:
        # Borramos el APK subido apenas terminamos - no lo necesitamos guardar
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)