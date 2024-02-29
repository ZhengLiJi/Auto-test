from lib.settings.logger import log
from lib.settings.get_time import GetTime
from lib.settings.random_utils import Random
from lib.settings.verify import Verify


class BaseUtils:
    _have = {}

    @property
    def log(self):
        return log

    @property
    def time(self):
        if self._have.get("time") is None:
            self._have['time'] = GetTime()
        return self._have['time']

    @property
    def random(self):
        if self._have.get("random") is None:
            self._have['random'] = Random()
        return self._have['random']

    @property
    def verify(self):
        if self._have.get("verify") is None:
            self._have['verify'] = Verify()
        return self._have['verify']

if __name__ == '__main__':
    a = BaseUtils()
    a.log.info("abc")
    a.log.info("def")
