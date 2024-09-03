import logging
import os

class CustomLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger('CustomLogger')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        
        # Check if the log file already exists and contains the initial headers
        self.initial_log_written = self._check_initial_log_written()
        self.confirmation_counter = self._get_initial_confirmation_counter()
    
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
    
    def log_initial_info(self, raw_image_path, res_image_path):
        if not self.initial_log_written:
            self.logger.info(f'.RAW_IMAGE_DIRECTORY\n{raw_image_path}')
            self.logger.info(f'.CONFIRMATION_RES_IMAGE_DIRECTORY\n{res_image_path}')
            self.logger.info(f'.CONFIRMATION_LIST')
            self.initial_log_written = True

    def log_confirmation(self, judgement, object_number):
        conf_number = self.confirmation_counter
        self.logger.info(f'CONF{conf_number} JUDGEMENT--({judgement})--IN--OBJECTNUMBER--({object_number})')
        self.confirmation_counter += 1


# Contoh penggunaan
if __name__ == "__main__":
    # Tentukan nama file log
    log_file_path = "A:/TMMIN Project/cuptip_vision/vizcap/logs/file1.txt"

    # Pastikan direktori untuk file log ada
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Buat instance logger
    custom_logger = CustomLogger(log_file_path)
    stat = ["OK", "OK", "OK", "NG", "OK", "OK", "OK","OK", "SANGKAKU",]
    for i, data in enumerate(stat, 1):
        custom_logger.log_confirmation(data, i)

    # Log informasi awal (hanya dilakukan sekali)
    custom_logger.log_initial_info("path/to/raw_image", "path/to/res_image")

    # Log beberapa informasi sebagai contoh
    # custom_logger.log_confirmation("PASS", 123)
    # custom_logger.log_confirmation("FAIL", 456)

    print(f"Log telah dibuat di {log_file_path}")
