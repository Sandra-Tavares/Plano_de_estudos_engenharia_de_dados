# 📚 Recursos, Materiais e Referências

Este arquivo reúne todos os links, leituras recomendadas, cursos gratuitos e detalhes das tarefas práticas de cada semana para apoiar seus estudos.

---

## 🧭 Semana 1: Modelagem de Dados e Python para Manipulação

### 📖 Leituras Essenciais
* **Modelagem Dimensional (OLAP / Star Schema):**
  - [Star Schema vs. Snowflake Schema (Towards Data Science)](https://towardsdatascience.com/understanding-star-schema-vs-snowflake-schema-ea118df283b0) - Artigo explicativo detalhando a diferença de performance e design.
  - [O que é Modelagem Dimensional? (Data Warehouse Info)](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/) - A metodologia clássica de Ralph Kimball.
* **Manipulação de Dados com Python:**

  - [Documentação Oficial do Pandas: Getting Started](https://pandas.pydata.org/docs/getting_started/index.html) - Guia passo a passo oficial para entender a estrutura dos DataFrames.
  - [PySpark Architecture & Core Concepts](https://spark.apache.org/docs/latest/api/python/index.html) - Introdução rápida ao processamento distribuído com Apache Spark.

### 🛠️ Atividade Prática da Semana
1. **Dataset de Entrada:** Procure um dataset pequeno e desorganizado no Kaggle (ex: vendas de lojas, dados de filmes) ou gere um arquivo CSV bagunçado simulado com valores nulos, registros duplicados e tipos incorretos.
2. **Transformação (Pandas):** Crie um script Python (`limpeza_dados.py`) para ler o CSV, filtrar registros inconsistentes, preencher ou remover valores nulos e renomear colunas para um formato legível.
3. **Modelagem:** Separe o dataset limpo em:
   - Uma tabela **Fato** (com as métricas numéricas e chaves estrangeiras).
   - Uma ou mais tabelas **Dimensão** (com os atributos descritivos, como datas, categorias de produtos ou clientes).
4. **Output:** Salve os novos datasets limpos localmente em formato CSV ou Parquet.

---

## ☁️ Semana 2: Armazenamento em Nuvem (Data Lakes e Data Warehouses)

### 📖 Leituras & Documentação
* **AWS Amazon S3 (Data Lake):**
  - [Criar conta AWS Free Tier](https://aws.amazon.com/free/) - Registre-se para obter acesso a 5 GB de armazenamento gratuito no S3 por 12 meses.
  - [Guia do usuário do Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) - Como criar buckets e configurar permissões básicas.
  - [CSV vs Parquet (Dremio Blog)](https://www.dremio.com/resources/guide/csv-vs-parquet/) - Entenda por que o Parquet é superior para analytics e economiza dinheiro.
* **Google BigQuery (Data Warehouse):**
  - [Google BigQuery Sandbox](https://cloud.google.com/bigquery/docs/sandbox) - Use o BigQuery sem inserir dados de cartão de crédito.
  - [Guia Rápido do Google Cloud: O que é o BigQuery?](https://cloud.google.com/bigquery/docs/introduction) - Introdução ao Data Warehouse serverless do Google.
  - [Praticando SQL Avançado (Kaggle Learn)](https://www.kaggle.com/learn/advanced-sql) - Excelente curso rápido e interativo com funções de janela (`WINDOW FUNCTIONS`) e joins.

### 🛠️ Atividade Prática da Semana
1. Crie um bucket no **Amazon S3** e organize uma estrutura de pastas simulando particionamento (ex: `dados-brutos/vendas/ano=2026/mes=06/dia=09/`).
2. Faça o upload manual ou via CLI do arquivo limpo na Semana 1 para o S3.
3. Crie um dataset no **Google BigQuery Sandbox**.
4. Importe o dataset do S3 (ou faça o upload do seu computador) para tabelas no BigQuery.
5. Escreva e execute consultas SQL para obter relatórios simples, utilizando:
   - `GROUP BY` para agregação de vendas por mês/categoria.
   - `ROW_NUMBER()` ou `SUM() OVER(PARTITION BY ...)` para cálculos de acumulado móvel e rankings.

---

## 🛠️ Semana 3: Pipelines de Dados (ETL / ELT com AWS Glue e dbt)

### 📖 Leituras & Cursos
* **Arquitetura de Dados:**
  - [ETL vs. ELT: A Nova Era de Analytics Engineering](https://www.getdbt.com/analytics-engineering/etl-vs-elt/) - Por que a transformação agora ocorre após a carga (Load).
* **AWS Glue:**
  - [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) - Entenda o funcionamento do Crawler e do Data Catalog.
* **dbt (data build tool):**
  - [🎓 Curso Gratuito: dbt Fundamentals (Oficial)](https://courses.getdbt.com/courses/dbt-fundamentals) - **Recomendado!** O melhor curso prático gratuito para começar a usar o dbt Cloud ou Core.
  - [Boas Práticas de Projeto no dbt](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview) - Como organizar diretórios de models, staging e marts.

### 🛠️ Atividade Prática da Semana
1. Inscreva-se no curso gratuito **dbt Fundamentals** e conclua os módulos práticos.
2. Configure um projeto local dbt ou utilize a versão gratuita do dbt Cloud.
3. Conecte o seu dbt ao seu Google BigQuery Sandbox.
4. Crie modelos (models) SQL no dbt para automatizar as transformações (Fato e Dimensão) criadas na Semana 1.
5. Adicione testes de qualidade nos seus arquivos de schema (ex: validar que a chave primária é `unique` e `not_null`).

---

## 🔗 Semana 4: Orquestração com Airflow e Projeto de Portfólio

### 📖 Leituras & Documentação
* **Apache Airflow:**
  - [Apache Airflow Official Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html) - Arquitetura de microsserviços do orquestrador.
  - [Conceitos Fundamentais: O que é uma DAG?](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) - Como planejar a execução cíclica e dependências.
* **Construção de Portfólio:**
  - [Como criar um Portfólio de Engenharia de Dados de Sucesso](https://towardsdatascience.com/how-to-build-a-data-engineering-portfolio-a-step-by-step-guide-1c3905477465) - Dicas para destacar seus repositórios do GitHub.

### 🛠️ Atividade Prática (O Projeto Final de Portfólio)
Junte todas as etapas do aprendizado em um único fluxo automatizado:
1. **Passo 1 (Python):** Script lê dados de uma API pública gratuita (ex: [OpenWeatherMap API](https://openweathermap.org/api), [CoinGecko API](https://www.coingecko.com/en/api), ou [PokeAPI](https://pokeapi.co/)).
2. **Passo 2 (S3):** Script envia os dados brutos no formato JSON ou CSV diretamente para o bucket do Amazon S3.
3. **Passo 3 (BigQuery):** Carga dos dados brutos para tabelas de staging no Google BigQuery.
4. **Passo 4 (dbt):** Execução do pipeline de transformação do dbt para estruturar os dados brutos de staging em tabelas limpas de Fato e Dimensões.
5. **Passo 5 (Airflow):** Orquestração completa. Uma única DAG que:
   - Dispara a tarefa de extração e ingestão no S3.
   - Dispara a tarefa de cópia do S3 para o BigQuery.
   - Dispara a tarefa `dbt run` e `dbt test` no BigQuery.
6. **Passo 6 (GitHub):** Suba todo o código (scripts Python, pasta do dbt, DAGs do Airflow) para um repositório no seu GitHub pessoal e escreva um `README.md` detalhado explicando o fluxo de dados e as ferramentas utilizadas.
