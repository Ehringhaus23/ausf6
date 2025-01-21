import requests
import os
import yaml

def main():
    url = 'https://api.start.gg/gql/alpha'
    # API query to pull the most recent 3 tourneys for street fighter in Victoria, Australia
    graphql_query = {
        "query": """
        query TournamentsByVideogameAndState($perPage: Int!, $videogameId: ID!, $state: String!) {
            tournaments(query: {
                perPage: $perPage,
                page: 1,
                sortBy: "startAt desc",
                filter: {
                    past: false,
                    videogameIds: [$videogameId],
                    addrState: $state
                }
            }) {
                nodes {
                    id
                    name
                    addrState
                    slug
                }
            }
        }
        """,
        "variables": {
            "perPage": 3, 
            "videogameId": 43868, # SF6 id 
            "state": "VIC"
        }
    }

    

    with open('api_key.yaml') as f:
        dict = yaml.safe_load(f)
        
    # Replace <key> with your actual API token
    api_token = dict['key']
    headers = {'Authorization': f'Bearer {api_token}'}

    try:
        response = requests.post(url=url, json=graphql_query, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx

        # Print the response for debugging
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print(f"Failed to decode JSON response: {response.text}")

if __name__ == '__main__':
    main()