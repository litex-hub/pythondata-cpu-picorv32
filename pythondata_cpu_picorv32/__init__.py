import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post112"
version_tuple = (1, 0, 112)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post112")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post39"
data_version_tuple = (1, 0, 39)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post39")
except ImportError:
    pass
data_git_hash = "f9b1beb4cfd6b382157b54bc8f38c61d5ae7d785"
data_git_describe = "v1.0-39-gf9b1beb"
data_git_msg = """\
commit f9b1beb4cfd6b382157b54bc8f38c61d5ae7d785
Author: Larry Doolittle <ldoolitt@recycle.lbl.gov>
Date:   Mon Apr 27 17:23:45 2020 +0200

    Make Makefile more flexible
    
    Signed-off-by: Claire Wolf <claire@symbioticeda.com>

"""

# Tool version info
tool_version_str = "0.0.post73"
tool_version_tuple = (0, 0, 73)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post73")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_picorv32."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_picorv32".format(f))
    return fn
