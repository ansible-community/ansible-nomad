## v1.0.0

- Installs Nomad on each node
- Installs example configuration for server and client
- Installs example init, systemd, and upstart scripts
- Correct versions
- Update Galaxy meta

## v1.0.1

- Remove unused variables
- Update documentation

## v1.0.2

- Enable and start nomad service
- Fixup initial configuration paths
- Update documentation

## v1.1.0

- Prepare role for Galaxy
- Add optional Docker installation support
- Update initial configuration
- Update documentation
- Update start scripts

## v1.1.1

- Switch to galaxy_tags
- Enable CI

## v1.1.2

- Tests run best when they exist!

## v1.1.3

- Fix package name vars

## v1.1.4

- Update supported versions
- Fix up unarchive task quoting

## v1.1.5

- Keyserver quoting

## v1.1.6

- Update OS packages
- Update signing key tasks

## v1.1.7

- Update default variables
- Update supported versions
- Update documentation — now w/ more header meta (h/t @dochang)

## v1.1.8

- Update doc meta

## v1.1.9

- Remove deprecated tasks
- Add conditionals to tasks

## v1.2.0

- Dropping native Docker subsystem support in favor of external role
- Attempting to run nomad as nomad user

## v1.2.1

- Renamed vars to be more in line with Nomad terminology
- Switched to merged config style with base, bootstrap, server, client

## v1.3.0

- Remove Docker majority of bits except for supporting packages, etc.
- Docker will only be installed for Vagrant based clusters via the
  Vagrant provisioner when environment variable `NOMAD_DOCKER_ENABLE="true"`
  is set
- Update start scripts to be smarter about node role
- Add cgroups packages on Debian/Ubuntu
- Run Nomad as root for now

## v1.3.1

- Update/validate CentOS 7 box
- Update documentation
- Update failure cases for CentOS

## v1.3.2

- Disable SELinux when Docker is used

## v1.3.3

- Correct var
- More SELinux config

## v1.4.0

- Nomad 0.5.0
- Automatic SHA determination
- Streamline and split out install, Docker, and SELinux tasks
- Remove deprecated task files
- Establish OS vars
- Update documentation

## v1.4.1

- Nomad 0.5.1
- Add NOMAD_VERSION environment variable
- Fix typo in default variables

## v1.4.2

- Checks for existing packages and summary files
- Nomad 0.5.2

## v1.4.3

- Nomad 0.5.4

## v1.4.4

- Nomad 0.5.4
- Fixed typo in install tasks fixes #6 (thanks @asemt)
- Added nomad_group_name and use nomad_iface (thanks @dggreenbaum)
- Updated documentation

## v1.4.5

- Switch init scripts to send SIGTERM to address #2
- Add leave_on_terminate and set to True by default

## v1.4.6

- Better conditionals for init scripts fixes #5
- Change to compact YAML
- Misc task updates

## v1.5.0

- Version fix

## v1.5.1

- Enable the service when starting
- Prefer compact YAML in tasks
- Task cleanup

## v1.5.2

- Initial ARM support (thanks @lanefu)

## v1.5.3

- Nomad version 0.5.5
- Updated documentation

## v1.5.4

- Make nomad user account dynamic and also a system account

## v1.5.5

- Fix cluster_nodes references

## v1.5.6

- Add iface env var

## v1.5.7

- Nomad version 0.5.6
- Update documentation

## v1.6.0

- Use all directory variables in all templates
  - Addresses #8
  - Addresses #9
- New variables:
  - `nomad_lockfile`
  - `nomad_run_dir`
- Updated init script templates
- Updated systemd unit template
- Convert to local action plays

## v1.6.1

- Fix install task issue

## v1.6.2

- Move bootstrap into server config
- Remove bootstrap node role
- Use node role in startup scripts
- Update startup scripts
- Update install playbook

## v1.6.3

- Remove bootstrap task

## v1.6.4

- Fix log portion of start line in init script - fixes #13
- Fix bad nomad_docker_enable variable refs
- Update CONTRIBUTING

## v1.6.5

- Add custom configuration option (thanks @awheeler)
- Fixed systemd service file when nomad_custom_config used (thanks @awheeler)
- Update documentation
- Update task meta
- Update role meta
- Update CONTRIBUTORS

## v1.7.0

- Update README (thanks @groggemans)
- Add meta parameters to client template (thanks @groggemans)
- Add options parameters to client template (thanks @groggemans)
- Update and fix CONTRIBUTORS file (thanks @groggemans)
- Small syntax fixes and init script updates (thanks @groggemans)
- Update and extend config templates (thanks @groggemans)
- Main tasks cleanup (thanks @groggemans)
- Initial reordering of role defaults (thanks @groggemans)
- Move asserts and checks to there own file (thanks @groggemans)
- CHANGELOG++

## v1.7.1

- Clean up docker tasks
- Fix debian init and client only config (thanks @groggemans)

## v1.7.2

- Conditionally include options and meta to avoid error when empty
- Rename `nomad_cluster_nodes` label to `nomad_instances`

## v1.7.3

- Nomad version 0.6.0

## v1.7.4

- Proper client/server template rendering (thanks @awheeler)

## v1.7.5

- Nomad v0.6.2
- Re-instate nomad_use_consul functionality (thanks @awheeler)

## v1.7.6

- Nomad 0.6.3
- Finish cluster_nodes -> nomad_instances renaming
- Update CONTRIBUTORS
- Typo fixes (thanks @kjagiello)

## v1.7.7 (UNRELEASED)

- Explicit owner and mode for config files (thanks @groggemans)
