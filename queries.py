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