from scripts.utils.diagnostics import diagnostics

def test_diagnostics_return_type():
    result = diagnostics()
    assert isinstance(result, dict)
    
def test_python_version_exists():
    result = diagnostics()
    assert "python_version" in result
    
def test_platform_exists():
    result = diagnostics()
    assert "platform" in result