"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_service(host):
    """Validate nomad service."""
    nomad = host.service('nomad')

    assert nomad.is_running
    assert nomad.is_enabled