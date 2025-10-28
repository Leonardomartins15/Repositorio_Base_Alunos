import streamlit as st
st.sidebar.title("Aluguel de Carros")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha o carro ideal para você!")
carros = ["Gol", "BMW", "Corsa", "Toro"]

opcao = st.sidebar.selectbox("Escolha o carro que foi alugado", carros)

st.title('Leonardo Motors - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

### Copia daqui pra frente --- Define a diária
if opcao == 'Gol':
    diaria = 350

elif opcao == 'BMW':
    diaria = 700

elif opcao == 'Corsa':
    diaria = 150

elif opcao == 'Toro':
    diaria = 450

### calcular

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. valor total a pagar é R${aluguel_total:.2f}')
    
