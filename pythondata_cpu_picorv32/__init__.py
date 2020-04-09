import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post71"
version_tuple = (1, 0, 71)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post71")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post23"
data_version_tuple = (1, 0, 23)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post23")
except ImportError:
    pass
data_git_hash = "e308982e18fc952a8d446ddb7ea8b70433a998c2"
data_git_describe = "v1.0-23-ge308982"
data_git_msg = """\
commit e308982e18fc952a8d446ddb7ea8b70433a998c2
Merge: 46aa89c 1e24e99
Author: Clifford Wolf <clifford@clifford.at>
Date:   Mon Nov 18 14:21:10 2019 +0100

    Merge pull request #141 from rxrbln/master
    
    added CROSS prefix and CFLAGS to the picsoc/Makefile

"""

# Tool version info
tool_version_str = "0.0.post48"
tool_version_tuple = (0, 0, 48)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post48")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_picorv32."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_picorv32".format(f))
    return fn
