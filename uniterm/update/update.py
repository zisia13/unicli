import json
import urllib.request
from importlib.metadata import version as _get_installed_version
from packaging.version import Version
import functools
import subprocess
import sys
from abc import ABC, abstractmethod

_autoupdate_var_name = "_autoupdate"

class ObjectAutoupdateable(ABC):
    @abstractmethod
    def DisableAutoUpdate(self) -> None:
        raise NotImplementedError()

class ClassAutoupdateable(ABC):
    @classmethod
    @abstractmethod
    def DisableAutoUpdate(cls) -> None:
        raise NotImplementedError()

def objectautoupdatecheck(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if getattr(self, _autoupdate_var_name):
            Updater.run()
        return func(self, *args, **kwargs)
    return wrapper

def classautoupdatecheck(func):
    @functools.wraps(func)
    def wrapper(cls, *args, **kwargs):
        if getattr(cls, _autoupdate_var_name):
            Updater.run()
        return func(cls, *args, **kwargs)
    return wrapper



class Updater:
    name = "uniterm"

    @classmethod
    def _get_installed_version(cls) -> str:
        return _get_installed_version(cls.name)

    @classmethod
    def _get_pypi_version(cls) -> str:
        url = f"https://pypi.org/pypi/{cls.name}/json"
        with urllib.request.urlopen(url) as resp:
            data = json.load(resp)
        return data["info"]["version"]
    
    @classmethod
    def _check_for_update(cls) -> bool:
        local = Version(cls._get_installed_version())
        remote = Version(cls._get_pypi_version())

        if remote > local:
            # print(f"Update available: {local} → {remote}")
            return True
        elif remote == local:
            # print("Up to date.")
            return False
        else:
            # print("Local version is newer than PyPI")
            return False

    @classmethod
    def _update(cls) -> None:
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "--upgrade", cls.name
            ])
        except Exception as error:
            print(f"Lib could not be updated: {error}")

    @classmethod
    def run(cls) -> None:
        cls._update() if cls._check_for_update() else None
