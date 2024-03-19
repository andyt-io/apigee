import xml.etree.ElementTree as ET
import os

def scan_proxy_bundle(proxy_path):
    dependencies = {
        "kvms": [],
        "proxies": [],
        "targets": []
    }

    # Process Policies 
    policies_path = os.path.join(proxy_path, "policies")
    if os.path.exists(policies_path):
        for policy_file in os.listdir(policies_path):
            process_policy(os.path.join(policies_path, policy_file), dependencies)

    # ... (similarly process 'targets' folder) ...

    return dependencies

def process_policy(policy_file, dependencies):
    tree = ET.parse(policy_file)
    root = tree.getroot()

    # Find KVM references
    for kvm_ref in root.findall('.//AssignTo[@variableName]'): 
        if kvm_ref.get('variableName').startswith('kvm.'):
            dependencies["kvms"].append(kvm_ref.get('variableName'))

    # ... (add logic to find proxy references, target endpoint references) ...

# Main Scan Logic
root_folder = "/path/to/proxy/bundles"
all_dependencies = {}

for bundle_folder in os.listdir(root_folder):
    bundle_path = os.path.join(root_folder, bundle_folder)
    if os.path.isdir(bundle_path):
        proxy_name = os.path.basename(bundle_folder)  # Use folder name as proxy name
        dependencies = scan_proxy_bundle(bundle_path)
        all_dependencies[proxy_name] = dependencies

print(all_dependencies)