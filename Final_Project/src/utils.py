from pathlib import Path
import pandas as pd

def load_cardio_data(path):
    """Load the original semicolon-separated cardiovascular CSV."""
    return pd.read_csv(Path(path), sep=";")

def add_engineered_features(df):
    """Return a copy with the project feature-engineering fields."""
    data = df.copy()
    data["bmi"] = data["weight"] / ((data["height"] / 100) ** 2)
    data["pulse_pressure"] = data["ap_hi"] - data["ap_lo"]
    return data
