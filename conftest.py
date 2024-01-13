def pytest_addoption(parser):
    parser.addoption("--context", default="local_real", help="Specify context")
