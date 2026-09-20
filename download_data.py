from pathlib import Path
import gzip
import shutil
from urllib.request import urlretrieve

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent / "data"
OUTPUT_FILE = DATA_DIR / "hillstrom.csv"

# Original public source released for the MineThatData challenge.
PRIMARY_URL = (
    "http://www.minethatdata.com/"
    "Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv"
)

# Public mirror used only if the original host does not respond.
FALLBACK_URL = (
    "https://hillstorm1.s3.us-east-2.amazonaws.com/"
    "hillstorm_no_indices.csv.gz"
)


def download_hillstrom():
    DATA_DIR.mkdir(exist_ok=True)

    if OUTPUT_FILE.exists():
        print(f"Dataset already exists: {OUTPUT_FILE}")
        return

    try:
        print("Downloading from the original MineThatData source...")
        urlretrieve(PRIMARY_URL, OUTPUT_FILE)
    except Exception:
        print("Original source did not respond. Trying the public mirror...")
        gz_path = DATA_DIR / "hillstrom.csv.gz"
        urlretrieve(FALLBACK_URL, gz_path)

        with gzip.open(gz_path, "rb") as source, open(OUTPUT_FILE, "wb") as target:
            shutil.copyfileobj(source, target)

        gz_path.unlink(missing_ok=True)

    # A quick check so I know I downloaded the expected file.
    df = pd.read_csv(OUTPUT_FILE)

    expected_columns = {
        "recency",
        "history_segment",
        "history",
        "mens",
        "womens",
        "zip_code",
        "newbie",
        "channel",
        "segment",
        "visit",
        "conversion",
        "spend",
    }

    if len(df) != 64000 or not expected_columns.issubset(df.columns):
        OUTPUT_FILE.unlink(missing_ok=True)
        raise ValueError("The downloaded file does not look like the Hillstrom dataset.")

    print(f"Saved {len(df):,} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    download_hillstrom()
