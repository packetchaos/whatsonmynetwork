# whatsonmynetwork
Show the Assets found in the last 30 days from Tenable.sc

# Download the Repository
Clone the repository to your local machine

    git clone https://github.com/packetchaos/whatsonmynetwork.git

# Update the Script
You will need to update the script SC_newHost.py with your SC credentials
    
    # Set User data
    hostname = "<your T.sc IP address>"
    username = "<your User Name>"
    password = "<your password>"
    
# Build the docker container
    docker build -t silentninja/newhost:latest .

# Run the docker container
    docker run -d -p 5001:5001 silentninja/newhost:latest
    
# View the Web SPA
Navigate to http://127.0.0.1:5001



