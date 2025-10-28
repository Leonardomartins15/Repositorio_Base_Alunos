import streamlit as st

st.sidebar.title("EliteCarros")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha o carro ideal para você!")

carros = [
    "Fiat Strada", "Volkswagen Polo", "Chevrolet Onix", "Hyundai HB20", "Fiat Argo",
    "Volkswagen T-Cross", "Chevrolet Tracker", "Fiat Mobi", "Renault Kwid", "Hyundai Creta",
    "BMW X1", "Volvo EX30", "BMW Série 3", "Porsche Cayenne", "Volvo XC60",
    "Mercedes-Benz GLB", "BMW X2", "Audi Q3"
]

preco_carro = [
    111990, 93960, 94900, 90690, 82990, 119990, 119990, 68990, 58890,
    141890, 200000, 229995, 332950, 875955, 95000, 369900, 406950, 95000
]

# Cria um dicionário que associa cada carro ao seu preço
carros_dict = dict(zip(carros, preco_carro))

opcao = st.sidebar.selectbox("Escolha um carro", carros)

st.title('Elite Carros — Qualidade, Estilo e Performance')
st.image(f'{opcao}.png')

# Recupera o preço diretamente do dicionário
preco = carros_dict[opcao]
st.markdown(f'Você escolheu o carro: **{opcao}** e o preço dele é **R$ {preco:.2f}**')