# app.py
import streamlit as st
import plotly.express as px
from teametl import extract_team_data
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Team Analytics",
    layout="wide"
)

# Streamlit caching - fetches fresh data every 5 minutes
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_team_data(team_id):
    return extract_team_data(team_id)

# Load data
team_id = "382"  # Manchester City
df = load_team_data(team_id)

if df is not None:
    st.title(f"{df['displayName'].values[0]} Analytics")
    # st.dataframe(df)
    
    # Display key metrics
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric("Games Played", int(df['gamesPlayed'].values[0]))
    col2.metric("Wins", int(df['wins'].values[0]))
    col3.metric("Losses", int(df['losses'].values[0]))
    col4.metric("Ties", int(df["ties"].values[0]))
    col5.metric("Rank", int(df['rank'].values[0]), 
            int(df['rankChange'].values[0]))    
    col6.metric("Points", int(df['points']))


    col1, col2 = st.columns(2)

    with col1:
        
        st.subheader("Overview")
        st.metric("Points per game", int(df['points'].values[0])/int(df['gamesPlayed'].values[0]))
        st.metric("Goal difference", int(df['pointsFor'].values[0]) - int(df['pointsAgainst'].values[0]))
        # st.metric("Losses", int(df['losses'].values[0]))
        # st.metric("Ties", int(df["ties"].values[0]))

    with col2:
    
        result_data = {
            'Result': ['Wins', 'Losses', 'Draws'],
            'Value': [df['wins'].values[0], df['losses'].values[0], df['ties'].values[0]]
        }
        color_map = {
            'Wins': '#2ecc71',    # green
            'Losses': '#e74c3c',  # red
            'Draws': '#95a5a6'    # gray
        }

        fig  = px.pie(result_data, values = 'Value', names = 'Result', title="Games result distribution", color='Result', color_discrete_map=color_map)
        
        st.plotly_chart(fig)

    
    home_away_data = {
    'Metric': ['games played', 'Wins', 'Losses', 'Ties', 'Goals Scored', 'Goals Conceded'],
    'Home': [
        int(df['homeGamesPlayed'].values[0]),
        int(df['homeWins'].values[0]),
        int(df['homeLosses'].values[0]),
        int(df['homeTies'].values[0]),
        int(df['homePointsFor'].values[0]),
        int(df['homePointsAgainst'].values[0])
    ],
    'Away': [
        int(df['awayGamesPlayed'].values[0]),
        int(df['awayWins'].values[0]),
        int(df['awayLosses'].values[0]),
        int(df['awayTies'].values[0]),
        int(df['awayPointsFor'].values[0]),
        int(df['awayPointsAgainst'].values[0])
        ]
    }

    comparison_df = pd.DataFrame(home_away_data)

    # Create grouped bar chart
    fig = go.Figure(data=[
        go.Bar(
            name='Home',
            x=comparison_df['Metric'],
            y=comparison_df['Home'],
            marker_color='#3498db',  # Blue for home
            text=comparison_df['Home'],
            textposition='auto'
        ),
        go.Bar(
            name='Away',
            x=comparison_df['Metric'],
            y=comparison_df['Away'],
            marker_color='#e74c3c',  # Red for away
            text=comparison_df['Away'],
            textposition='auto'
        )
    ])

    # Update layout
    fig.update_layout(
        title='Home vs Away Performance',
        xaxis_title='Metrics',
        yaxis_title='Count',
        barmode='group',
        height=500,
        hovermode='x unified'
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Failed to load team data")