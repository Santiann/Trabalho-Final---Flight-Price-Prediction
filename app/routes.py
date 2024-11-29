import plotly.express as px
import pandas as pd
from flask import Blueprint, render_template, request, flash, redirect, url_for
import os
from .utils import validate_csv

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def upload_file():
    df = None  # Inicializa a variável df fora do bloco condicional

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

    if df is not None:
        # Gerando gráficos de comparação das classes econômica e executiva
        graph_html = {}

        # Gráfico interativo - Preços por companhia aérea
        fig = px.scatter(
            df, x='airline', y='price', 
            title="Preços por Companhia Aérea"
        )
        fig.update_layout(xaxis_title="Companhia Aérea", yaxis_title="Preço")

        # Gráfico interativo - Preços por classe de voo
        fig2 = px.scatter(
            df, x='class', y='price', 
            title="Preços por Classe de Voo"
        )
        fig2.update_layout(xaxis_title="Classe", yaxis_title="Preço")

        # Calculando a média dos preços por companhia
        mean_prices = df.groupby('airline')['price'].mean().sort_values()

        # Gráfico para mostrar a média de preços das companhias
        fig3 = px.scatter(
            df, x=mean_prices.index, y=mean_prices.values,
            title="Média de preço por companhia"
        )
        fig3.update_layout(xaxis_title="Companhia Aérea", yaxis_title="Preço médio da passagem")

        mean_prices = df.groupby('stops')['price'].mean().reset_index()

        # Preço Médio do Bilhete por Número de Paradas
        fig4 = px.scatter(
            mean_prices, x='stops', y='price',
            title="Preço Médio do Bilhete por Número de Paradas"
        )
        fig4.update_layout(xaxis_title="Número de Paradas", yaxis_title="Preço médio da passagem")

        # Agrupando os dados para contagem por classe
        df2 = df.groupby(['class'], as_index=False).count()

        # Criando o gráfico de pizza
        fig5 = px.pie(
            df2, 
            names='class',  # Coluna para os rótulos (classes de voo)
            values='flight',  # Coluna para os valores (contagem de voos por classe)
            title="Distribuição das Classes de Voos"
        )

        # Atualizando o layout do gráfico
        fig5.update_traces(textinfo='percent+label')  # Exibe porcentagem e rótulos no gráfico

        # Criando o gráfico equivalente ao stripplot
        fig6 = px.strip(
            df,
            x='class',  # Eixo X: Classe do bilhete
            y='price',  # Eixo Y: Preço
            color='class',  # Paleta de cores com base nas classes
            title="Distribuição de Preços por Classe",
            stripmode='overlay'  # Modo padrão para plotar pontos sobrepostos
        )

        # Personalizando o layout
        fig6.update_layout(
            title_font=dict(size=18, family="Arial", color="black"),
            xaxis_title="Classe do Bilhete",
            yaxis_title="Preço do Bilhete (USD)",
            xaxis=dict(tickfont=dict(size=12)),
            yaxis=dict(tickfont=dict(size=12), gridcolor='lightgray', gridwidth=0.5),
            plot_bgcolor='white'
        )

        # Ajustando o traço dos pontos
        fig6.update_traces(
            marker=dict(size=7, line=dict(width=1, color="DarkSlateGrey")),
            jitter=0.3  # Adiciona dispersão horizontal (jitter)
        )

        # Adicionando gráficos ao dicionário com identificadores
        graph_html = {
            "airline_price": fig.to_html(full_html=False),
            "class_price": fig2.to_html(full_html=False),
            "mean_price": fig3.to_html(full_html=False),
            "stops_price": fig4.to_html(full_html=False),
            "class_airplace": fig5.to_html(full_html=False),
            "class2_price": fig6.to_html(full_html=False),
        }

        flash("Arquivo enviado e validado com sucesso!", "success")
        return render_template('upload.html', graph_html=graph_html)

    # Se não houver um arquivo CSV válido, retorna o formulário de upload
    return render_template('upload.html')
