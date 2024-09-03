import logging
import os

class ConfirmationLogger:
    def __init__(self, log_path):
        self.log_path = log_path
        self.filename = None
        self.logger = logging.getLogger('CustomLogger')
        self.logger.setLevel(logging.DEBUG)
        self.initial_log_written = False
        self.confirmation_counter = 1
        self.log_file = None
        self.fh = None
        
    def _check_initial_log_written(self):
        if not os.path.exists(self.log_file):
            return False
        with open(self.log_file, 'r') as file:
            content = file.read()
            if '.RAW_IMAGE_DIRECTORY' in content and '.CONFIRMATION_RES_IMAGE_DIRECTORY' in content and '.CONFIRMATION_LIST' in content:
                return True
        return False
    
    def _get_initial_confirmation_counter(self):
        if not os.path.exists(self.log_file):
            return 1
        with open(self.log_file, 'r') as file:
            content = file.read()
            conf_lines = [line for line in content.split('\n') if line.startswith('CONF')]
            return len(conf_lines) + 1
    
    def log_name(self, name):
        self.filename = name
        self.log_file = f"{self.log_path}/{self.filename}.txt"
        
        # Ensure the directory exists
        os.makedirs(self.log_path, exist_ok=True)
        
        if self.fh:  # Remove the old file handler if it exists
            self.logger.removeHandler(self.fh)
        
        self.fh = logging.FileHandler(self.log_file)
        self.fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(message)s')
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        
        self.initial_log_written = self._check_initial_log_written()
        self.confirmation_counter = self._get_initial_confirmation_counter()
    
    def log_initial_info(self, raw_image_path, res_image_path):
        if not self.initial_log_written:
            self.logger.info(f'.RAW_IMAGE_DIRECTORY\n{raw_image_path}')
            self.logger.info(f'.CONFIRMATION_RES_IMAGE_DIRECTORY\n{res_image_path}')
            self.logger.info(f'.CONFIRMATION_LIST')
            self.initial_log_written = True

    def log_confirmation(self, judgement, object_number):
        if not self.filename:
            raise ValueError("Filename not set. Please call log_name() first.")
        
        conf_number = self.confirmation_counter
        self.logger.info(f'CONF{conf_number} JUDGEMENT--({judgement})--IN--OBJECTNUMBER--({object_number})')
        self.confirmation_counter += 1