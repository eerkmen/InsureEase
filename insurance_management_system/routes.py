from flask import Blueprint, jsonify
from insurance_management_system.service import create_client,get_all_clients,get_client_by_id,update_client,get_all_policies,get_policies_by_type,add_policy_to_client,get_policies_by_client,submit_claim


insurance_management_system_bp = Blueprint('insurance_management_system', __name__)

@insurance_management_system_bp.route("/clients", methods=["POST"])
def create_client_func():
    client = create_client()
    return jsonify(client)

@insurance_management_system_bp.route("/clients", methods=["GET"])
def get_all_clients_func():
    clients = get_all_clients()
    return jsonify(clients)

@insurance_management_system_bp.route("/clients/:clientId", methods=["GET"])
def get_client_by_id_func(clientId):
    client =get_client_by_id(clientId)
    return jsonify(client)

@insurance_management_system_bp.route("/clients/update/:clientId", methods=["POST"])
def update_client_func(clientId):
    client = update_client(clientId)
    return jsonify(client)

@insurance_management_system_bp.route("/policies", methods=["GET"])
def get_all_policies_func():
    policies =get_all_policies()
    return jsonify(policies)

@insurance_management_system_bp.route("/policies/type/:keyword", methods=["GET"])
def get_policies_by_type_func(keyword):
    policies = get_policies_by_type(keyword)
    return jsonify(policies)

@insurance_management_system_bp.route("/client-policy/add-policy-to-client", methods=["POST"])
def add_policy_to_client_func():
    client_policy = add_policy_to_client()
    return jsonify(client_policy)

@insurance_management_system_bp.route("/client-policy/policies-by-client/:clientId", methods=["GET"])
def get_policies_by_client_func(clientId):
    client_policy = get_policies_by_client(clientId)
    return jsonify(client_policy)

@insurance_management_system_bp.route("/claims", methods=["POST"])
def submit_claim_func():
    claim = submit_claim()
    return jsonify(claim)



