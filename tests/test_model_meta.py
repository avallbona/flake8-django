from .utils import run_check, load_fixture_file


def test_model_without_meta_fails():
    code = load_fixture_file('model_without_meta.py')
    result = run_check(code)
    assert len(result) == 1
    assert 'DJ09' in result[0][2]


def test_model_with_meta_success():
    code = load_fixture_file('model_with_meta.py')
    result = run_check(code)
    assert len(result) == 0


def test_model_wit_meta_without_verbose_name_fails():
    code = load_fixture_file('model_with_meta_without_verbose_name.py')
    result = run_check(code)
    assert len(result) == 2
    assert 'DJ10' in result[0][2]
    assert 'DJ11' in result[1][2]
