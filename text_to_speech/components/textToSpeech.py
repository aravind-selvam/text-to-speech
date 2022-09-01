import os
import sys
import base64
import datetime
from gtts import gTTS
from text_to_speech.constants import *
from text_to_speech.entity.config_entity import App_config
from text_to_speech.config.configuration import TTSconfig
from text_to_speech.logging import logger
from text_to_speech.exception import TTSException

class TTSapplication:
    """
    TTS application is a simple application for converting text to speech.
    It uses gTTS open source library to convert text to speech.
    """        
    def __init__(self, app_config=TTSconfig(), time_stamp=CURRENT_TIME_STAMP ):
        """
        Initialize the application
        """
        try:
            self.app_info = app_config.get_app_config()
            self.artifact_dir = self.app_info.artifact_dir
            self.audio_dir = self.app_info.audio_dir
            self.text_dir = self.app_info.text_dir
            
            logger.info(f"Loaded all application configurations")
        except Exception as e:
            raise TTSException(e,sys)from e
        
    def text2Speech(self, data, accent):
        """
        text2Speech
        
        Args:
            data (str): Give text data which has to be converted to speech
            accent (int): The accent input is given in tld format

        Returns:
            Encoded string of the audio
        """
        try:
            my_text = data
            
            text_dir = self.text_dir
            txt_filename = TEXT_FILENAME
            
            txt_file_path = os.path.join(text_dir, txt_filename)
            
            with open(txt_file_path, "a+") as file:
                file.write(f'\n{my_text}')
                
            # Create object for Text to speech
            tts = gTTS(text=my_text, lang='en', slow=False, tld=accent)
            
            audio_dir = self.audio_dir
            
            filename = f"converted_file_{CURRENT_TIME_STAMP}.mp3"
            
            audiopath = os.path.join(audio_dir, filename)
            
            # save tts object as mp3
            tts.save(audiopath)

            with open(audiopath, "rb") as file:
                my_string = base64.b64encode(file.read())
            return my_string
        except Exception as e:
            raise TTSException(e,sys)from e