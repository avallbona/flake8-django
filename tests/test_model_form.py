from .utils import run_check, load_fixture_file


def test_model_form_doesnt_set_exclude_fails():
    code = load_fixture_file('model_form_exclude.py')
    result = run_check(code)
    assert len(result) == 2
    assert 'DJ06' in result[0][2]
    assert 'DJ06' in result[1][2]


def test_model_form_doesnt_set_exclude_success():
    code = load_fixture_file('model_form_fields.py')
    result = run_check(code)
    assert len(result) == 0


def test_model_form_doesnt_set_fields_dunder_all():
    code = load_fixture_file('model_form_fields_all.py')
    result = run_check(code)
    assert len(result) == 2
    assert 'DJ07' in result[0][2]
    assert 'DJ07' in result[1][2]
