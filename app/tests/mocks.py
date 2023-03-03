class FakeResponse:
    def __init__(self, data=None, status_code=None):
        self._data = data
        self._status_code = status_code

    @property
    def data(self):
        return self._data

    @property
    def status_code(self):
        return self._status_code
