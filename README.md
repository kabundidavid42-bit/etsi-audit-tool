ETSI Audit Tool

A simple Python script to check if a website or IP meets the ETSI EN 303 645 TLS security standard.

Getting Started
Clone or download the repository
You can use Git or download the ZIP from GitHub.

Create a Python virtual environment

python -m venv venv
Activate the virtual environment

Windows:

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate

Run the audit script

python audit.py

Enter the domain or IP
When prompted, type the website (e.g., google.com) or an IP address to check its TLS compliance.
Notes
Only the audit.py file is required. Do not upload the venv folder to GitHub.
The script will indicate whether the target is PASS, FAIL, or INCONCLUSIVE based on its TLS configuration.
Errors may occur if the site restricts access or has unusual configurations.
Example Output
Enter domain or IP (e.g. google.com): example.com

=== ETSI Compliance Result ===
Provision: 5.1-1
Check: Secure Communication (TLS)
Status: PASS
Protocol: TLSv1.3
Cipher: TLS_AES_256_GCM_SHA384
