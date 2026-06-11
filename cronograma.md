# 📅 Cronograma Semanal (Dias 1 a 30)

Utilize este arquivo para acompanhar o seu progresso diário. Você pode marcar as caixas de seleção `[ ]` como `[x]` conforme for concluindo as tarefas.

---

## 🧭 Semana 1: Modelagem de Dados e Python para Manipulação
> **Foco:** Entender como estruturar tabelas para análise e como manipular dados via código.

- [ ] **Dias 1 a 3: Introdução à Modelagem Analítica (OLAP)**
  - [ ] Entender a diferença essencial entre bancos de dados transacionais (OLTP) e analíticos (OLAP).
  - [ ] Estudar o conceito de **Star Schema** (Tabelas Fato e Tabelas Dimensão).
  - [ ] Compreender por que a estruturação dimensional de dados economiza poder de processamento e custo na nuvem.
- [ ] **Dias 4 a 7: Python Focado em Dados**
  - [ ] Dominar o básico da biblioteca **Pandas** (leitura de CSVs/JSONs, filtros, joins e agregações).
  - [ ] Entender o conceito de processamento distribuído lendo sobre o **PySpark** e como ele gerencia dados que superam a memória RAM de uma única máquina.

---

## ☁️ Semana 2: Armazenamento em Nuvem (Data Lakes e Data Warehouses)
> **Foco:** Onde e como salvar dados de forma barata e rápida.

- [ ] **Dias 8 a 10: Amazon S3 (Data Lake)**
  - [ ] Criar uma conta gratuita (Free Tier) na AWS.
  - [ ] Aprender a criar *buckets* e compreender o conceito de particionamento (organização por ano/mês/dia).
  - [ ] Estudar a diferença de performance e custo entre formatos tradicionais (CSV) e formatos colunares (Parquet).
- [ ] **Dias 11 a 14: Google BigQuery (Data Warehouse)**
  - [ ] Acessar a sandbox gratuita do Google BigQuery (não necessita de cartão de crédito).
  - [ ] Subir as tabelas limpas na Semana 1 para o BigQuery.
  - [ ] Treinar consultas SQL analíticas avançadas utilizando `GROUP BY`, `WINDOW FUNCTIONS` e `JOINS`.

---

## 🛠️ Semana 3: Pipelines de Dados (ETL / ELT com AWS Glue e dbt)
> **Foco:** Mover os dados da origem para o destino e transformá-los dentro da nuvem.

- [ ] **Dias 15 a 17: Conceitos de Pipeline & AWS Glue**
  - [ ] Entender a diferença teórica e prática entre **ETL** (Extração, Transformação local, Carga) e **ELT** (Extração, Carga bruta, Transformação no destino).
  - [ ] Estudar os conceitos de **AWS Glue** (especialmente Data Catalog e Crawlers) para mapear e catalogar dados automaticamente.
- [ ] **Dias 18 a 21: Introdução ao dbt (data build tool)**
  - [ ] Entender por que o dbt se tornou o padrão de mercado para transformações dentro do Data Warehouse (camada de Transformação do ELT).
  - [ ] Aprender a escrever consultas SQL organizadas dentro do dbt.
  - [ ] Estudar a aplicação de testes automáticos do dbt (validação de dados nulos, únicos ou formatos inconsistentes).

---

## 🔗 Semana 4: Orquestração com Airflow e Projeto de Portfólio
> **Foco:** Automatizar tudo para rodar sozinho e consolidar o aprendizado em um projeto real.

- [ ] **Dias 22 a 25: Apache Airflow**
  - [ ] Compreender o conceito de **DAG (Directed Acyclic Graph)**, que representa o desenho lógico do fluxo de tarefas.
  - [ ] Entender como o Airflow orquestra a dependência temporal (ex: rodar script Python de extração às 02h00 e o dbt de transformação às 02h10).
- [ ] **Dias 26 a 30: O Projeto de Portfólio Fim a Fim**
  - Consolidar todos os conceitos criando e documentando um repositório no seu GitHub pessoal com o seguinte fluxo:
    1. **Extração:** Um script Python extrai dados de uma API pública/gratuita qualquer.
    2. **Ingestão:** Salva os dados brutos (JSON/CSV) em um bucket do Amazon S3.
    3. **Carga:** Carrega esses dados brutos diretamente no Google BigQuery.
    4. **Transformação:** Utiliza o dbt para limpar, modelar e estruturar esses dados em tabelas Fato e Dimensão.
    5. **Orquestração:** Cria uma DAG no Apache Airflow para automatizar e agendar todo o processo diário de ponta a ponta.

---

> [!IMPORTANT]
> Atualize este arquivo com `[x]` à medida que você avança para manter um registro visual claro do seu progresso!
