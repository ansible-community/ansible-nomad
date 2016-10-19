# Nomad

![](https://travis-ci.org/brianshumate/ansible-nomad.svg?branch=master)

This Ansible role performs a basic [Nomad](https://nomadproject.io/) installation, including filesystem structure, and example configuration.

It will also bootstrap a minimal cluster of 3 server nodes and do this
in a development environment based on Vagrant and VirtualBox. See
[README_VAGRANT.md](https://github.com/brianshumate/ansible-nomad/blob/master/examples/README_VAGRANT.md) for more details about the developer mode setup.

## Requirements

This role requires a Debian or RHEL family of Linux host; the role is tested
with the following specific software versions:

* Ansible: 2.1.0.0
* nomad: 0.4.1
* Debian: 8

## Role Variables

The role specifies variables in `defaults/main.yml`:

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `nomad_version` | `0.4.0` | nomad version to install |
| `nomad_zip_url` | `https://releases.hashicorp.com/nomad/{{ nomad_version }}/nomad_{{ nomad_version }}_linux_amd64.zip` | nomad download URL |
| `nomad_zip_sha256` | SHA256 SUM | nomad download SHA256 summary |
| `nomad_bin_path` | `/usr/local/bin` | nomad binary installation path |
| `nomad_config_path` | `/etc/nomad.d` | nomad configuration file path |
| `nomad_data_path` | `/var/nomad` | nomad data path |
| `nomad_log_path` | `/var/log/nomad` | nomad log path |
| `nomad_user` | `nomad` | nomad OS user |
| `nomad_group` | `bin` | nomad OS group |
| `nomad_region` | `global` | The default region |
| `nomad_datacenter` | boone | nomad datacenter label |
| `nomad_log_level` | `INFO` | Logging level |
| `nomad_syslog_enable` | true | nomad logs to syslog |
| `nomad_iface` | `eth1` | nomad network interface |
| `nomad_bind_address` | dynamic from hosts inventory | The interface address to bind to
| `nomad_enable_docker` | `false` | Install Docker subsystem on nodes? |

### OS Distribution Variables

The nomad binary works on most Linux platforms and is not distribution
specific. Some distributions require installation of specific OS packages with different nomenclature, so this role was built with support for
the major Linux distributions.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `nomad_centos_pkg` | `{{ nomad_version }}_linux_amd64.zip` | nomad package filename |
| `nomad_centos_url` | `{{ nomad_zip_url }}` | nomad package download URL |
| `nomad_centos_sha256` | SHA256 SUM | nomad download SHA256 summary |
| `nomad_centos_os_packages` | list | List of OS packages to install |
| `nomad_debian_pkg` | `{{ nomad_version }}_linux_amd64.zip` | nomad package filename |
| `nomad_debian_url` | `{{ nomad_zip_url }}` | nomad package download URL |
| `nomad_debian_sha256` | SHA256 SUM | nomad download SHA256 summary |
| `nomad_debian_os_packages` | list | List of OS packages to install |
| `nomad_redhat_pkg` | `{{ nomad_version }}_linux_amd64.zip` | nomad package filename |
| `nomad_redhat_url` | `{{ nomad_zip_url }}` | nomad package download URL |
| `nomad_redhat_sha256` | SHA256 SUM | nomad download SHA256 summary |
| `nomad_redhat_os_packages` | list | List of OS packages to install |
| `nomad_ubuntu_pkg` | `{{ nomad_version }}_linux_amd64.zip` | nomad package filename |
| `nomad_ubuntu_url` | `{{ nomad_zip_url }}` | nomad package download URL |
| `nomad_ubuntu_sha256` | SHA256 SUM | nomad download SHA256 summary |
| `nomad_ubuntu_os_packages` | list | List of OS packages to install |

## Dependencies

None

## Example Playbook


After you have reviewed and altered any necessary variables, and created a
hosts inventory, basic nomad installation is possible using the
included `site.yml` playbook:

```
ansible-playbook -i hosts site.yml
```

You can also simply pass variables in using the `--extra-vars` option
to the `ansible-playbook` command:

```
ansible-playbook -i hosts site.yml --extra-vars "nomad_datacenter=maui"
```

### Vagrant and VirtualBox

See `examples/README_VAGRANT.md` for details on quick Vagrant deployments
under VirtualBox for testing, etc.

## License

BSD

## Author Information

[Brian Shumate](http://brianshumate.com)
