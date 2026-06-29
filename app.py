from flask import Flask, render_template_string, request
from datetime import datetime
import secrets
import string

app = Flask(__name__)

VERSION = "1.0.0"

# Diseño en HTML/CSS para un generador de contraseñas de ciberseguridad moderno
TEMPLATE_PASSWORD = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generador de Contraseñas DevOps</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #1e293b;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            text-align: center;
            width: 380px;
        }
        h1 { color: #38bdf8; margin-bottom: 5px; font-size: 24px; }
        h2 { color: #94a3b8; font-size: 13px; margin-top: 0; margin-bottom: 25px; }
        
        .form-group {
            text-align: left;
            margin-bottom: 15px;
        }
        label {
            display: block;
            font-size: 14px;
            color: #cbd5e1;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="number"] {
            width: 100%;
            padding: 12px;
            border: 1px solid #475569;
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 16px;
            background-color: #334155;
            color: white;
        }
        .checkbox-group {
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            cursor: pointer;
            user-select: none;
        }
        .checkbox-group input {
            margin-right: 10px;
            width: 18px;
            height: 18px;
            cursor: pointer;
        }
        button {
            width: 100%;
            background-color: #0284c7;
            color: white;
            padding: 14px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.2s;
            margin-top: 15px;
        }
        button:hover { background-color: #0369a1; }
        
        .result {
            margin-top: 25px;
            padding: 15px;
            background-color: #0284c71a;
            border: 1px solid #0284c7;
            border-radius: 6px;
            text-align: left;
        }
        .password-display {
            font-family: 'Courier New', Courier, monospace;
            font-size: 18px;
            color: #38bdf8;
            background-color: #0f172a;
            padding: 10px;
            border-radius: 4px;
            word-break: break-all;
            margin-top: 8px;
            text-align: center;
            border: 1px solid #334155;
        }
        footer {
            margin-top: 25px;
            font-size: 11px;
            color: #64748b;
            line-height: 1.4;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🛡️ DevOps Password Gen</h1>
    <h2>Servidor Contabo | Versión {{ version }}</h2>
    
    <form method="POST">
        <div class="form-group">
            <label for="longitud">Longitud de la clave (8-32):</label>
            <input type="number" id="longitud" name="longitud" value="{{ longitud }}" min="8" max="32" required>
        </div>
        
        <div style="text-align: left; margin-top: 15px; margin-bottom: 15px;">
            <label style="margin-bottom: 10px;">Parámetros de Seguridad:</label>
            
            <label class="checkbox-group">
                <input type="checkbox" name="mayusculas" value="y" {% if mayusculas %}checked{% endif %}>
                <span>Incluir Mayúsculas (A-Z)</span>
            </label>
            
            <label class="checkbox-group">
                <input type="checkbox" name="numeros" value="y" {% if numeros %}checked{% endif %}>
                <span>Incluir Números (0-9)</span>
            </label>
            
            <label class="checkbox-group">
                <input type="checkbox" name="simbolos" value="y" {% if simbolos %}checked{% endif %}>
                <span>Incluir Símbolos (!@#$...)</span>
            </label>
        </div>
        
        <button type="submit">Generar Clave Segura</button>
    </form>

    {% if resultado %}
    <div class="result">
        <span style="font-size: 13px; color: #94a3b8; font-weight: bold;">🔑 Contraseña Generada:</span>
        <div class="password-display">{{ resultado }}</div>
    </div>
    {% endif %}

    <footer>
        Hora del servidor: {{ hora }}<br>
        Desplegado de forma independiente mediante Docker Swarm
    </footer>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def generador():
    resultado = ""
    longitud = 12
    mayusculas = True
    numeros = True
    simbolos = True
    
    if request.method == "POST":
        try:
            longitud = int(request.form.get("longitud", 12))
            mayusculas = request.form.get("mayusculas") == "y"
            numeros = request.form.get("numeros") == "y"
            simbolos = request.form.get("simbolos") == "y"
            
            # Construir set de caracteres base (minúsculas por defecto)
            caracteres = string.ascii_lowercase
            if mayusculas:
                caracteres += string.ascii_uppercase
            if numeros:
                caracteres += string.digits
            if simbolos:
                caracteres += "!@#$%^&*()-_=+[]{}|;:,.<>?"
            
            # Generación criptográficamente segura usando 'secrets'
            resultado = "".join(secrets.choice(caracteres) for _ in range(longitud))
                    
        except Exception as e:
            resultado = f"Error al generar: {str(e)}"

    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return render_template_string(
        TEMPLATE_PASSWORD,
        version=VERSION,
        hora=hora_actual,
        resultado=resultado,
        longitud=longitud,
        mayusculas=mayusculas,
        numeros=numeros,
        simbolos=simbolos
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)