#!/usr/bin/python3
""" distributes an archive to your web servers using """
from datetime import datetime
from fabric.api import local, run, put, env
from os.path import exists

env.hosts = ['35.190.156.211', '34.73.132.239']


def do_pack():
    """ Function to make a pack of a directory on local """

    local('mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    final = 'versions/web_static_{}.tgz'.format(date)

    try:
        local('tar -czvf {} web_static'.format(final))
        return final
    except:
        return None


def do_deploy(archive_path):
    """ distributes an archive to web servers """
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        base = archive_path.split('/')[-1]
        extent = base.split('.')[0]
        rel = '/data/web_static/releases/'
        cur = '/data/web_static/current'
        run('mkdir -p {}{}/'.format(rel, extent))
        run('tar -xzf /tmp/{} -C {}{}/'.format(base, rel, extent))
        run('rm /tmp/{}'.format(base))
        run('mv {1}{0}/web_static/* {1}{0}/'.format(extent, rel))
        run('rm -rf {}{}/web_static'.format(rel, extent))
        run('rm -rf {}'.format(cur))
        run('ln -fs {}{}/ {}'.format(rel, extent, cur))
        return True
    except:
        return False


def deploy():
    """ fabrick script that creates an archive and distribute it """

    a = do_pack()
    if not a:
        return False
    else:
        new = do_deploy(a)
        return new
