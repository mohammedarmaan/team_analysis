# Premier League Team Analytics Dashboard

Real-time analytics dashboard for Premier League teams using ESPN API data.

## Features

- Live team statistics and standings
- Win/Loss/Draw distribution visualization
- Home vs Away performance comparison
- Auto-refreshing data (5-minute cache)

## Tech Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas
- **API**: ESPN Soccer API

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## How It Works

1. `teametl.py` - Fetches team data from ESPN API
2. `app.py` - Streamlit dashboard with interactive charts
3. Data refreshes every 5 minutes automatically

## Current Configuration

Default team: Manchester City (ID: 382)

To change teams, modify the `team_id` variable in `app.py`.
