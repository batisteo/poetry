# -*- coding: utf-8 -*-

from typing import Union


class Operation(object):

    def __init__(self, reason=None):  # type: (Union[str, None]) -> None
        self._reason = reason

        self._skipped = False
        self._skip_reason = None

    @property
    def job_type(self):  # type: () -> str
        raise NotImplementedError

    @property
    def reason(self):  # type: () -> str
        return self._reason

    @property
    def skipped(self):  # type: () -> bool
        return self._skipped

    @property
    def skip_reason(self):  # type: () -> Union[str, None]
        return self._skip_reason

    def format_version(self, package):  # type: (...) -> str
        return package.full_pretty_version

    def skip(self, reason):  # type: (str) -> Operation
        self._skipped = True
        self._skip_reason = reason

        return self
