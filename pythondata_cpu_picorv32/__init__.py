import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post87"
version_tuple = (1, 0, 87)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post87")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post38"
data_version_tuple = (1, 0, 38)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post38")
except ImportError:
    pass
data_git_hash = "59ef49564f214f5031cf7e6c67290dac6354fb69"
data_git_describe = "v1.0-38-g59ef495"
data_git_msg = """\
commit 59ef49564f214f5031cf7e6c67290dac6354fb69
Author: Larry Doolittle <ldoolitt@recycle.lbl.gov>
Date:   Thu Apr 23 18:01:24 2020 +0200

    Remove obsolete line from firmware/sections.lds
    
    Signed-off-by: Claire Wolf <claire@symbioticeda.com>

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
