import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post164"
version_tuple = (1, 0, 164)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post164")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post47"
data_version_tuple = (1, 0, 47)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post47")
except ImportError:
    pass
data_git_hash = "1d9f5b7678c008fd4ab71d9c742a70ff2365f186"
data_git_describe = "v1.0-47-g1d9f5b7"
data_git_msg = """\
commit 1d9f5b7678c008fd4ab71d9c742a70ff2365f186
Merge: 6b13977 2cce6f4
Author: Claire Xen <claire@clairexen.net>
Date:   Mon Dec 6 16:10:29 2021 +0100

    Merge pull request #166 from tommythorn/master
    
    Enable the use of 64-bit riscv tools

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_picorv32."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_picorv32".format(f))
    return fn
