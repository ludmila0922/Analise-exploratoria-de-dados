import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)
print("Selecione o arquivo CSV na janela que apareceu...")
caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo ncr_ride_bookings")

if not caminho_arquivo:
    print("Nenhum arquivo selecionado.")
else:
    # Carregar os dados
    df = pd.read_csv(caminho_arquivo)
    print("Arquivo carregado com sucesso!")

    df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df['hora'] = df['datetime'].dt.hour

  
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='hora', palette='viridis')
    plt.title('Padrões de Utilização: Volume de Reservas por Hora do Dia')
    plt.xlabel('Hora (0-23h)')
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='Vehicle Type', hue='Booking Status')
    plt.title('Características: Status da Reserva por Tipo de Veículo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

