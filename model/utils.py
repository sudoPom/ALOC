def extract_key(kwargs, key, default):
    return kwargs.get(key, default)


def throw_if_no_keys_found(kwargs, expected_keys):
    assert any(
        key in kwargs for key in expected_keys), f"Expected at least one of the following keys: {expected_keys}"
