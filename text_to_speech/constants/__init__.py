import os 
from datetime import datetime

def get_current_time():
    fmt = "%Y-%m-%d %H%M%S"
    return f"{datetime.now().strftime(fmt)}"


ROOT_DIR = os.getcwd()
CONFIG_FOLDERNAME = "config"
CONFIG_FILENAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FOLDERNAME, CONFIG_FILENAME)

CURRENT_TIME_STAMP = get_current_time()

# Application configuration
APP_KEY = "application_config"
APPLICATION_NAME = "app_name"
ARTIFACT_DIR_KEY = "artifact_dir"
AUDIO_DIR = "audio_dir"
TEXT_DIR = "text_dir"
TEXT_FILENAME = "input_texts.txt"
