<seotitle>Infrastructure as Code: Terraform</seotitle>
<seodescription>Deploy Meraki environments as code using Terraform and the Meraki Dashboard API.</seodescription>

# Terraform

## Introduction

Terraform is an Infrastructure-as-Code provisioning tool created by Hashicorp, widely used across IT roles from system administrators to developers. The Meraki Terraform Provider is tailored to work with the Cisco Meraki Dashboard API, providing a powerful and simple **Infrastructure-as-Code** solution.  

More info: [Meraki Terraform Provider - Documentation](https://registry.terraform.io/providers/cisco-open/meraki/latest/docs)

## Terraform Basics

A Terraform provider is a plugin that enables Terraform to interact with specific types of cloud, infrastructure, or service providers to provision and manage resources.

A Terraform configuration file is a text file written in HashiCorp Configuration Language (HCL) that defines the infrastructure resources and their desired state for provisioning and management using Terraform.
Terraform configuration files can be saved, shared, or reused, which ensures consistent execution of tasks and codifies operational knowledge.

## Prerequisites

- Terraform 0.13.x
- Go 1.21 (to build the provider plugin)

## Installation


1. **Install Terraform**

    *On a Mac*
    ```bash
    brew tap hashicorp/tap
    brew install hashicorp/tap/terraform
    ```

    *On Ubuntu*
    ```bash
    wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt update && sudo apt install terraform
    ```

    *On CentOS*
    ```bash
    sudo yum install -y yum-utils
    sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
    sudo yum -y install terraform
    ```

    More info: [Terraform Installation docs](https://developer.hashicorp.com/terraform/install).

2. **Install The Meraki Terraform Provider**

    To install this provider, copy and paste this code into your Terraform configuration.

    ```
        terraform {
        required_providers {
            meraki = {
            source = "cisco-open/meraki"
            version = "0.1.0-alpha"
            }
        }
        }

        provider "meraki" {
        # Configuration options
        }    
    ```
    Then, run:
    ```bash
    terraform init
    ```

    More info: [Meraki Terraform Provider docs](https://registry.terraform.io/providers/cisco-open/meraki/latest/)


## How to Use

Once you have everything installed, obtain your Meraki API key, set your authentication up and start building your first Terraform configuration file.

### API Authentication

The easiest way to provide access to your Meraki infrastracture is by setting your API key to an environment variable. 

1. **Environment Variable**

    In your terminal, set your [Meraki API key]((https://developer.cisco.com/meraki/api-v1/authorization/)) to an environment variable.

    ```bash
    export MERAKI_DASHBOARD_API_KEY=YOUR_API_KEY_HERE
    ```




### Your First Terraform Execution Plan

The best way to get started using Terraform is to run execution plans. All Terraform plans are written in HCL (Hashicorp Configuration Language). HCL is very similar to the JSON format.

In this example, we will be gathering the identity of the administrator associated with this Meraki API key and then print the name and email. We will then return a list of the Meraki organization names this administrator can manage.

1. **Develop the Plan**

    Create a file called `who_am_i.tf` and copy the following code into it.

    ```
    terraform {
    required_providers {
        meraki = {
        source = "cisco-open/meraki"
        version = "0.1.0-alpha"
        }
    }
    }

    provider "meraki" {
    }

    data "meraki_administered_identities_me" "example" {
    }

    output "meraki_administered_identities_me_example" {
    value = data.meraki_administered_identities_me.example.item
    }
    ```

2. **Execute the Plan**

    These command run the Terraform Plan. Note that `terraform init` is required only for the first time we initialize the plan.

    ```bash
    terraform init
    terraform plan
    ```

3. **Results**

    The terminal should display our results as each task is completed. If you run into any issues, check your spacing, or refer to the Troubleshooting section in this guide. 

    ```bash
    > terraform init

    Initializing the backend...


    Initializing provider plugins...



    Finding cisco-open/meraki versions matching "0.1.0-alpha"...
    r- Installing cisco-open/meraki v0.1.0-alpha...

    Installed cisco-open/meraki v0.1.0-alpha (self-signed, key ID 535815BB4B6133C1)


    Partner and community providers are signed by their developers.
    If you'd like to know more about provider signing, you can read about it here:
    https://www.terraform.io/docs/cli/plugins/signing.html


    Terraform has created a lock file .terraform.lock.hcl to record the provider
    selections it made above. Include this file in your version control repository
    so that Terraform can guarantee to make the same selections by default when
    you run "terraform init" in the future.


    Terraform has been successfully initialized!


    You may now begin working with Terraform. Try running "terraform plan" to see
    any changes that are required for your infrastructure. All Terraform commands
    should now work.


    If you ever set or change modules or backend configuration for Terraform,
    rerun this command to reinitialize your working directory. If you forget, other
    commands will detect it and remind you to do so if necessary.



    terraform plan
    data.meraki_administered_identities_me.example: Reading...
    data.meraki_administered_identities_me.example: Read complete after 1s



    Changes to Outputs:



    meraki_administered_identities_me_example = {

    authentication         = {

    api        = {

    key = {

    created = true
    }
    }





    mode       = "email"

    saml       = {

    enabled = false
    }



    two_factor = {

    enabled = true
    }
    }





    email                  = "meraki@example.com"

    last_used_dashboard_at = "2024-03-27T17:18:34.000000Z"

    name                   = "Meraki Miles"
    }




    You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.


    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


    Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
    ```

**Success! Now you have a working Meraki Terraform Provider and can begin configuring your Infrastructure as Code!** 

Explore more example [plans](https://github.com/cisco-open/terraform-provider-meraki/tree/main/examples/samples).

## Resources

- [Documentation](https://registry.terraform.io/providers/cisco-open/meraki/latest/docs)

- [GitHub](https://github.com/cisco-open/terraform-provider-meraki)

- [Learning Lab](https://developer.cisco.com/learning/labs/meraki-dashboard-terraform/introduction/)


## Contributions and Feedback

For issues, or enhancements, please [open an issue ](https://github.com/cisco-open/terraform-provider-meraki/issues).
For contributions, kindly read our [contribution doc](https://github.com/cisco-open/terraform-provider-meraki/blob/main/CONTRIBUTING.md)

## Release Management

We adhere to [Semantic Versioning](https://semver.org/). Version updates will align with Cisco Meraki product updates, REST API changes, and Terraform releases.

