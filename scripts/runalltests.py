import os
import stat
import subprocess
import glob

executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
for filename in glob.glob("test_*"):
    if os.path.isfile(filename):
        st = os.stat(filename)
        mode = st.st_mode
        if mode & executable:
            print("Running " + filename)
            command = "./" + filename
            proc    = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output, _ = proc.communicate()
            print(output)

            if proc.returncode != 0:
                print("** ERROR ** returned error code {}".format(proc.returncode))
