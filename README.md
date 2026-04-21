# 🏥 Tratamento de Fila de Espera em Saúde Pública

## 📌 Descrição do Projeto

Este projeto tem como objetivo a **qualificação e tratamento de uma base de dados de fila de espera em saúde pública**, visando aumentar a confiabilidade das informações para apoio à gestão e tomada de decisão.

Foram aplicadas técnicas de limpeza e padronização de dados, além de regras de negócio específicas, como identificação de óbitos, remoção de duplicidades e filtragem de registros inconsistentes.

---

## 🎯 Objetivos

* Padronizar dados inconsistentes (nomes e datas)
* Identificar pacientes em óbito na fila de espera
* Remover registros duplicados
* Aplicar regras de exclusão com base em critérios administrativos
* Gerar uma base final limpa e confiável

---

## ⚙️ Etapas do Pipeline

1. **Padronização de Datas**

   * Conversão de múltiplos formatos (`dd/mm/yyyy`, `yyyymmdd`, com hora)

2. **Padronização de Nomes**

   * Remoção de acentos
   * Padronização para caixa alta
   * Remoção de espaços extras

3. **Cruzamento com Base de Óbitos**

   * Comparação por nome + data de nascimento
   * Identificação de pacientes que faleceram após entrada na fila

4. **Aplicação de Regras de Negócio**

   * Filtragem por CNES
   * Exclusão por justificativas inconsistentes

5. **Tratamento de Duplicidades**

   * Identificação por ID do usuário
   * Marcação ou exclusão conforme regra

---

## 📊 Resultados

* Base original: ~492.000 registros
* Aplicação de filtros resultou em uma base mais confiável
* Identificação automatizada de óbitos
* Redução de inconsistências e duplicidades

---

## ⚠️ Sobre os Dados

Os dados utilizados neste projeto são **sensíveis e confidenciais**, portanto **não estão disponíveis neste repositório**.

Foram mantidos apenas os scripts e a estrutura do processo para fins de demonstração técnica.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* OpenPyXL

---

## 📂 Estrutura do Projeto

```
fila-espera-saude/
│
├── scripts/
│   ├── 01_padronizar_datas.py
│   ├── 02_padronizar_nomes.py
│   ├── 03_remover_obitos.py
│   ├── 04_tratar_justificativas.py
│
├── README.md
└── requirements.txt
```

---

## 🚀 Possíveis Melhorias

* Automatização completa do pipeline
* Criação de dashboard (Power BI / Streamlit)
* Uso de fuzzy matching para nomes
* Integração com banco de dados

---

## 👩‍💻 Autora

Projeto desenvolvido por Marta Magri
🔗 [LinkedIn](https://www.linkedin.com/in/marta-m-0645616a/)
🔗 [GitHub](https://github.com/Marmagri)
