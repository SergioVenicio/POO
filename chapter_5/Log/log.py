from abc import ABCMeta, abstractmethod
from datetime import datetime
import io


class BaseLog(metaclass=ABCMeta):
    DEGUB = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    FATAL = 'FATAL'
    DT_FORMAT = '%Y-%m-%d %H:%M:%S'

    def debug(self, message: str):
        self.log(BaseLog.DEGUB, message)

    def info(self, message: str):
        self.log(BaseLog.INFO, message)

    def warning(self, message: str):
        self.log(BaseLog.WARNING, message)

    def error(self, message: str):
        self.log(BaseLog.ERROR, message)

    def fatal(self, message: str):
        self.log(BaseLog.FATAL, message)

    def get_date(self) -> str:
        return datetime.now().strftime(BaseLog.DT_FORMAT)

    @abstractmethod
    def log(self, log_level: str, message: str):
        raise NotImplementedError()


class FileLog(BaseLog):
    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path

    @property
    def _file(self) -> io.FileIO:
        return open(self.file_path, 'a')

    def log(self, log_level, message):
        log_string = f'[{self.get_date()}][{log_level}]: {message}\n'
        self._file.write(log_string)
        self._file.close()


class ScreenLog(BaseLog):
    def log(self, log_level, message):
        print(f'[{self.get_date()}][{log_level}]: {message}')
