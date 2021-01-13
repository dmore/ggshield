from ggshield.config import Cache

    api_key = os.getenv("TEST_GITGUARDIAN_API_KEY", "1234567890")
    base_uri = os.getenv("TEST_GITGUARDIAN_API_URL", "https://api.gitguardian.com")


@pytest.fixture(scope="session")
def cache() -> Cache:
    c = Cache()
    c.purge()
    return c