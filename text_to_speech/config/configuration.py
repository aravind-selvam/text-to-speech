import os 
import sys
from text_to_speech.logging import logger
from text_to_speech.exception import TTSException
from text_to_speech.entity.config_entity import *
from text_to_speech.constants import *
from text_to_speech.utils.utils import read_yaml_file


class TTSconfig:
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH,
                 current_time_stamp:str = CURRENT_TIME_STAMP
        ) -> None:
        try:
            self.config_info = read_yaml_file(file_path= config_file_path)
        except Exception as e:
            raise TTSException(e, sys)from e 
    
    def get_app_config(self) ->App_config:
        try:
            application_config = self.config_info[APP_KEY]
            app_name = application_config[APPLICATION_NAME]
            artifact_key = application_config[ARTIFACT_DIR_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                        app_name,
                                        artifact_key
                                        )
            audio_dir = os.path.join(artifact_dir, 
                                     application_config[AUDIO_DIR]
                                     )
            os.makedirs(audio_dir, exist_ok=True)
            
            text_dir = os.path.join(artifact_dir,
                                    application_config[TEXT_DIR]
                                    )
            
            os.makedirs(text_dir, exist_ok=True)

            
            application_config = App_config(artifact_dir=artifact_dir,
                                            app_name=app_name,
                                            audio_dir= audio_dir, 
                                            text_dir=text_dir
                                            )
            return application_config
        except Exception as e:
            raise TTSException(e, sys)from e
        
            
            