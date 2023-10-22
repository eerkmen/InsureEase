from database import get_db_connection

def create_client():
    client={"name":"test"}
    return client

def get_all_clients():
    clients=[{"name":"test"}]
    return clients


def get_client_by_id(clientId):
    client={"name":"test"}
    return client

def update_client(clientId):
    client={"name":"test"}
    return client


def get_all_policies():
    policies=[{"name":"test"}]
    return policies

def get_policies_by_type(keyword):
    policies=[{"name":"test"}]
    return policies

def add_policy_to_client():
    client_policy={"name":"test"}
    return client_policy

def get_policies_by_client(clientId):
    client_policy={"name":"test"}
    return client_policy

def submit_claim():
    claim={"name":"test"}
    return claim
