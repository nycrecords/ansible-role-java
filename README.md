
![GitHub](https://img.shields.io/github/license/nycrecords/ansible-role-java)
[![Build Status](https://travis-ci.org/geerlingguy/ansible-role-java.svg?branch=master)](https://travis-ci.org/geerlingguy/ansible-role-java)
[![Galaxy](https://img.shields.io/badge/galaxy-nycrecords.java-blue.svg)](https://galaxy.ansible.com/nycrecords/java)
![Ansible](https://img.shields.io/ansible/role/d/45553)
![Ansible](https://img.shields.io/ansible/quality/45553)

# Ansible Role: Java

Installs Java for RedHat/CentOS and Debian/Ubuntu linux servers.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values:

    # The defaults provided by this role are specific to each distribution.
    java_packages:
      - java-1.8.0-openjdk

Set the version/development kit of Java to install, along with any other necessary Java packages. Some other options include are included in the distribution-specific files in this role's 'defaults' folder.

    java_home: ""

If set, the role will set the global environment variable `JAVA_HOME` to this value.

## Dependencies

None.

## Example Playbook (using default package)

    - hosts: servers
      roles:
        - role: geerlingguy.java
          become: yes

## Example Playbook (install OpenJDK 8)

For RHEL / CentOS:

    - hosts: server
      roles:
        - role: geerlingguy.java
          when: "ansible_os_family == 'RedHat'"
          java_packages:
            - java-1.8.0-openjdk

For Ubuntu < 16.04:

    - hosts: server
      tasks:
        - name: installing repo for Java 8 in Ubuntu
  	      apt_repository: repo='ppa:openjdk-r/ppa'
    
    - hosts: server
      roles:
        - role: geerlingguy.java
          when: "ansible_os_family == 'Debian'"
          java_packages:
            - openjdk-8-jdk

## License

MIT / BSD

## Author Information

This role was originally created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).

Modified by [Joel Castillo](https://github.com/joelbcastillo) for the [NYC Department of Records and Information Services](https://github.com/nycrecords).
