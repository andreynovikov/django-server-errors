import os
from unittest import mock

from errors import recorder

TESTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')


def is_project_or_test_file(filename, is_project_file=recorder.is_project_file):
    return is_project_file(filename) or filename.startswith(TESTS_DIR)


class TestsAreProjectCode:
    """
    The views and tasks of the tests stand for project code. When the package
    is installed they are in site-packages, which the recorder skips.
    """
    def setUp(self):
        patcher = mock.patch.object(recorder, 'is_project_file', is_project_or_test_file)
        patcher.start()
        self.addCleanup(patcher.stop)
        super().setUp()
