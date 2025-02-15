#!/usr/bin/python3
"""(Fabric script) Fabfile file that generates a .tgz archive from the
contents of the web_static folder, using the function do_pack.
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static.
    """
    d_t = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            d_t.year, 
            d_t.month, 
            d_t.day, 
            d_t.hour, 
            d_t.minute, 
            d_t.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
