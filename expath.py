import os
from pathlib import Path as _Path_, _windows_flavour, _posix_flavour


class ExPath(_Path_):
 _flavour = _windows_flavour if os.name == 'nt' else _posix_flavour


if __name__ == '__main__':
	pt = ExPath(os.getcwd())
