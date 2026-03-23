import streamlit as st
import joblib
import numpy as np

# Carregar modelo e scaler
modelo = joblib.load('modelo_heart_disease.pkl')
scaler = joblib.load('scaler.pkl')

# Título da aplicação
st.title('🫀 Predição de Doença Cardíaca')
st.write('Preencha os dados do paciente abaixo para verificar o risco de doença cardíaca.')

# Inputs do usuário
age = st.number_input('Idade', min_value=1, max_value=120, value=50)
sex = st.selectbox('Sexo', options=[0, 1], format_func=lambda x: 'Feminino' if x == 0 else 'Masculino')
chest_pain = st.selectbox('Tipo de Dor no Peito', options=[1, 2, 3, 4])
bp = st.number_input('Pressão Arterial (BP)', min_value=50, max_value=250, value=120)
cholesterol = st.number_input('Colesterol', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Glicose em Jejum > 120mg/dl', options=[0, 1], format_func=lambda x: 'Não' if x == 0 else 'Sim')
ekg = st.selectbox('Resultado do EKG', options=[0, 1, 2])
max_hr = st.number_input('Frequência Cardíaca Máxima', min_value=50, max_value=250, value=150)
angina = st.selectbox('Angina por Exercício', options=[0, 1], format_func=lambda x: 'Não' if x == 0 else 'Sim')
st_depression = st.number_input('Depressão ST', min_value=0.0, max_value=10.0, value=0.0)
slope = st.selectbox('Inclinação do ST', options=[1, 2, 3])
vessels = st.selectbox('Número de Vasos (Fluoroscopia)', options=[0, 1, 2, 3])
thallium = st.selectbox('Tálio', options=[3, 6, 7])

# Botão de previsão
if st.button('🔍 Analisar Paciente'):
    dados = np.array([[age, sex, chest_pain, bp, cholesterol, fbs,
                       ekg, max_hr, angina, st_depression, slope, vessels, thallium]])
    
    dados_normalizados = scaler.transform(dados)
    resultado = modelo.predict(dados_normalizados)[0]

    if resultado == 'Presence':
        st.error('⚠️ Alto risco de doença cardíaca detectado!')
    else:
        st.success('✅ Baixo risco de doença cardíaca.')