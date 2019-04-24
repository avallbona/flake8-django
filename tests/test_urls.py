import pytest

from .utils import run_check


def test_url_name_with_dash_fails():
    code = "url(name='test-1')"
    result = run_check(code)
    assert len(result) == 1
    assert 'DJ04' in result[0][2]


def test_url_name_with_underscore_sucess():
    code = "url('/test/', View.as_view(), name='test_1')"
    result = run_check(code)
    assert len(result) == 0


def test_url_include_without_namespace_fails():
    code = "url('/test/', include())"
    result = run_check(code)
    assert len(result) == 1
    assert 'DJ05' in result[0][2]


@pytest.mark.parametrize('code', [
    "url('/test/', include('test', namespace='test'))",
    "url('/test/', includes('test2', namespace='test-2'))"
])
def test_url_include_with_namespace_success(code):
    result = run_check(code)
    assert len(result) == 0
