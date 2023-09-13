
# Ansible

## Introduction

Ansible is an open-source automation tool sponsored by Red Hat, widely used across IT roles from system administrators to developers. This document describes an Ansible Collection tailored to work with the Cisco Meraki Dashboard API. An Ansible Collection is a package format that bundles various Ansible content types, such as playbooks, roles, modules, and plugins. These collections can be shared and installed through platforms like Ansible Galaxy or other Galaxy servers, such as Pulp 3.

## Understanding Ansible Playbooks

An Ansible Playbook serves as a blueprint for automation tasks. It outlines the steps that Ansible will execute on specified inventories or groups of hosts. A playbook comprises 'plays,' which are ordered groupings of tasks. Each task is executed by an Ansible module that encapsulates the logic and parameters for that task. Playbooks can be saved, shared, or reused, which ensures consistent execution of tasks and codifies operational knowledge.

## Pre-requisites

- Ansible version 2.9 or higher
- Python version 3.6 or higher
- [Python Meraki SDK v1.33.0](https://github.com/meraki/dashboard-api-python) or newer

## Installation and Configuration

### Installation Steps

1. **Install Ansible**
    ```bash
    pip install ansible
    ```
    *or on a Mac*
    ```bash
    brew install ansible
    ```

    **(Optional with Virtual Environment)**
        Create a virtual environment for ansible to run in

    ```bash
    python3 -m venv ansible
    source ansible2.9/bin/activate
    ```

2. **Install Python Meraki SDK**
    ```bash
    pip install meraki
    ```
    *or on a Mac*
    ```bash
    pip3 install meraki
    ```

3. **Install Ansible Collection**
    ```bash
    ansible-galaxy collection install cisco.meraki -f
    ```

### Additional Configuration Options

Ansible supports multiple sources for configuring its behavior, including configuration files, environment variables, command-line options, playbook keywords, and variables. Configuration files are sought in the following order:

1. `ANSIBLE_CONFIG` environment variable, if set
2. `ansible.cfg` in the current directory
3. `~/.ansible.cfg` in the home directory
4. `/etc/ansible/ansible.cfg`

Ansible will use the first configuration file it finds from this list, ignoring the others.

Below is an example `ansible.cfg` file with configuration options specific to the Cisco Meraki Ansible collection:

```yaml
---
meraki_api_key: "ABC"
meraki_base_url: "https://api.meraki.com/api/v1"
meraki_single_request_timeout: ""
meraki_certificate_path: ""
meraki_requests_proxy: True
meraki_wait_on_rate_limit: 60
meraki_nginx_429_retry_wait_time: 60
meraki_action_batch_retry_wait_time: 60
meraki_retry_4xx_error: False
meraki_retry_4xx_error_wait_time: 60
meraki_maximum_retries: 2
meraki_output_log: True
meraki_log_file_prefix: "meraki_api_"
meraki_log_path: ""
meraki_print_console: True
meraki_suppress_logging: False
meraki_simulate: False
meraki_be_geo_id: ""
meraki_caller: ""
meraki_use_iterator_for_get_pages: False
meraki_inherit_logging_config: False
```

## How to Use

### API Authentication

1. **Environment Variable**
    ```bash
    export MERAKI_DASHBOARD_API_KEY=YOUR_API_KEY_HERE
    ```

**(Alternative Authentication Options)**

2. **Credentials File**
    - Create a `credentials.yml` file.
        - Refer to this [example](https://github.com/meraki/dashboard-api-ansible/blob/main/playbooks/credentials.yml).
    - Encrypt it, with Anisble Vault! 
    ```
    $ ansible-vault encrypt credentials.yml
    ```
    - Learn more about securing and using your Ansible credentials [here](https://docs.ansible.com/ansible/latest/vault_guide/index.html).



3. **Ansible Configuration File**
    - Create or use our exsiting `ansible.cfg` file.
    - Refer to this [Ansible doc](https://docs.ansible.com/ansible/latest/reference_appendices/config.html).

    > **Security Alert:** This option could store API keys in plain text, which is not recommended.


### Example Playbook

1. **Create a `hosts` File**
    ```bash
    [meraki_servers]
    meraki_server
    ```

2. **Develop the Playbook**
Create a file called `myplaybook.yml`
    ```yml
    ---
    - hosts: localhost
    gather_facts: false
    tasks:
        - name: Get administered _identities _me
        cisco.meraki.administered_identities_me_info:
            meraki_suppress_logging: true
        register: me

        - name: Show current Meraki administrator
        ansible.builtin.debug:
            msg: "{{ me.meraki_response.name }} - {{me.meraki_response.email}}"
        
        - name: Get all Organizations
        cisco.meraki.organizations_info:
            meraki_suppress_logging: true
        register: result
        - name: Show Organizations List
        ansible.builtin.debug:
            msg: "{{ result | json_query('meraki_response[*].name') }}"
    ```

3. **Execute the Playbook**

    ```bash
    ansible-playbook -i hosts myplaybook.yml
    ```

This command runs the playbook, targeting the hosts defined in the `hosts` file and performing the tasks specified in `myplaybook.yml`.

4. **Results**

```
PLAY [localhost] ******************************************************************************************************************

TASK [Get all administered _identities _me] ******************************************************************************************************************
ok: [localhost]

TASK [Show current Meraki administrator] ******************************************************************************************************************
ok: [localhost] => {
    "msg": "Miles Meraki - miles@meraki.com"
}

TASK [Get all Organizations] ******************************************************************************************************************
ok: [localhost]

TASK [Show Organizations List] ******************************************************************************************************************
ok: [localhost] => {
    "msg": [
        "Test",
        "API-Test",
        "Sample Company",
        "Sample Org Inc.",
        "Support Lab Test"
    ]
}

PLAY RECAP *******************************************************************************************************************************************************************************************************
localhost                  : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0     

```

**Success! Now you have a working Meraki Ansible collection and can begin automating your cloud networks!** 

## Additional Information

- [Ansible Using Collections Documentation](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)

## macOS Troubleshooting

If you encounter `objc_initializeAfterForkError` or `ERROR! A worker was found in a dead state` errors on macOS, set the following environment variable:

```bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

## Contributions and Feedback

For contributions, issues, or enhancements, please [open an issue or create a PR](https://github.com/meraki/dashboard-api-ansible/issues).

## Release Management

We adhere to [Semantic Versioning](https://semver.org/). Version updates will align with Cisco Meraki product updates, REST API changes, and Python SDK releases.

