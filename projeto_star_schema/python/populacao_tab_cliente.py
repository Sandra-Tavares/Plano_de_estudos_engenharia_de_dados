import psycopg2
from faker import Faker
from datetime import date, datetime, timedelta

fake = Faker('pt_BR')

def conectar():
    return psycopg2.connect(
        dbname="Entregas",
        user="produtos",
        password="Ajuda123!",
        host="localhost",
        port="5432",
        options="-c client_encoding=UTF8"
    )

def inserir_clientes(qtd=5):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
        nome = fake.name()
        segmento = fake.random_element(elements=("Varejo", "Atacado", "Distribuidor"))
        cidade = fake.city()
        print(nome, cidade)
        cur.execute(
            "INSERT INTO dim_cliente (nome_cliente, segmento, cidade) VALUES (%s, %s, %s)",
            (nome, segmento, cidade)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_motorista(qtd=50):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
        nome = fake.name()
        idade = fake.random_int(min=18, max=65)
        experiencia = fake.random_int(min=0, max=40)
        print(nome, idade, experiencia)
        cur.execute(
            "INSERT INTO dim_motorista (nome, idade, experiencia) VALUES (%s, %s, %s)",
            (nome, idade, experiencia)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_produtos(qtd=50):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
        categoria = fake.random_element(elements=("Eletrônicos", "Alimentos", "Roupas", "Brinquedos"))
        peso = round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        tipo = fake.random_element(elements=("Perecível", "Não Perecível"))
        print( categoria, peso, tipo)
        cur.execute(
            "INSERT INTO dim_produto (categoria, peso, tipo) VALUES (%s, %s, %s)",
            ( categoria, peso, tipo)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_regiao(qtd=50):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
       cidade=fake.city()
       estado=fake.state()
       pais=fake.country()
       print(cidade, estado, pais)
       cur.execute(
            "INSERT INTO dim_regiao (cidade, estado, pais) VALUES (%s, %s, %s)",
            (cidade,estado, pais)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_tempo(qtd=50):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
        ano = fake.random_int(min=2020, max=2024)
        mes = fake.random_int(min=1, max=12)
        dia= fake.random_int(min=1, max=28)  # Para evitar problemas com meses de 30/31 dias
        trimestre = (mes- 1) // 3 + 1
      
        print(dia, mes, trimestre, ano)
        cur.execute(
            "INSERT INTO dim_tempo (dia, mes, trimestre, ano) VALUES (%s, %s, %s, %s)",
            (dia, mes, trimestre, ano)
        )
    conn.commit()
    cur.close()
    conn.close()

import psycopg2
from faker import Faker
from datetime import date, datetime, timedelta

fake = Faker('pt_BR')

def conectar():
    return psycopg2.connect(
        dbname="Entregas",
        user="produtos",
        password="Ajuda123!",
        host="localhost",
        port="5432",
        options="-c client_encoding=UTF8"
    )

def inserir_clientes(qtd=5):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
        nome = fake.name()
        segmento = fake.random_element(elements=("Varejo", "Atacado", "Distribuidor"))
        cidade = fake.city()
        print(nome, cidade)
        cur.execute(
            "INSERT INTO dim_cliente (nome_cliente, segmento, cidade) VALUES (%s, %s, %s)",
            (nome, segmento, cidade)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_motorista(qtd=50):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
        nome = fake.name()
        idade = fake.random_int(min=18, max=65)
        experiencia = fake.random_int(min=0, max=40)
        print(nome, idade, experiencia)
        cur.execute(
            "INSERT INTO dim_motorista (nome, idade, experiencia) VALUES (%s, %s, %s)",
            (nome, idade, experiencia)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_produtos(qtd=50):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
        categoria = fake.random_element(elements=("Eletrônicos", "Alimentos", "Roupas", "Brinquedos"))
        peso = round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        tipo = fake.random_element(elements=("Perecível", "Não Perecível"))
        print( categoria, peso, tipo)
        cur.execute(
            "INSERT INTO dim_produto (categoria, peso, tipo) VALUES (%s, %s, %s)",
            ( categoria, peso, tipo)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_regiao(qtd=50):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
       cidade=fake.city()
       estado=fake.state()
       pais=fake.country()
       print(cidade, estado, pais)
       cur.execute(
            "INSERT INTO dim_regiao (cidade, estado, pais) VALUES (%s, %s, %s)",
            (cidade,estado, pais)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_tempo(qtd=50):
    conn = conectar()
    cur = conn.cursor()
    for _ in range(qtd):
        ano = fake.random_int(min=2020, max=2024)
        mes = fake.random_int(min=1, max=12)
        dia= fake.random_int(min=1, max=28)  # Para evitar problemas com meses de 30/31 dias
        trimestre = (mes- 1) // 3 + 1
      
        print(dia, mes, trimestre, ano)
        cur.execute(
            "INSERT INTO dim_tempo (dia, mes, trimestre, ano) VALUES (%s, %s, %s, %s)",
            (dia, mes, trimestre, ano)
        )
    conn.commit()
    cur.close()
    conn.close()

def inserir_fato_entrega(qtd=50):
    conn = conectar()
    cur = conn.cursor()

    # Buscar os IDs existentes nas tabelas dimensão
    cur.execute("SELECT id_cliente FROM dim_cliente")
    clientes = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id_motorista FROM dim_motorista")
    motoristas = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id_produto FROM dim_produto")
    produtos = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id_regiao FROM dim_regiao")
    regioes = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id_tempo FROM dim_tempo")
    tempos = [row[0] for row in cur.fetchall()]

    # Agora criamos entregas usando IDs reais
    for i in range(qtd):
        id_cliente = clientes[i % len(clientes)]
        id_motorista = motoristas[i % len(motoristas)]
        id_produto = produtos[i % len(produtos)]
        id_regiao = regioes[i % len(regioes)]
        id_tempo = tempos[i % len(tempos)]

        # Definir valores não aleatórios (exemplo: fixos ou calculados)
        valor_frete = 100.00
        custo_entrega = 80.00
        tempo_entrega = 3
        status_entrega = "Entregue"
        distancia_km = 15.0

        cur.execute(
            """
            INSERT INTO fato_entrega 
            (id_cliente, id_motorista, id_produto, id_regiao, id_tempo, 
             valor_frete, custo_entrega, tempo_entrega, status_entrega, distancia_km)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (id_cliente, id_motorista, id_produto, id_regiao, id_tempo,
             valor_frete, custo_entrega, tempo_entrega, status_entrega, distancia_km)
        )

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    try:
        inserir_clientes()
        inserir_motorista()
        inserir_regiao()
        inserir_produtos()
        inserir_tempo()
        inserir_fato_entrega()
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    try:
        inserir_clientes()
        inserir_motorista()
        inserir_regiao()
        inserir_produtos()
        inserir_tempo()
        inserir_fato_entrega()
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print("Erro:", e)
