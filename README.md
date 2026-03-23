# 🫀 Predição de Doença Cardíaca

Projeto de Machine Learning para predição de doenças cardíacas usando Regressão Logística otimizada com GridSearchCV.

## 📋 Sobre o Projeto

O objetivo é identificar pacientes com risco de doença cardíaca com base em dados clínicos. Por se tratar de um problema médico, o **Recall** foi escolhido como métrica principal — é mais importante não deixar passar nenhum paciente doente do que gerar alguns alarmes falsos.

## 📊 Resultados

| Modelo | Recall |
|---|---|
| Logistic Regression (baseline) | 0.7368 |
| Random Forest | 0.7368 |
| Decision Tree | 0.6052 |
| Gradient Boosting | 0.6315 |
| **Logistic Regression + GridSearchCV** | **0.8158** |

## 🛠️ Tecnologias

- Python
- Pandas
- Scikit-learn
- Matplotlib / Plotly
- Streamlit
- Joblib

## 📁 Estrutura do Projeto
```
├── Heart_Disease_Prediction.csv   # Dataset
├── inicial.ipynb                  # Notebook com toda a análise
├── app.py                         # Aplicação Streamlit
├── modelo_heart_disease.pkl       # Modelo treinado
├── scaler.pkl                     # Scaler salvo
└── README.md
```

## 🚀 Como Executar

1. Clone o repositório
2. Instale as dependências:
```
pip install -r requirements.txt
```
3. Rode a aplicação:
```
python -m streamlit run app.py
```

## 📚 Metodologia

Projeto desenvolvido seguindo a metodologia **CRISP-DM**:
1. Entendimento do negócio
2. Exploração dos dados
3. Preparação dos dados
4. Modelagem e otimização
5. Avaliação
6. Implantação com Streamlit
```

---

Depois cria também um arquivo `requirements.txt` para quem for rodar o projeto saber quais bibliotecas instalar:
```
pandas
scikit-learn
streamlit
joblib
numpy
plotly
matplotlib