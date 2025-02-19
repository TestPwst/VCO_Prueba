import unittest

def load_tests(loader, tests, pattern):
    # Filtra archivos que no sean pruebas
    excluded_files = {"__init__.py", "FuncionesGral.py", "VariablesGral.py"}
    filtered_tests = [t for t in tests if t._testMethodName not in excluded_files]
    return unittest.TestSuite(filtered_tests)
