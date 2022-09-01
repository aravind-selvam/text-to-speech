from text_to_speech.logging import logger
from text_to_speech.exception import TTSException
import sys

def get_accent_message():
    try:
        accent = ['1) Australian ', '2) American', '3) British',
                '4) Indian', '5) Canadian', '6) Irish', '7) Spanish']
        return accent
    except Exception as e:
        raise TTSException(e, sys)from e


def get_accent_tld(user_input):
    try:
        accent_input = {
            'Australian': 1,
            'American': 2,
            'British': 3,
            'Indian': 4,
            'Canadian': 5,
            'Irish': 6,
            'Spanish': 7
        }
        number = accent_input.get(user_input)
        # Map the input
        accent_map = {
            1: 'com.au',
            2: 'com',
            3: 'co.uk',
            4: 'co.in',
            5: 'ca',
            6: 'ie',
            7: 'es'
        }
        # Write function to return accent code
        if number in accent_map:
            return accent_map[number]
        else:
            pass
    except Exception as e:
        raise TTSException(e, sys) from e
