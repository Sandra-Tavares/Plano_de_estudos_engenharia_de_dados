CREATE TABLE dim_cliente (
id_cliente SERIAL PRIMARY KEY,
nome_cliente VARCHAR(100) NOT NULL,
segmento VARCHAR(100) NOT NULL,
cidade VARCHAR(30) NOT NULL
);

CREATE TABLE dim_produto (
id_produto SERIAL PRIMARY KEY,
categoria VARCHAR(100) NOT NULL,
peso DECIMAL(10,2) NOT NULL,
tipo VARCHAR(50) NOT NULL
);

CREATE TABLE dim_motorista (
id_motorista SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
idade INT NOT NULL,
experiencia INT NOT NULL
);

CREATE TABLE dim_tempo (
id_tempo SERIAL PRIMARY KEY,
dia INT NOT NULL,
mes INT NOT NULL ,
trimestre VARCHAR(10) NOT NULL,
ano INT NOT NULL
);

CREATE TABLE dim_regiao (
id_regiao SERIAL PRIMARY KEY,
cidade VARCHAR(50) NOT NULL,
estado VARCHAR(50) NOT NULL,
pais VARCHAR(50) NOT NULL
);

CREATE TABLE fato_entrega (
id_entrega SERIAL PRIMARY KEY,
tempo_entrega INT NOT NULL,
status_entrega VARCHAR(20) NOT NULL,
valor_frete DECIMAL(10,2) NOT NULL,
custo_entrega DECIMAL(10,2) NOT NULL,
distancia_km NUMERIC(10,2) NOT NULL NOT NULL,
id_cliente SERIAL,
id_produto SERIAL,
id_motorista SERIAL,
id_tempo SERIAL,
id_regiao SERIAL,
FOREIGN KEY (id_cliente) REFERENCES dim_cliente(id_cliente),
FOREIGN KEY (id_produto) REFERENCES dim_produto(id_produto),
FOREIGN KEY (id_motorista) REFERENCES dim_motorista(id_motorista),
FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id_tempo),
FOREIGN KEY (id_regiao) REFERENCES dim_regiao(id_regiao)
)