import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title='Análise de Futebol', page_icon=':soccer:', layout='wide')

# Adiciona o CSS diretamente no app
st.markdown(
    """
    <style>
    .st-emotion-cache-1dp5vir {
        background-image: linear-gradient(90deg, #A8F841, #2B3749) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar os dados de partidas e jogadores
matches_df = pd.read_csv('matchess.csv', delimiter=';')
players_df = pd.read_csv('playerss.csv')

# Filtrar os dados de partidas
matches_df = matches_df[(matches_df['status'] != 'incomplete') & (matches_df['status'] != 'suspended')]

# Criar listas de times e jogadores únicos
times = sorted(list(set(matches_df['home_team_name']).union(set(matches_df['away_team_name']))))
jogadores = sorted(list(set(players_df['full_name'])))

# Caixa de seleção para alternar entre análise de times e jogadores
opcao_analise = st.sidebar.selectbox('Escolha o tipo de análise', ['Time', 'Jogador'])

if opcao_analise == 'Time':
    # Análise de Times
    time_selecionado = st.sidebar.selectbox('Selecione um time para analisar', times)

    # Filtrar os dados para o time selecionado
    dados_time_casa = matches_df[matches_df['home_team_name'] == time_selecionado]
    dados_time_fora = matches_df[matches_df['away_team_name'] == time_selecionado]

    # Estatísticas do time
    gols_casa = dados_time_casa['home_team_goal_count'].sum()
    gols_fora = dados_time_fora['away_team_goal_count'].sum()
    total_gols = gols_casa + gols_fora
    total_partidas = len(dados_time_casa) + len(dados_time_fora)

    # Estatísticas adicionais
    total_chutes_ao_gol = dados_time_casa['home_team_shots_on_target'].sum() + dados_time_fora['away_team_shots_on_target'].sum()
    total_escanteios = dados_time_casa['home_team_corner_count'].sum() + dados_time_fora['away_team_corner_count'].sum()
    media_posse_bola = (dados_time_casa['home_team_possession'].mean() + dados_time_fora['away_team_possession'].mean()) / 2

    # Exibir estatísticas gerais do time
    st.title(f'Estatísticas do Time: {time_selecionado}')
    st.write(f'Total de Partidas: {total_partidas}')
    st.write(f'Total de Gols: {total_gols}')
    st.write(f'Total de Chutes ao Gol: {total_chutes_ao_gol}')
    st.write(f'Total de Escanteios: {total_escanteios}')
    st.write(f'Posse de Bola Média: {media_posse_bola:.2f}%')

    # Configurando o estilo global dos gráficos
    backgroundColor = st.get_option('theme.backgroundColor')
    textColor = st.get_option('theme.textColor')
    accentColor = '#A8F841'
    accentColor2 = '#49499e'

    plt.rcParams['figure.facecolor'] = backgroundColor  # Fundo da figura
    plt.rcParams['axes.facecolor'] = backgroundColor  # Fundo dos eixos
    plt.rcParams['axes.labelcolor'] = textColor  # Cor dos rótulos dos eixos
    plt.rcParams['xtick.color'] = textColor  # Cor dos ticks do eixo X
    plt.rcParams['ytick.color'] = textColor  # Cor dos ticks do eixo Y
    plt.rcParams['text.color'] = textColor  # Cor dos textos em geral
    plt.rcParams['axes.edgecolor'] = textColor  # Cor das bordas dos eixos
    plt.rcParams['legend.facecolor'] = backgroundColor  # Fundo da legenda
    plt.rcParams['legend.edgecolor'] = textColor  # Cor da borda da legenda
    
    # Gráficos de gols e chutes ao gol por partida
    col1, col2 = st.columns(2)
    with col1:
        st.write(f'Gols por Partida do {time_selecionado}')
        fig, ax = plt.subplots()
        
        ax.bar(dados_time_casa['home_team_name'] + ' x ' + dados_time_casa['away_team_name'], 
            dados_time_casa['home_team_goal_count'], label='Em Casa', color=accentColor2)
        ax.bar(dados_time_fora['home_team_name'] + ' x ' + dados_time_fora['away_team_name'], 
            dados_time_fora['away_team_goal_count'], label='Fora', color=accentColor)

        plt.xticks(rotation=90)
        ax.legend()
        st.pyplot(fig)

    with col2:
        st.write(f'Chutes ao Gol por Partida do {time_selecionado}')
        fig, ax = plt.subplots()
        ax.bar(dados_time_casa['home_team_name'] + ' x ' + dados_time_casa['away_team_name'], dados_time_casa['home_team_shots_on_target'], label='Em Casa', color=accentColor2)
        ax.bar(dados_time_fora['home_team_name'] + ' x ' + dados_time_fora['away_team_name'], dados_time_fora['away_team_shots_on_target'], label='Fora', color=accentColor)
        plt.xticks(rotation=90)
        ax.legend()
        st.pyplot(fig)

    col3, col4 = st.columns(2)
    with col3:
        st.write(f'Escanteios por Partida do {time_selecionado}')
        fig, ax = plt.subplots()
        ax.bar(dados_time_casa['home_team_name'] + ' x ' + dados_time_casa['away_team_name'], dados_time_casa['home_team_corner_count'], label='Em Casa', color=accentColor2)
        ax.bar(dados_time_fora['home_team_name'] + ' x ' + dados_time_fora['away_team_name'], dados_time_fora['away_team_corner_count'], label='Fora de Casa', color=accentColor)
        ax.set_ylabel('Número de Escanteios')
        ax.set_title(f'Escanteios por Partida do {time_selecionado}')
        plt.xticks(rotation=90)
        ax.legend()
        st.pyplot(fig)

    with col4:
    # Gráfico de Pizza para Posse de Bola Média
        st.write(f'Posse de Bola Média do {time_selecionado}')
        explode = (0.1, 0)
        fig, ax = plt.subplots()
        ax.pie([media_posse_bola, 100 - media_posse_bola], labels=['Posse de Bola', 'Oponente'], autopct='%1.1f%%', colors=[accentColor2, accentColor], explode=explode, shadow=True)
        ax.set_title(f'Posse de Bola Média do {time_selecionado}')
        st.pyplot(fig)


    

    
elif opcao_analise == 'Jogador':
    # Análise de Jogadores
    jogador_selecionado = st.sidebar.selectbox('Selecione um jogador para analisar', jogadores)

    # Filtrar os dados para o jogador selecionado
    dados_jogador = players_df[players_df['full_name'] == jogador_selecionado]

    # Estatísticas do jogador
    gols = dados_jogador['goals_overall'].sum()
    assistencias = dados_jogador['assists_overall'].sum()
    partidas = dados_jogador['sm_matches_recorded_total_overall'].sum()
    posicoes = dados_jogador['position'].unique()
    # Estatísticas adicionais
    chutes_ao_gol = dados_jogador['shots_on_target_total_overall'].sum()
    yellow_cards = dados_jogador['yellow_cards_overall'].sum()
    red_cards = dados_jogador['red_cards_overall'].sum()
    right_passes = dados_jogador['passes_completed_total_overall'].sum()
    duelos_aereos = dados_jogador['aerial_duels_won_total_overall'].sum()
    penalty_goals = dados_jogador['penalty_goals'].sum()
    penalty_misses = dados_jogador['penalty_misses'].sum()

    # Exibir estatísticas gerais do jogador
    st.title(f'Estatísticas do Jogador: {jogador_selecionado}')
    st.write(f'Total de Partidas: {partidas}')
    st.write(f'Total de Gols: {gols}')
    st.write(f'Total de Assistências: {assistencias}')
    st.write(f'Total de Chutes ao Gol: {chutes_ao_gol}')
    st.write(f'Posição: {posicoes}')
    st.write(f'Cartões Amarelos: {yellow_cards}')
    st.write(f'Cartões Vermelhos: {red_cards}')
    st.write(f'Passes Certos: {right_passes}')
    st.write(f'Duelos Aéreos Vencidos: {duelos_aereos}')
    st.write(f'Gols de Pênalti: {penalty_goals}')
    st.write(f'Pênaltis Perdidos: {penalty_misses}')

    if 'Goalkeeper' in posicoes:
        saves = dados_jogador['saves_total_overall'].sum()  # Supondo que você tenha essa coluna 'saves_overall'
        st.write(f'Total de Defesas: {saves}')
    
