def test_substring(full_string, substring):
    a = f"expected '{substring}' to be substring of '{full_string}'"
    assert substring in full_string, a


test_substring('text', 'some')
