# AGCDN Terraform - Adding Sites & Activating Domains (Simplified)
This guide helps you add a site to AGCDN using Terraform and activate its custom domain.

###### Prerequisites (Things You Need Before Starting)
- Basic Understanding of AGCDN & Terraform – You should know how AGCDN works and have Terraform access.
- Terminus Installed – A tool used to interact with Pantheon.
- Admin Cookie Set Up – A session cookie required for authentication.
- Pantheon Employee Certificate – Needed for secure communication.
- Pantheon CA Cert – Also required for secure communication.

######  Steps: Access to Ygg – A tool used to enable/disable AGCDN for a domain.
- Step 1 - Gather Required Information
Before starting, you need:
  - Site UUID (Unique ID) or Site Name – Used to identify the site.
  - Machine Name Directory in Terraform Repo – The folder where site info is stored.

- Step 2 - Update the sites.json File
- The sites.json file is where new site entries are added. This file needs to be updated and merged into the main repository before deployment.

- How to Add a Site?
  - You can add a site using either of these methods:

  - ###### 2.1 Using streamlined_single.py (For One Site)
    - This script adds a single site entry. Command:
      - python scripts/streamlined_single.py <machine_name_folder> <site_name>
    - Example:
      - python scripts/streamlined_single.py nestle_all dig0049398-petcare-purina-ecuador

- ###### Using streamlined.py (For Multiple Sites)
  - This script adds multiple sites from an organization. Command:
  python scripts/streamlined.py <machine_name_folder>
  - Example (for all environments: live, test, dev, multidevs):
    - python scripts/streamlined.py <machine_name_folder> all

- ###### Step 3 - Apply Changes to the Service
  - Once the sites.json file is updated, it needs to be merged into the main branch and deployed.

- ###### Step 4 Merging the File (Creating a Pull Request)
  - A Pull Request (PR) is required to review and approve changes.
  - Make sure no existing Site UUIDs are deleted, or it may break AGCDN.
  - ###### Step 4 Deploying the Changes
    - Once the PR is merged, apply the changes using one of these methods:
    - ###### 4.1 Via Github CLI (Command Line) Run this command in your local machine:
      - gh workflow run service-plan.yml -f apply=true -f service_name={{ machine_name }}
    - ###### 4.2 Via Github Actions (Web Interface):
      - Go to the GitHub Actions page.
      - Open service-plan.yml.
      - Enter the machine_name and select Apply.

- ###### Step 5 - Activate the Domain
  - This step makes the domain live on AGCDN.
    - Method 1: Using Direct Bash Command
    - Find the pan-enable.txt file in the repo. Run this command:
    bash -c "ssh -o SendEnv='LC_ALL LANG' yggdrasil-12fe1f82.panth.io pantheon sites.enable_agcdn:<domain-name> | sed '1d' | sed '$ d' "
    - Method 2: Using Ygg
    Log in to Ygg:
      - ssh yggdrasil-12fe1f82.panth.io
      - Run the enable command:
        - pan sites.enable_agcdn:<domain-name>

Final Thoughts
- Make sure you have all the required information before starting.
- Carefully update the sites.json file and create a PR.
- Use the correct method to deploy and activate the domain.