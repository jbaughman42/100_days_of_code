import pytest

from day_three_love_calculator import check_letters, love_score

love_score_data = [
    (("Adam", "Jim"), "Your score is 0; you go together like Coke and Mentos."),
    (("Tru", "Vasco"), "Your score is 32; you figure it out!"),
    (("True", "Vasco"), "Your score is 43; you're alright together."),
]


def test_check_letters():
    assert check_letters("Jen", "Mark", "TRUE") == 2


# TODO: break the setup into a fixture
@pytest.mark.parametrize("test_input, expected", love_score_data)
def test_love_score(test_input, expected):
    name_1, name_2, = test_input
    true = check_letters(name_1, name_2, "TRUE")
    love = check_letters(name_1, name_2, "LOVE")
    assert love_score(true, love) == expected
