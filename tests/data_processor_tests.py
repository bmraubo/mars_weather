import pytest
import app.data_processor as dp


def test_data_processor_initialise():
    weather_data = {
        "date": None,
        "time": None,
        "mission_sol": None,
        "max_temp": None,
        "min_temp": None,
    }

    data_processor = dp.DataProcessor()

    assert data_processor.weather_data == weather_data
