import json
import urllib.request
from importlib.metadata import version as _get_installed_version
from packaging.version import Version
import functools
from abc import ABCMeta, abstractmethod

class ObjectAutoupdateable(ABCMeta):
    @abstractmethod
    def DisableAutoUpdate(self) -> None: ...

class ClassAutoupdateable(ABCMeta):
    @abstractmethod
    def DisableAutoUpdate(cls) -> None: ...

def objectautoupdatecheck(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._autoupdate:
            update_package()
        return func(self, *args, **kwargs)
    return wrapper

def classautoupdatecheck(func):
    @functools.wraps(func)
    def wrapper(cls, *args, **kwargs):
        if cls._autoupdate:
            update_package()
        return func(cls, *args, **kwargs)
    return wrapper









def _get_pypi_version(name: str) -> str:
    url = f"https://pypi.org/pypi/{name}/json"
    with urllib.request.urlopen(url) as resp:
        data = json.load(resp)
    return data["info"]["version"]

def _process_update():
    name = "uniterm"
    local = Version(_get_installed_version(name))
    remote = Version(_get_pypi_version(name))

    if remote > local:
        print(f"Update available: {local} → {remote}")
    elif remote == local:
        print("Up to date.")
    else:
        print("Local version is newer than PyPI (unusual.")

def update_package() -> None:
    print("updating")