from githubkit import GitHub


def test_github_api_endpoint():
    g = GitHub(base_url="https://api.github.com")
    assert g.graphql._get_graphql_endpoint() == "/graphql"


def test_ghes_api_endpoint():
    g = GitHub(base_url="https://example.github.com/api/v3")
    assert g.graphql._get_graphql_endpoint() == "https://example.github.com/api/graphql"
