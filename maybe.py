class Maybe:
    def __init__(self, value):
        self.value = value

    def map(self, function):
        if self.value is None:
            return Maybe(None)
        return Maybe(function(self.value))

    def flat_map(self, function):
        if self.value is None:
            return Maybe(None)
        return function(self.value)

    def get_or_else(self, default_value):
        if self.value is None:
            return default_value
        return self.value