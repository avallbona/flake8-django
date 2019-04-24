from .utils import run_check


def test_render_doesnt_use_locals_fails():
    code = "render(request, 'template.html', locals())"
    result = run_check(code)
    assert len(result) == 1
    assert 'DJ03' in result[0][2]


def test_render_doesnt_use_locals_success():
    code = "render(request, 'template.html', {'test': 'test'})"
    result = run_check(code)
    assert len(result) == 0
