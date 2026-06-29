from flask import Flask

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/")
def inicio():
    return f"""
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Nueva App</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f7f6; }}
            h1 {{ color: #2c3e50; }}
            .badge {{ background-color: #3498db; color: white; padding: 5px 10px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>🚀 ¡Nueva Aplicación Desplegada Exitosamente!</h1>
        <h2>Versión: <span class="badge">{VERSION}</span></h2>
        <p>El pipeline de CI/CD funciona correctamente y está expuesto vía Traefik.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)