import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post74"
version_tuple = (1, 0, 74)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post74")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post25"
data_version_tuple = (1, 0, 25)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post25")
except ImportError:
    pass
data_git_hash = "824a5c801194299f89f4fd8844c1fbcd1bdf4e21"
data_git_describe = "v1.0-25-g824a5c8"
data_git_msg = """\
commit 824a5c801194299f89f4fd8844c1fbcd1bdf4e21
Merge: e308982 a7ff70d
Author: Claire Wolf <clifford@clifford.at>
Date:   Wed Apr 15 18:49:23 2020 +0200

    Merge pull request #158 from rxrbln/uart
    
    added default clk divider parameter to simpleuart

"""

# Tool version info
tool_version_str = "0.0.post49"
tool_version_tuple = (0, 0, 49)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post49")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_picorv32."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_picorv32".format(f))
    return fn
