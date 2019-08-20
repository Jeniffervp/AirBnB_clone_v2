#!/usr/bin/python3
""" create a tgz file """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Function to make a pack of a directory on local"""

    local('mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    final = 'versions/web_static_{}.tgz'.format(date)

    try:
        local('tar -czvf {} web_static'.format(final))
        return final
    except:
        return None
