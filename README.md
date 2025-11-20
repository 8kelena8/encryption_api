# encryption_api
Flask encryption API for secure exchange of confidential information between two systems.

Code for setting the API as a daemon in a Red Hat Server (it requires the creation of a virtual environment with the requirement file)
[Unit]
Description=Encryption API
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/api_encrypt
ExecStart=/var/www/api_encrypt/venv/bin/python server.py
Restart=always

[Install]
WantedBy=multi-user.target
