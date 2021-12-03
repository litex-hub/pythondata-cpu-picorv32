import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post153"
version_tuple = (1, 0, 153)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post153")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post41"
data_version_tuple = (1, 0, 41)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post41")
except ImportError:
    pass
data_git_hash = "e8edf98772672653c67dc3f4877980abcaaedf09"
data_git_describe = "v1.0-41-ge8edf98"
data_git_msg = """\
commit e8edf98772672653c67dc3f4877980abcaaedf09
Author: Miodrag Milanovic <mmicko@gmail.com>
Date:   Fri Dec 3 15:54:08 2021 +0100

    add license file

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_picorv32."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_picorv32".format(f))
    return fn
