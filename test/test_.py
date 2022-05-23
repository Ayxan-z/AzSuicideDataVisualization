import sys
import os.path
import pandas as pd
import plotly.express as px
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from app.main import data_location, lineGraph


def test_dataLocation():
    assert data_location == "C:\\Users\\shahs\\Documents\\az_suicide_data_visualization\\data"
