import pytest

run = False


@pytest.mark.smoke
@pytest.mark.skip(reason="JIRA-123")
def test_example_one():
    assert 0


@pytest.mark.regress
@pytest.mark.skipif("not run")
def test_example_two():
    assert 0


@pytest.mark.regress
@pytest.mark.xfail(run=False)
def test_example_three():
    assert True


@pytest.mark.regress
@pytest.mark.xfail(strict=True)
def test_example_four():
    assert True


@pytest.mark.auth
def test_example_five():
    pass


@pytest.mark.only
def test_example_five():
    pass