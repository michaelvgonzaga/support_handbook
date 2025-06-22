# Terraform - Adding AGCDN  Sites & Activating Domains (Simplified)
This guide helps you add a site to AGCDN using Terraform and activate its custom domain.

###### Prerequisites (Things You Need Before Starting)
* Terraform access, Terminus installed
* Admin cookie + Pantheon certs configured

###### Gather Info
* Site UUID or Site Name
* machine_name_folder (from repo)

###### Add Sites to sites.json
* clone repo
* git checkout -b service/{org_dir}/{your-name}
* Add Site to sites.json
* Commit and push the change.
* Create PR
  * Open PR with the updated sites.json
  * Don't delete any existing UUIDs

###### Run Service Plan (Required)
* via cli:
  * gh workflow run service-plan.yml -f apply=true -f service_name=<machine_name>
* via web:
  * go here https://github.com/pantheon-systems/tf-agcdn/actions/workflows/service-plan.yml
  * Click Run workflow
  * Set machine_name and apply=true
 
###### Activate domain
* ssh yggdrasil-12fe1f82.panth.io
* pan sites.enable_agcdn:<domain-name>
