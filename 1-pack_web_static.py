#!/usr/bin/python3
"""(Fabric script) Fabfile file that generates a .tgz archive from the
   contents of the web_static folder, using the function do_pack.
"""
from time import strftime
from datetime import date
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static.
    """
    file = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(file))
        print("Packing web_static to versions/web_static_{}.tgz".format(file)
        return "versions/web_static_{}.tgz".format(file)
    except Exception as e:
        return None
