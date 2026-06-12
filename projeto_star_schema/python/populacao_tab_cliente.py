import psycopg2
from faker import Faker

fake = Faker('pt_BR')

conn = psycopg2.connect(
    dbname="Entregas",
    user ="postgres",
    password="123456",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

for _ in range(100):
    nome = fake.name()
    segmento = fake.random_element(elements=("Varejo", "Atacado", "Distribuidor"))
    cidade = fake.city()
    cur.execute("INSERT INTO dim_cliente (nome_cliente, segmento, cidade) VALUES (%s, %s, %s)", 
                 (nome, segmento, cidade)
                 )
conn.commit()
cur.close()
conn.close()