# 📝 Diário de Aprendizado: Semana 01

Use este arquivo para registrar suas anotações de estudo, códigos, resumos de artigos e insights. Ao final da semana, você terá um excelente material de revisão!

---

## 🎯 Foco da Semana
* **Tema:** Modelagem de Dados e Python para Manipulação
* **Objetivo:** Entender a estruturação de tabelas para análise (Star Schema) e realizar limpeza/manipulação de dados local usando Python.

---

## 📓 Registro Diário

### 🔹 Dia 1: Modelagem Analítica (OLAP) e Conceito de Star Schema
* **O que estudei hoje:**
  - *Estudei modelagem de tabelas, tabela fato e tabela dimensão, tabela dimensão são as tabelas que trazem os dados descritivos para a nossa análise exemplo dados do cliente, do produto, locais, horários, os insumos que são utilizados para que a atividade aconteça, já a tabela fato nos traz o resultado das atividades, os números, exemplo: vendas, valores, totais e as chaves estrangeiras que é a conexão da tabela fato com as tabelas dimensões
o Conceito OLAP significa processamento analítico online das informações, geração de relatórios com os dados armazenados no DW , OLTP sistema que registra informações no DW  *
* **Prática/Anotações:**
  - *Resuma as principais diferenças e desenhe mentalmente (ou descreva) um Star Schema.*
tabela fato - tabelas dimensões -

* **Dificuldades & Dúvidas:**
  - *Ficou alguma dúvida sobre Tabelas Fato e Dimensão?*
* **Links interessantes do dia:**
  - *Cole aqui os artigos lidos.*
- [O que é Modelagem Dimensional? (Data Warehouse Info)](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/) - A metodologia clássica de Ralph Kimball.

### 🔹 Dia 2: Modelagem Dimensional em Detalhes
* **O que estudei hoje:**
  - *Como as tabelas Fato e Dimensão se relacionam (chaves surrogate, chaves estrangeiras).*
* **Prática/Anotações:**
  - *Identifique chaves primárias e chaves estrangeiras comuns em modelos de e-commerce ou vendas.*
* **Dificuldades & Dúvidas:**
  - *Algum termo ou conceito ficou confuso?*
* **Links interessantes do dia:**
  - *Links adicionais.*

### 🔹 Dia 3: Economia de Recursos na Nuvem (Performance de Modelos OLAP)
* **O que estudei hoje:**
  - *Por que estruturar os dados em Fato/Dimensão economiza processamento e custos em ferramentas de nuvem.*
* **Prática/Anotações:**
  - *Crie uma reflexão rápida sobre por que consultas em tabelas muito largas (denormalizadas) vs tabelas Star Schema se comportam de formas diferentes.*
* **Dificuldades & Dúvidas:**
  - *O que precisa ser revisado sobre performance e armazenamento analítico?*
* **Links interessantes do dia:**
  - *Links úteis.*

### 🔹 Dia 4: Python e Pandas - Leitura e Estruturas Básicas
* **O que estudei hoje:**
  - *Leitura de CSV/JSON e estruturas fundamentais do Pandas (Series e DataFrames).*
* **Prática/Anotações:**
  - *Exemplo rápido de código usado:*
    ```python
    import pandas as pd
    # Exemplo: ler um CSV
    # df = pd.read_csv("arquivo.csv")
    ```
* **Dificuldades & Dúvidas:**
  - *Dúvidas sobre manipulação inicial do Pandas.*
* **Links interessantes do dia:**
  - *Links úteis.*

### 🔹 Dia 5: Pandas - Limpeza, Filtros e Agregações
* **O que estudei hoje:**
  - *Tratamento de valores nulos (`fillna`, `dropna`), filtros booleanos e agregações (`groupby`).*
* **Prática/Anotações:**
  - *Trechos de código ou raciocínios desenvolvidos.*
* **Dificuldades & Dúvidas:**
  - *O que foi mais difícil na sintaxe do Pandas?*
* **Links interessantes do dia:**
  - *Documentação do Pandas ou guias de referência.*

### 🔹 Dia 6: Pandas Joins & Introdução ao PySpark (Teoria)
* **O que estudei hoje:**
  - *Fazer junções (`merge` e `concat`) em Pandas. Teoria de processamento distribuído com PySpark.*
* **Prática/Anotações:**
  - *Diferença entre o processamento em memória do Pandas (Single Node) e o particionamento do Spark (Multi Node).*
* **Dificuldades & Dúvidas:**
  - *O que achou mais complexo na arquitetura distribuída?*
* **Links interessantes do dia:**
  - *Leitura sobre PySpark.*

### 🔹 Dia 7: Implementação do Script Prático da Semana
* **O que estudei hoje:**
  - *Integração de tudo o que foi visto na semana para finalizar o script prático local.*
* **Prática/Anotações:**
  - *Caminho do script criado e um breve resumo do pipeline local desenvolvido.*
* **Dificuldades & Dúvidas:**
  - *Desafios encontrados durante o desenvolvimento e como foram solucionados.*

---

## 🛠️ Prática Semanal: Limpeza e Modelagem Local
> **Desafio:** Ler um CSV bagunçado, tratar valores nulos, separar em tabelas de Fato e Dimensão, e salvar o resultado final.

* **Dataset Utilizado:** *(ex: dados de vendas, log de acessos, etc.)*
* **Problemas Identificados no Dado Bruto:**
  - [ ] Valores nulos / ausentes.
  - [ ] Tipos de dados incorretos (ex: datas como texto, números como texto).
  - [ ] Registros duplicados.
* **Modelo Dimensional Definido:**
  - **Tabela Fato:** *(nome e colunas)*
  - **Tabelas Dimensão:** *(nomes e colunas)*
* **Caminho para o Código-Fonte:** `[Link para o arquivo/pasta no seu workspace]`

---

## 🔍 Autoavaliação da Semana

* **O que funcionou muito bem:**
  - *Escreva aqui suas maiores vitórias e facilidades aprendidas.*
* **O que precisa de mais atenção na próxima semana:**
  - *Conceitos teóricos ou práticos que ainda precisam amadurecer.*
* **Nível de confiança nos temas abordados:**
  - Modelagem Analítica / Star Schema: ⭐⭐⭐⭐⭐ (substitua pelas estrelas correspondentes)
  - Manipulação de Dados (Pandas): ⭐⭐⭐⭐⭐
  - Conceito de Processamento Distribuído (PySpark): ⭐⭐⭐⭐⭐
