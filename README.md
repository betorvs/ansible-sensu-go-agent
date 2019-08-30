Role Name
=========

TravisCI: [![Build Status](https://travis-ci.org/betorvs/ansible-sensu-go-agent.svg?branch=master)](https://travis-ci.org/betorvs/ansible-sensu-go-agent)

Install sensu-go-agent in servers


Role Variables
--------------

Variables to configure sensu agent like backend, ssl, namespace and sudo access. Probably you need to change this values for your environment.

```yml
sensuGo_backend_url: "localhost"
sensuGo_ssl: False
sensuGo_namespace: default
sensuGo_sudo_access: False
```

Basic variables to install sensu go agent and plugins. You can keep default values.

```yml
sensuGo_agent_repo: 
sensuGo_agent_gpgkey: 
sensuGo_plugins_repo: 
sensuGo_plugins_gpgkey: 
sensuGo_plugins_bin_path: "/opt/sensu-plugins-ruby/embedded/bin"
```

Variables to configure labels style "key:value". Configure per server to have specifically labels.

```yml
sensuGo_labels:
  docs: "https://docs.sensu.io/sensu-go/latest"
```

Variables to install plugins

```yml
sensuGo_plugin_elasticsearch: ""
sensuGo_plugin_http: ""
sensuGo_subscriptions_active: false
sensuGo_plugin_k8s: ""
sensuGo_plugin_rabbitmq: ""
sensuGo_plugin_redis: ""
sensuGo_plugin_mysql: ""
sensuGo_clean_docker: ""
```

Example Playbook
----------------

Import this inside our roles directory and import in your playbook:

    - hosts: servers
      roles:
         - { role: ansible-sensu-go-agent }

License
-------

MIT

Author Information
------------------

Roberto Scudeller beto.rvs@gmail.com
