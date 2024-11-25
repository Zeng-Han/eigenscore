import getpass
import os
import sys

__USERNAME = getpass.getuser()
_BASE_DIR = f'/mnt/f7a57ea9-f9b0-4806-966e-7f21cbc76421/zenghan/eigenscore_base'
MODEL_PATH = f'/mnt/f7a57ea9-f9b0-4806-966e-7f21cbc76421/zenghan'
DATA_FOLDER = os.path.join(_BASE_DIR, 'datasets')
GENERATION_FOLDER = os.path.join(_BASE_DIR, 'output')
os.makedirs(GENERATION_FOLDER, exist_ok=True)

DEVICE_MAP = "balanced_low_0"

