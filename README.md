# Nomad

[![Build Status](https://travis-ci.org/brianshumate/ansible-nomad.svg?branch=master)](https://travis-ci.org/brianshumate/ansible-nomad)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-brianshumate.nomad-blue.svg)](https://galaxy.ansible.com/brianshumate/nomad/)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/brianshumate/ansible-nomad.svg)](http://isitmaintained.com/project/brianshumate/ansible-nomad "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/brianshumate/ansible-nomad.svg)](http://isitmaintained.com/project/brianshumate/ansible-nomad "Percentage of issues still open")

This Ansible role performs basic [Nomad](https://nomadproject.io/)
installation, including filesystem structure, and example configuration.

It will also bootstrap a minimal cluster of 3 server nodes, and can do this
in a development environment based on Vagrant and VirtualBox. See
[README_VAGRANT.md](https://github.com/brianshumate/ansible-nomad/blob/master/examples/README_VAGRANT.md) for more details about the Vagrant setup.

## Requirements

This role requires a Debian, RHEL, or Ubuntu distribution; the role is tested
with the following specific software versions:

* Ansible: 2.3.0.0
* nomad: 0.5.6
* CentOS: 7
* Debian: 8
* RHEL: 7
* Ubuntu: 16.04

## Role Variables

The role defines most of its variables in `defaults/main.yml`:

### `nomad_version`

- Nomad version to install
- Default value: **0.5.6**

### `nomad_architecture_map`

- This variable does not need to be changed in most cases
- Default value: Dictionary translating ansible_architecture to HashiCorp
  architecture naming convention

### `nomad_architecture`

- Host architecture
- Default value: determined by `{{ nomad_architecture_map[ansible_architecture] }}`

### `nomad_zip_url`

- Nomad download URL
- Default value: `https://releases.hashicorp.com/nomad/{{ nomad_version }}/nomad_{{ nomad_version }}_linux_{{nomad_architecture}}.zip`

### `nomad_bin_dir`

- Nomad binary installation path
- Default value: `/usr/local/bin`

### `nomad_config_dir`

- Nomad configuration file path
- Default value: `/etc/nomad.d`

### `nomad_data_dir`

- Nomad data path
- Default value: `/var/nomad`

### `nomad_log_dir`

- Nomad log path
- Default value: `/var/log/nomad`

### `nomad_user`

- Nomad OS username
- Default value: **nomad**

### `nomad_group`

- Nomad OS group
- Default value: **bin**

### `nomad_region`

- Default region
- Default value: **global**

### `nomad_datacenter`

- Nomad datacenter label
- Default value: **dc1**

### `nomad_log_level`

- Logging level
- Default value: **INFO**

### `nomad_syslog_enable`

- Log to syslog
- Default value: **true**

### `nomad_iface`

- Nomad network interface
- Default value: **eth1**

### `nomad_advertise_address`

- Network interface address to advertise to other nodes
- Default value: dynamic from hosts inventory

### `nomad_bind_address`

- Bind interface address
- Default value: **0.0.0.0**

### `nomad_docker_enable`

- Install Docker subsystem on nodes?
- Default value: **false**

### 'nomad_use_consul'

- Bootstrap nomad via native consul zero-configuration support
  assumes consul default ports etc.
- Default value: **False**

#### Custom Configuration Section

As Nomad loads the configuration from files and directories in lexical order,
typically merging on top of previously parsed configuration files, you may set
custom configurations via `nomad_config_custom`, which will be expanded into a file named `custom.json` within your `nomad_config_dir` which will
be loaded after all other configuration by default.

An example usage for enabling `vault`:

```yaml
  vars:
    nomad_config_custom:
      vault:
        enabled          : true
        ca_path          : "/etc/certs/ca"
        cert_file        : "/var/certs/vault.crt"
        key_file         : "/var/certs/vault.key"
        address          : "https://vault.service.consul:8200"
        create_from_role : "nomad-cluster"
```

### OS Distribution Variables

The `nomad` binary works on most Linux platforms and is not distribution
specific. However, some distributions require installation of specific OS
packages with different naming, so this role was built with support for
popular Linux distributions and defines these variables to deal with the
differences across distributions:

### `nomad_centos_pkg`

- Nomad package filename
- Default value: `{{ nomad_version }}_linux_amd64.zip`

### `nomad_centos_url`

- Nomad package download URL
- Default value: `{{ nomad_zip_url }}`

### `nomad_centos_sha256`

- Nomad download SHA256 summary
- Default value: **SHA256 SUM**

### `nomad_centos_os_packages`

- List of OS packages to install
- Default value: **list**

### `nomad_debian_pkg`

- Nomad package filename
- Default value: `{{ nomad_version }}_linux_amd64.zip`

### `nomad_debian_url`

- Nomad package download URL
- Default value: `{{ nomad_zip_url }}`

### `nomad_debian_sha256`

- Nomad download SHA256 summary
- Default value: **SHA256 SUM**

### `nomad_debian_os_packages`

- List of OS packages to install
- Default value: **list**

### `nomad_redhat_pkg`

- Nomad package filename
- Default value: `{{ nomad_version }}_linux_amd64.zip`

### `nomad_redhat_url`

- Nomad package download URL
- Default value: `{{ nomad_zip_url }}`

### `nomad_redhat_sha256`

- Nomad download SHA256 summary
- Default value: **SHA256 SUM**

### `nomad_redhat_os_packages`

- List of OS packages to install
- Default value: **list**

### `nomad_ubuntu_pkg`

- Nomad package filename
- Default value: `{{ nomad_version }}_linux_amd64.zip`

### `nomad_ubuntu_url`

- Nomad package download URL
- Default value: `{{ nomad_zip_url }}`

### `nomad_ubuntu_sha256`

- Nomad download SHA256 summary
- Default value: *8SHA256 SUM**

### `nomad_ubuntu_os_packages`

- List of OS packages to install
- Default value: **list**

## Dependencies

Ansible requires GNU tar and this role performs some local use of the
unarchive module, so ensure that your system has `gtar` installed.

## Example Playbook

Basic nomad installation is possible using the included `site.yml` playbook:

```
ansible-playbook -i <hosts> site.yml
```

You can also simply pass variables in using the `--extra-vars` option to the
`ansible-playbook` command:

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

## Contributors

Special thanks to the folks listed in [CONTRIBUTORS.md](https://github.com/brianshumate/ansible-nomad/blob/master/CONTRIBUTORS.md) for their
contributions to this project.

Contributions are welcome, provided that you can agree to the terms outlined
in [CONTRIBUTING.md](https://github.com/brianshumate/ansible-nomad/blob/master/CONTRIBUTING.md)
