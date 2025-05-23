import os

def set_jenkins_connection():
    # Simulate environment variables
    os.environ["INFLUXDB_USERNAME"] = "example_user"
    os.environ["INFLUXDB_PASSWORD"] = "example_password"

    username = os.environ["INFLUXDB_USERNAME"]
    influxdb = os.environ["INFLUXDB_PASSWORD"]

    print("INFLUXDB_USERNAME: %s" % username)
    print("INFLUXDB_PASSWORD: %s" % influxdb)

    # Common patterns that may trigger secret detection tools
    # You can comment/uncomment to test different cases
    
    # Case 1: Hardcoded secret
    # password = "hardcoded_secret"

    # Case 2: Assigned from env variable directly
    password = influxdb  # Still flagged by some scanners

    # Case 3: Indirect assignment
    db_config = {
        "username": username,
        "password": password  # This might also be flagged
    }

    # Simulate DB client call
    client = f"Connecting to DB with username={db_config['username']} and password={db_config['password']}"

    return client

if __name__ == "__main__":
    result = set_jenkins_connection()
    print(result)
