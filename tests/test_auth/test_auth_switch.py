from githubkit import GitHub, UnauthAuthStrategy


def test_auth_switch(g: GitHub):
    new_auth = UnauthAuthStrategy()

    new_g = g.with_auth(new_auth)
    assert new_g.auth is new_auth
    assert new_g.config == g.config
