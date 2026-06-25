import sqlite3

def conectar():
    return sqlite3.connect("./BancoDados/Brasileirao2026DB.db")  # banco no mesmo diretório