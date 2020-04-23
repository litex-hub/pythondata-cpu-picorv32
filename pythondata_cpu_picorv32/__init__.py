import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/cliffordwolf/picorv32"

# Module version
version_str = "1.0.post83"
version_tuple = (1, 0, 83)
try:
    from packaging.version import Version as V
    pversion = V("1.0.post83")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.post34"
data_version_tuple = (1, 0, 34)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.post34")
except ImportError:
    pass
data_git_hash = "409d0dfd6772551e2ce77502e368973c447cbeb8"
data_git_describe = "v1.0-34-g409d0df"
data_git_msg = """\
commit 409d0dfd6772551e2ce77502e368973c447cbeb8
Merge: fe1ee2c 0201e8f
Author: Claire Wolf <clifford@clifford.at>
Date:   Wed Apr 22 17:32:19 2020 +0200

    Merge pull request #145 from Novakov/patch-1
    
    spimemio documentation: read latency reset value

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
