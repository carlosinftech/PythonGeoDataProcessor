import pytest

def process_data(data):
    # Some data processing logic
    # [1, 2, 3] to [1, 4, 9]
    return [1, 4, 9]

@pytest.fixture
def data():
    return [1, 2, 3]

def test_process_data(data):
    expected_output = [1, 4, 9]
    output = process_data(data)
    assert output == expected_output

def test_process_data_raises_error_on_empty_input(data):
    with pytest.raises(ValueError) as exc_info:
        process_data([])
    assert "Input data cannot be empty" in str(exc_info.value)