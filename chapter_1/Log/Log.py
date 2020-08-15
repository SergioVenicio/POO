import sys


class Log:
    def debug(self, message: str):
        self.print_msg("DEGUB ", message)

    def info(self, message: str):
        self.print_msg("INFO ", message)

    def warning(self, message: str):
        self.print_msg("WARNING ", message)

    def error(self, message: str):
        self.print_msg("ERRROR ", message)

    def fatal(self, message: str):
        self.print_msg("Fatal ", message)
        sys.exit(1)

    def print_msg(self, message: str, severity: str):
        print(severity + ": " + message)


if __name__ == '__main__':
    log = Log()
    log.debug('test')
