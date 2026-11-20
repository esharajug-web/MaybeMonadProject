class Maybe:
    def __init__(self, value):
        self.value = value

    def is_present(self):
        return self.value is not None

    def is_empty(self):
        return self.value is None

    def map(self, function):
        if self.is_empty():
            return Maybe(None)

        return Maybe(function(self.value))

    def flat_map(self, function):
        if self.is_empty():
            return Maybe(None)

        return function(self.value)

    def get_or_else(self, default_value):
        if self.is_empty():
            return default_value

        return self.value