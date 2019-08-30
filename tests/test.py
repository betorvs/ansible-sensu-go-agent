import testinfra

def test_sensu_file(host):
    sensu = host.file("/etc/sensu/agent.yml")
    assert sensu.user == "root"
    assert sensu.group == "root"
    assert sensu.mode == 0o644


def test_sensu_is_installed(host):
    openjdk = host.package("sensu-go-agent")
    assert openjdk.is_installed


def test_sensu_agent_enabled(host):
    sensu = host.service("sensu-agent")
    assert sensu.is_enabled