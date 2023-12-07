#!/usr/bin/python3
"""(Fabric script) Fabfile file that generates a .tgz archive from the
contents of the web_static folder, using the function do_pack.
"""
from fabric.api import task, local
from datetime import datetime

@task
def do_pack():
    """Create a tar gzipped archive of the directory web_static.
    """
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(formatted_dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None
