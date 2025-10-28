import streamlit as st

# Gêneros musicais disponíveis
generos_musical = ["Rap", "Funk", "Trap"]

# Artistas por gênero
artistas_por_genero = {
    "Rap": ["Racionais", "50 Cent"],
    "Funk": ["MC Hariel", "MC IG"],
    "Trap": ["Veigh", "Felipe Ret", "Matuê"]
}

# Vídeos por artista
videos_por_artista = {
    "Racionais": "https://youtu.be/VDYRbLOdTAI?si=AJSTCV0V2foNUhnE",
    "50 Cent": "https://youtu.be/L9rJ0vwBisE?si=SbgTOKdvNdHOI1L5",
    "MC Hariel": "https://youtu.be/8miyvWwDnUA?si=BAXe-rkWEf0A6L-e",
    "MC IG": "https://youtu.be/wWl6AufVWS8?si=4luZu_HKjrL5udf8",
    "Veigh": "https://youtu.be/h3jebyHaDrY?si=PAwhTaUyEj5Sln2T",
    "Felipe Ret": "https://youtu.be/DBV_6F0GCcM?si=0MP6Q8aVPnnLNhlC",
    "Matuê": "https://youtu.be/LSAuLm-uZ2g?si=ATCiJ9mF4YslhYiw"
}

# Interface lateral
st.sidebar.image("logo.png")
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos_musical)

# Escolha do artista e exibição do vídeo
if genero_selecionado:
    artistas_disponiveis = artistas_por_genero[genero_selecionado]
    artista_selecionado = st.sidebar.selectbox("Selecione o artista:", artistas_disponiveis)

    if artista_selecionado:
        st.title(f"{artista_selecionado}")
        st.video(videos_por_artista[artista_selecionado])