import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/YosysHQ/picorv32"

# Module version
version_str = "1.0.post218"
version_tuple = (1, 0, 218)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post218")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post70"
data_version_tuple = (1, 0, 70)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post70")
except ImportError:
    pass
data_git_hash = "87c89acc18994c8cf9a2311e871818e87d304568"
data_git_describe = "v1.0-70-g87c89acc1899"
data_git_msg = """\
commit 87c89acc18994c8cf9a2311e871818e87d304568
Author: Miodrag Milanovic <mmicko@gmail.com>
Date:   Mon Jun 17 08:20:13 2024 +0200

    clean Makefile

"""

# Tool version info
tool_version_str = "0.0.post148"
tool_version_tuple = (0, 0, 148)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post148")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_picorv32."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_picorv32".format(f))
    return fn
