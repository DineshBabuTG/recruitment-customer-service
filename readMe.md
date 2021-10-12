Run the following docker command to run the customer service container

docker run -d -p 8001:8001 -e dbhostname=<DB-Hostname> tgdinababu/customerapp:latest