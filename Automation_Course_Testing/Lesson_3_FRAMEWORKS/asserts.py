def test_input_text(expected_result, actual_result):
    a = f"expected {expected_result}, got {actual_result}"
    assert actual_result == expected_result, a



test_input_text(21, 11)