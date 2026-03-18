"""
Configuration and Settings Loader
Loads environment variables and provides configuration to the bot
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

def load_config():
    """
    Load configuration from environment variables
    Returns a dictionary with all settings
    """
    config = {
        'tidal': {
            'session_file': os.getenv('TIDAL_SESSION_FILE', '.tidal_session'),
        },
        'bot': {
            'name': os.getenv('BOT_NAME', 'TidalMusicBot'),
            'log_level': os.getenv('LOG_LEVEL', 'INFO'),
        },
        'schedule': {
            'interval': int(os.getenv('PLAYLIST_CHECK_INTERVAL', '3600')),
            'times': os.getenv('STREAM_SCHEDULE', '09:00,14:00,21:00').split(','),
            'shuffle': os.getenv('SHUFFLE_SONGS', 'true').lower() == 'true',
        }
    }
    return config

def get_session_file():
    """Get the path to the Tidal session file"""
    return os.getenv('TIDAL_SESSION_FILE', '.tidal_session')

def get_log_level():
    """Get the logging level"""
    return os.getenv('LOG_LEVEL', 'INFO')