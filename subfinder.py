import subprocess
import argparse
import json

def find_subdomains_with_nslookup(domain, wordlist_file):
    subdomains = []
    try:
        with open(wordlist_file, 'r') as file:
            for line in file:
                subdomain = f"{line.strip()}.{domain}"
                try:
                    result = subprocess.run(
                        ["nslookup", subdomain],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )

                    if "Name:" in result.stdout:
                        subdomains.append({"subdomain": subdomain, "status": "resolved"})
                        print(f"Found: {subdomain}")
                    else:
                        subdomains.append({"subdomain": subdomain, "status": "unresolved"})

                except Exception as e:
                    subdomains.append({"subdomain": subdomain, "status": f"error: {e}"})
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_file}' not found.")
    return subdomains

def save_to_json_file(data, output_file):
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"\nResults saved to {output_file}")
    except Exception as e:
        print(f"Error saving to JSON file: {e}")

def parse_json_file(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        print("\nParsed JSON Logs:")
        for entry in data:
            print(f"Subdomain: {entry['subdomain']}, Status: {entry['status']}")
    except Exception as e:
        print(f"Error parsing JSON file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find subdomains using nslookup and save to JSON.")
    parser.add_argument("-target", required=True, help="The target domain to search for subdomains (e.g., example.com).")
    parser.add_argument("-wordlist", required=True, help="Path to the wordlist file containing potential subdomain names.")
    parser.add_argument("-output", required=True, help="Path to save the JSON file with results.")
    args = parser.parse_args()

    target_domain = args.target
    wordlist_path = args.wordlist
    output_path = args.output

    print(f"\nSearching for subdomains of {target_domain} using nslookup...\n")

    found_subdomains = find_subdomains_with_nslookup(target_domain, wordlist_path)

    save_to_json_file(found_subdomains, output_path)

    parse_json_file(output_path)
