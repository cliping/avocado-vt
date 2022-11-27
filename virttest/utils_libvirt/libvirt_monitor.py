import copy
import logging

from avocado.core import exceptions

from virttest import virsh

LOG = logging.getLogger('avocado.' + __name__)


def check_domjobinfo(params, expected_list, remote=False):
    """
    Check domjobinfo

    :param params: dict, get vm name
    :param expected_list: expected list
    :param remote: check remote host if remote is True
    """
    vm_name = params.get("main_vm")
    remote_ip = params.get("remote_ip")
    options = params.get("domjobinfo_options", "")

    LOG.info("Check domjobinfo")
    if remote:
        dest_uri = "qemu+ssh://%s/system" % remote_ip
        jobinfo = virsh.domjobinfo(vm_name, options, debug=True, uri=dest_uri)
    else:
        jobinfo = virsh.domjobinfo(vm_name, options, debug=True)
    tmp_list = copy.deepcopy(expected_list)
    for line in jobinfo.stdout.splitlines():
        key = line.split(':')[0]
        if key in tmp_list:
            value = ':'.join(line.strip().split(':')[1:]).strip()
            LOG.debug("domjobinfo: key = %s, value = %s", key, value)
            LOG.debug("expected key = %s, value = %s", key, tmp_list.get(key))
            if value != tmp_list.get(key):
                raise exceptions.TestFail("'%s' is not matched expect '%s'" % (value, tmp_list.get(key)))
            else:
                del tmp_list[key]
