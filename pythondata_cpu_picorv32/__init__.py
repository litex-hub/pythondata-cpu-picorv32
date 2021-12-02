import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post152"
version_tuple = (1, 0, 152)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post152")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post40"
data_version_tuple = (1, 0, 40)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post40")
except ImportError:
    pass
data_git_hash = "100e421be0aa5fb130b6e4f532d15fc7d1a03f02"
data_git_describe = "v1.0-40-g100e421"
data_git_msg = """\
commit 100e421be0aa5fb130b6e4f532d15fc7d1a03f02
Author: Claire Xenia Wolf <claire@clairexen.net>
Date:   Thu Dec 2 15:59:12 2021 +0100

    Fix copyright info
    
    Signed-off-by: Claire Xenia Wolf <claire@clairexen.net>

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
