import streamlit as st
import pandas as pd
import plotly.express as px

# === CONFIGURATION ===
st.set_page_config(
    page_title="DataPulse 🎵",
    page_icon="🎵",
    layout="wide"
)

# === CHARGEMENT DES DONNÉES ===
@st.cache_data
def load_data():
    df = pd.read_csv('data/clean/spotify_clean.csv')
    return df

df = load_data()

# === EN-TÊTE ===
st.title("🎵 DataPulse — Analyse Spotify")
st.markdown("Exploration interactive des tendances musicales · 89 740 morceaux")
st.divider()

# === MÉTRIQUES ===
col1, col2, col3, col4 = st.columns(4)
col1.metric("🎵 Morceaux", f"{len(df):,}")
col2.metric("🎤 Artistes", f"{df['artists'].nunique():,}")
col3.metric("🎸 Genres", df['track_genre'].nunique())
col4.metric("⭐ Popularité moy.", f"{df['popularity'].mean():.1f}/100")

st.divider()

# === SIDEBAR FILTRES ===
st.sidebar.header("🎛️ Filtres")

genres = st.sidebar.multiselect(
    "Genres",
    options=sorted(df['track_genre'].unique()),
    default=[]
)

popularity_range = st.sidebar.slider(
    "Popularité", 0, 100, (0, 100)
)

energy_range = st.sidebar.slider(
    "Énergie", 0.0, 1.0, (0.0, 1.0)
)

# Appliquer les filtres
df_f = df[
    (df['popularity'] >= popularity_range[0]) &
    (df['popularity'] <= popularity_range[1]) &
    (df['energy'] >= energy_range[0]) &
    (df['energy'] <= energy_range[1])
]
if genres:
    df_f = df_f[df_f['track_genre'].isin(genres)]

st.sidebar.info(f"📊 {len(df_f):,} morceaux affichés")

# === GRAPHIQUE 1 : Top 10 genres ===
st.subheader("🏆 Top 10 genres les plus populaires")
top_genres = (df_f.groupby('track_genre')['popularity']
              .mean().nlargest(10).reset_index()
              .sort_values('popularity'))
fig1 = px.bar(top_genres, x='popularity', y='track_genre',
              orientation='h', color='popularity',
              color_continuous_scale='Viridis')
st.plotly_chart(fig1, use_container_width=True)

# === GRAPHIQUE 2 : Énergie vs Popularité ===
st.subheader("⚡ Énergie vs Popularité")
fig2 = px.scatter(
    df_f.sample(min(3000, len(df_f))),
    x='energy', y='popularity',
    color='valence', color_continuous_scale='RdYlGn',
    hover_data=['track_name', 'artists', 'track_genre'],
    opacity=0.6
)
st.plotly_chart(fig2, use_container_width=True)

# === GRAPHIQUE 3 : Danceability vs Valence ===
st.subheader("💃 Danceability vs Valence")
fig3 = px.scatter(
    df_f.sample(min(3000, len(df_f))),
    x='danceability', y='valence',
    color='track_genre',
    hover_data=['track_name', 'artists'],
    opacity=0.5
)
st.plotly_chart(fig3, use_container_width=True)

# === TABLEAU ===
with st.expander("📋 Voir les données"):
    st.dataframe(
        df_f[['track_name', 'artists', 'track_genre',
              'popularity', 'energy', 'danceability', 'valence']]
        .sort_values('popularity', ascending=False)
        .head(100),
        use_container_width=True
    )