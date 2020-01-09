import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_java_installed(host):
    java = host.package("java-1.8.0-openjdk")

    assert java.is_installed


def test_java_home_set(host):
    java_home = host.environment()["JAVA_HOME"]
    assert java_home == "/usr/lib/jvm/java-1.8.0-openjdk.x86_64"


def test_java_version(host):
    java_version = host.run("java -version")
    java_version_stderr = java_version.stderr

    assert java_version.rc == 0
    assert 'openjdk version "1.8.0_232"' in java_version_stderr
    assert "OpenJDK Runtime Environment (build 1.8.0_232-b09)" in java_version_stderr
    assert (
        "OpenJDK 64-Bit Server VM (build 25.232-b09, mixed mode)" in java_version_stderr
    )
