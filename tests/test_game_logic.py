#FIX: sys.path patched so logic_utils can be imported from parent directory using Claude Code
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# ---------------------------------------------------------------------------
# check_guess — outcome and hint direction
# ---------------------------------------------------------------------------

def test_winning_guess():
    # check_guess returns a tuple; outcome must be "Win"
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

#FIX: Hint messages were swapped — Too High now says Go LOWER, Too Low says Go HIGHER using Claude Code
def test_too_high_hint_says_go_lower():
    # Bug fix: hint was previously "Go HIGHER!" when guess was too high
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # Bug fix: hint was previously "Go LOWER!" when guess was too low
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_win_message():
    _, message = check_guess(50, 50)
    assert "Correct" in message or "🎉" in message


# ---------------------------------------------------------------------------
# get_range_for_difficulty — ranges were swapped for Normal and Hard
# ---------------------------------------------------------------------------

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

#FIX: Normal and Hard ranges were swapped using Claude Code
def test_normal_range():
    # Bug fix: Normal was returning 1-100 (Hard's range)
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_hard_range():
    # Bug fix: Hard was returning 1-50 (Normal's range)
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_hard_range_wider_than_normal():
    # Hard should always be harder (wider range) than Normal
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_unknown_difficulty_returns_default():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


# ---------------------------------------------------------------------------
# update_score — off-by-one on win points
# ---------------------------------------------------------------------------

#FIX: Win score off-by-one removed — first guess win now correctly awards 90 points using Claude Code
def test_win_on_first_attempt_gives_90():
    # Bug fix: was returning 80 due to `100 - 10 * (attempt_number + 1)`
    score = update_score(0, "Win", attempt_number=1)
    assert score == 90

def test_win_on_second_attempt_gives_80():
    score = update_score(0, "Win", attempt_number=2)
    assert score == 80

def test_win_score_minimum_is_10():
    # Very late win should not drop below 10 points
    score = update_score(0, "Win", attempt_number=100)
    assert score == 10

def test_too_high_deducts_5():
    score = update_score(50, "Too High", attempt_number=1)
    assert score == 45

def test_too_low_deducts_5():
    score = update_score(50, "Too Low", attempt_number=1)
    assert score == 45

def test_score_accumulates():
    score = update_score(100, "Win", attempt_number=1)
    assert score == 190


# ---------------------------------------------------------------------------
# parse_guess — invalid inputs must not crash and must return ok=False
# ---------------------------------------------------------------------------

#FIX: Invalid inputs no longer bypass game-over check — attempts now correctly exhaust using Claude Code
def test_parse_empty_string():
    # Bug context: invalid inputs still incremented attempts; ensure they parse as not ok
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_none():
    ok, _, _ = parse_guess(None)
    assert ok is False

def test_parse_non_numeric():
    ok, value, _ = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_valid_integer():
    ok, value, _ = parse_guess("42")
    assert ok is True
    assert value == 42

def test_parse_decimal_truncates():
    ok, value, _ = parse_guess("7.9")
    assert ok is True
    assert value == 7
