import numpy as np
import pandas as pd


def plot_with_presidents(X, y, ax, title='', xlabel='', ylabel='', label='', xlim=None, ylim=None):
	# Usando o mandatos_datetimes_corrigidos com pd.to_datetime já implementado
	if xlim is None:
		xlim = [pd.to_datetime('1994-01-01'), pd.to_datetime('2024-07-01')]

	mandatos = {
		'Carlos Menem': (pd.to_datetime('1989-07-08'), pd.to_datetime('1999-12-10')),
		'Fernando de la Rúa': (pd.to_datetime('1999-12-10'), pd.to_datetime('2001-12-20')),
		'Eduardo Duhalde': (pd.to_datetime('2002-01-02'), pd.to_datetime('2003-05-25')),
		'Néstor Kirchner': (pd.to_datetime('2003-05-25'), pd.to_datetime('2007-12-10')),
		'Cristina Fernández de Kirchner': (pd.to_datetime('2007-12-10'), pd.to_datetime('2015-12-10')),
		'Mauricio Macri': (pd.to_datetime('2015-12-10'), pd.to_datetime('2019-12-10')),
		'Alberto Fernández': (pd.to_datetime('2019-12-10'), pd.to_datetime('2023-12-10')),
		'Javier Milei': (pd.to_datetime('2023-12-10'), pd.to_datetime('2027-12-10')),
	}

	# Cores para os mandatos (adicionando uma nova cor)
	cores_mandatos = ['#9e9cc2', '#ffb6cd', '#f68cc6', '#6ec2c4', '#f3c2b8', '#a9eaec', '#ffc127', '#B9AEDC']  # Amarelo no final

	# Plotar a linha da dívida pública
	ax.plot(X, y, marker='o', color='orange', label=label)

	# Adicionar blocos dos mandatos
	for i, (presidente, (inicio, fim)) in enumerate(mandatos.items()):
		ax.axvspan(inicio, fim, color=cores_mandatos[i % len(cores_mandatos)], alpha=0.3, label=presidente)

	# Configurações do gráfico
	ax.set_title(title, fontsize=14)
	ax.set_xlabel(xlabel, fontsize=12)
	ax.set_xlim(xlim)

	if ylim is not None:
		ax.set_ylim(ylim)

	ax.set_ylabel(ylabel, fontsize=12)
	ax.grid(True)

	# Adicionar legenda
	ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Presidentes')

