import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from app.main import data_location


def test_dataLocation():
    assert data_location == "C:\\Users\\shahs\\Documents\\az_suicide_data_visualization\\data"