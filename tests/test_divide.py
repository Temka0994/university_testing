import pytest
from main import divide


def test_divide_positive():
    assert divide(10, 2) == 5


def test_divide_negative():
    assert divide(-10, 2) == -5


@pytest.fixture
def sample_data():
    return [
        (10, 2, 5),
        (20, 4, 5),
        (-9, 3, -3),
    ]


@pytest.mark.parametrize("a,b,expected", [
    (6, 2, 3),
    (15, 3, 5),
    (0, 1, 0),
])
def test_divide_parametrize(a, b, expected):
    assert divide(a, b) == expected


def test_divide_with_fixture(sample_data):
    for a, b, expected in sample_data:
        assert divide(a, b) == expected


def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.skip(reason="Функція ще не реалізована")
def test_future_feature():
    assert divide(10, 5) == 2


@pytest.mark.xfail(reason="Очікуємо помилку через відому проблему")
def test_known_bug():
    assert divide(10, 2) == 6


def test_fail_example():
    assert divide(10, 2) == 100
