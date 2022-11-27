import logging

from avocado.utils import process

from virttest import utils_libvirtd
from virttest import remote

LOG = logging.getLogger('avocado.' + __name__)


def get_service_name(params):
    """
    Get service name on source or target host

    :param params: Dictionary with the test parameters
    """
    service_name = params.get("service_name", "libvirtd")
    service_on_dst = "yes" == params.get("service_on_dst", "no")
    server_ip = params.get("remote_ip")
    server_user = params.get("remote_user", "root")
    server_pwd = params.get("remote_pwd")

    if service_name == "libvirtd":
        if service_on_dst:
            remote_session = remote.wait_for_login('ssh', server_ip, '22',
                                                   server_user, server_pwd,
                                                   r"[\#\$]\s*$")
            service_name = utils_libvirtd.Libvirtd(session=remote_session).service_name
            remote_session.close()
        else:
            service_name = utils_libvirtd.Libvirtd().service_name
    LOG.debug("service name: %s" % service_name)
    return service_name


def kill_service(params):
    """
    Kill service on source or target host

    :param params: Dictionary with the test parameters
    """
    service_on_dst = "yes" == params.get("service_on_dst", "no")

    service_name = get_service_name(params)
    cmd = "kill -9 `pidof %s`" % service_name
    if service_on_dst:
        remote.run_remote_cmd(cmd, params, ignore_status=False)
    else:
        process.run(cmd, ignore_status=False, shell=True)


def control_service(params):
    """
    Control service on source or target host

    :param params: Dictionary with the test parameters
    """
    service_on_dst = "yes" == params.get("service_on_dst", "no")
    service_operations = params.get("service_operations", "restart")

    service_name = get_service_name(params)
    cmd = "systemctl %s %s" % (service_operations, service_name)
    if service_on_dst:
        remote.run_remote_cmd(cmd, params, ignore_status=False)
    else:
        process.run(cmd, ignore_status=False, shell=True)
