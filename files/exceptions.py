class RateLimitError(Exception):
    pass

class ServerError(Exception):
    pass

class NoneJsonError(Exception):
    pass

class IDJsonError(Exception):
    pass

class TweetJsonError(Exception):
    pass

class ScanningError(Exception):
    pass

class FailedConnectDatabase(Exception):
    pass
