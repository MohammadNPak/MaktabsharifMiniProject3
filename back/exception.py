class PathNotFoundError(Exception):
    def __init__(self):
        msg = "Path dosn't exist"
    def __str__(self):
        return self.msg