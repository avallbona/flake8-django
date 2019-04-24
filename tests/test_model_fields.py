import pytest

from flake8_django.checkers.model_fields import NOT_BLANK_TRUE_FIELDS, NOT_NULL_TRUE_FIELDS

from .utils import run_check


@pytest.mark.parametrize('field_type', NOT_NULL_TRUE_FIELDS)
def test_not_null_fields_fails(field_type):
    code = "field = models.{}(null=True)".format(field_type)
    result = run_check(code)
    assert len(result) == 1
    assert 'DJ01' in result[0][2]


@pytest.mark.parametrize('field_type', NOT_NULL_TRUE_FIELDS)
def test_not_null_fields_success(field_type):
    code = "field = models.{}()".format(field_type)
    result = run_check(code)
    assert len(result) == 0


@pytest.mark.parametrize('field_type', NOT_BLANK_TRUE_FIELDS)
def test_not_blank_fields_fails(field_type):
    code = "another_field = models.{}(blank=True)".format(field_type)
    result = run_check(code)
    assert len(result) == 1
    assert 'DJ02' in result[0][2]


@pytest.mark.parametrize('field_type', NOT_BLANK_TRUE_FIELDS)
def test_not_blank_fields_sucess(field_type):
    code = "another_field = models.{}()".format(field_type)
    result = run_check(code)
    assert len(result) == 0
