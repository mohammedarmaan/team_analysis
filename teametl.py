# etl.py
import requests
import pandas as pd


def extract_team_data(team_id):

    url = f"https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/teams/{team_id}"
    
    try:
        response = requests.get(url)
        data = response.json()['team']
        
        # Extract basic info
        basic_info_fields = ['id', 'uid', 'slug', 'location', 'name', 
                            'nickname', 'abbreviation', 'displayName', 
                            'color', 'standingSummary']
        basic_info = {field: data[field] for field in basic_info_fields}
        
        # Extract team stats
        team_record = data['record']['items'][0]['stats']
        team_stats = {stat['name']: stat['value'] for stat in team_record}
        
        # Combine data
        team_data = basic_info | team_stats
        
        # Return as DataFrame
        return pd.DataFrame([team_data])
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None