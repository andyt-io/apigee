import xml.etree.ElementTree as ET
import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apigee Proxy Dependency Scanner")
    parser.add_argument(
        "-f", "--folder", help="Path to the root folder containing proxy bundles"
    )
    args = parser.parse_args()

    root_folder = args.folder or "./"  # Default if not provided

def scan_proxy_bundle(proxy_path):
    dependencies = {
        "kvms": [],
        "proxies": [],
        "targets": []
    }

    # Process Policies 
    policies_path = os.path.join(proxy_path, "policies")
    if os.path.exists(policies_path):
        print(policies_path)
        for policy_file in os.listdir(policies_path):
            process_policy(os.path.join(policies_path, policy_file), dependencies)

    # ... (similarly process 'targets' folder) ...

    return dependencies

def process_policy(policy_file, dependencies):
    tree = ET.parse(policy_file)
    root = tree.getroot()
    


    # Find KVMValueMapOperations references
    if root.tag == 'KeyValueMapOperations':
        if root.get('mapIdentifier') not in dependencies["kvms"]:
            dependencies["kvms"].append(root.get('mapIdentifier'))
    # for kvm_ref in root.findall('.//KeyValueMapOperations'): 
        #if kvm_ref.get('variableName').startswith('kvm.'):
        #    dependencies["kvms"].append(kvm_ref.get('variableName'))
        
      
        # Shared Flow References
    #for flowcallout in root.findall('.//FlowCallout'): 
    #    sharedflow_name = flowcallout.find('SharedFlowBundle').text
    #    dependencies["sharedflows"].append(sharedflow_name)

    # Target Server References
    #for service_callout in root.findall('.//ServiceCallout'): 
    #    targetserver_name = service_callout.get('request') 
        # (Handle cases where target server might be a variable)
    #    dependencies["targetservers"].append(targetserver_name)

    # References
    #for reference_el in root.findall('.//Reference'):
    #    ref_name = reference_el.get('ref')
    #    dependencies['references'].append(ref_name)

# Main Scan Logic
all_dependencies = {}

for bundle_folder in os.listdir(root_folder):
    bundle_path = os.path.join(root_folder, bundle_folder)
    if os.path.isdir(bundle_path):
        proxy_name = os.path.basename(bundle_folder)  # Use folder name as proxy name
        dependencies = scan_proxy_bundle(bundle_path+"/apiproxy/")
        all_dependencies[proxy_name] = dependencies

print(all_dependencies)
