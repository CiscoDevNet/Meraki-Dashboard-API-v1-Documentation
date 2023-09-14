
# Ansible

## Introduction

Ansible is an open-source automation tool sponsored by Red Hat, widely used across IT roles from system administrators to developers. This Ansible Collection is tailored to work with the Cisco Meraki Dashboard API, providing a powerful and simple **Infrastructure as Code** solution.  

More info: [Meraki Ansible Collection - Reference Guide](https://docs.ansible.com/ansible/latest/collections/cisco/meraki/index.html)

## Ansible Basics

An Ansible Collection is a package format that bundles various Ansible content types, such as playbooks, roles, modules, and plugins. 

A playbook serves as a blueprint for automation tasks. It outlines the steps that Ansible will execute on specified inventories or groups of `hosts`. A playbook comprises `plays`, which are ordered groupings of `tasks`. Each task is executed by an Ansible module that encapsulates the logic and parameters for that task. 

Playbooks can be saved, shared, or reused, which ensures consistent execution of tasks and codifies operational knowledge.

## Pre-requisites

- Ansible version 2.9 or higher
- Python version 3.6 or higher
- [Python Meraki SDK v1.33.0](https://github.com/meraki/dashboard-api-python) or newer

## Installation and Configuration


1. **Install Ansible**

    ```bash
    pip install ansible
    ```
    *or on a Mac*
    ```bash
    brew install ansible
    ```

    More info: [Ansible Installation docs](https://docs.ansible.com/ansible/latest/installation_guide/index.html).

2. **Install Python Meraki SDK**

    ```bash
    pip install meraki
    ```
    *or on a Mac*
    ```bash
    pip3 install meraki
    ```

    More info: [Meraki Python library docs](https://developer.cisco.com/meraki/api-v1/python/)

3. **Install Ansible Collection**

    ```bash
    ansible-galaxy collection install cisco.meraki -f
    ```

**(Alternative install with Virtual Environment)**
    
Create a virtual environment for Ansible and the Meraki API to run in.

```bash
python3 -m venv ansible
source ansible/bin/activate
pip3 install ansible
pip3 install meraki
ansible-galaxy collection install cisco.meraki -f
```

More info: [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) 
## How to Use

Once you have everything installed, obtain your Meraki API key, set your authentication up and start building your first Playbook.

### API Authentication

The easiest way to provide access to your Meraki infrastracture is by setting your API key to an environment variable. Ansible will use the Meraki python library to make the API requests with the provided key details.

1. **Environment Variable**

    In your terminal, set your [Meraki API key]((https://developer.cisco.com/meraki/api-v1/authorization/)) to an environment variable.

    ```bash
    export MERAKI_DASHBOARD_API_KEY=YOUR_API_KEY_HERE
    ```




### Playbooks

Let's build our first playbook.

In this example, we will be gathering the identity of the administrator associated with this Meraki API key and then print the name and email. We will then return a list of the Meraki organization names this administrator can manage.

1. **Hosts File**

    Create a file called `hosts` and copy the following code into it.

    ```bash
    [meraki_servers]
    meraki_server
    ```

2. **Develop the Playbook**

    Create a file called `myplaybook.yml` and copy the following code into it.

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

    This command runs the playbook, targeting the hosts defined in the `hosts` file and performs the tasks specified in `myplaybook.yml`.

    ```bash
    ansible-playbook -i hosts myplaybook.yml
    ```



4. **Results**

    The terminal should display our results as each task is completed. If you run into any issues, check your spacing, or refer to the Troubleshooting section in this guide. 

    ```bash
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

**Success! Now you have a working Meraki Ansible collection and can begin configuring your Infrastructure as Code!** 

Explore more example [playbooks](https://github.com/meraki/dashboard-api-ansible/tree/main/playbooks).

## Advanced Options

### Authentication

There are alternatives to providing your Meraki API key for use with the Ansible collection. 

1. **Credentials File**
- Create a `credentials.yml` file.
    - Refer to this [example](https://github.com/meraki/dashboard-api-ansible/blob/main/playbooks/credentials.yml).
- Encrypt it, with Anisble Vault! 

    ```bash
    $ ansible-vault encrypt credentials.yml
    ```
    More info: [Anisble Credentials Vault Guide](https://docs.ansible.com/ansible/latest/vault_guide/index.html).



2. **Configuration File**
    - Create or use an exsiting `ansible.cfg` file defined in the next section.
    - Set `meraki_api_key: "Your-API-Key"` to your API key
    
    More info: [Ansible Configurations](https://docs.ansible.com/ansible/latest/reference_appendices/config.html)

    > **Security Alert:** This option could store API keys in plain text, which is not recommended.

### **Ansible Configuration**

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
## Resources

- [Meraki Ansible Collection Documentation](https://docs.ansible.com/ansible/latest/collections/cisco/meraki/index.html)

- [Meraki Anisble Collection - Galaxy Hub](https://galaxy.ansible.com/cisco/meraki)

- [Meraki Ansible Collection - GitHub](https://github.com/meraki/dashboard-api-ansible)



- [Learning Lab](https://developer.cisco.com/learning/labs/meraki-dashboard-ansible/introduction/)

## Troubleshooting

### Mac OS 

If you encounter `ERROR! A worker was found in a dead state` or `objc_initializeAfterForkError`  errors, set the following environment variable:

```bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```



## Contributions and Feedback

For contributions, issues, or enhancements, please [open an issue or create a PR](https://github.com/meraki/dashboard-api-ansible/issues).

## Release Management

We adhere to [Semantic Versioning](https://semver.org/). Version updates will align with Cisco Meraki product updates, REST API changes, and Python SDK releases.

