import plotly.express as px
import pandas as pd
from flask import Blueprint, render_template, request, flash, redirect, url_for
import os
from .utils import validate_csv

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or not file.filename.endswith('.csv'):
            flash("Por favor, envie um arquivo CSV válido.", "error")
            return redirect(url_for('main.upload_file'))

        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        # Valida se o CSV contém as colunas necessárias
        if not validate_csv(filepath):
            flash("O CSV enviado não contém as colunas necessárias.", "error")
            return redirect(url_for('main.upload_file'))

        # Lê o arquivo CSV para usar no gráfico
        df = pd.read_csv(filepath)

        # Gerando um gráfico interativo
        fig = px.scatter(df, x='airline', y='price', title="Gráfico Interativo")
        graph_html = fig.to_html(full_html=False)

        flash("Arquivo enviado e validado com sucesso!", "success")
        return render_template('upload.html', graph_html=graph_html)

    return render_template("upload.html")
