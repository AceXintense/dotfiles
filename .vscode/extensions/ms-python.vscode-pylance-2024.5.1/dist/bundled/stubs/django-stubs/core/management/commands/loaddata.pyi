import zipfile
from collections.abc import Iterable

from django.core.management.base import BaseCommand

READ_STDIN: str = ...

class Command(BaseCommand):
    missing_args_message: str = ...
    def loaddata(self, fixture_labels: Iterable[str]) -> None: ...
    def load_label(self, fixture_label: str) -> None: ...
    def find_fixtures(self, fixture_label: str) -> list[str | None]: ...
    @property
    def fixture_dirs(self) -> list[str]: ...
    def parse_name(self, fixture_name: str) -> tuple[str, str, str]: ...

class SingleZipReader(zipfile.ZipFile): ...

def humanize(dirname: str) -> str: ...
