from pymisp import PyMISP
from dotenv import load_dotenv
import os

load_dotenv()

misp_url = os.getenv("MISP_URL")
misp_key = os.getenv("MISP_API_KEY")

hash_value = "14b03ac41b5ef44ca31790fefb23968f2525c3aabfe11e96b9b1ccb6215eb8be"

misp = PyMISP(misp_url, misp_key, ssl=False)

result = misp.search(
    controller="attributes",
    value=hash_value
)

attributes = result.get("Attribute", [])

print("\n=== MISP IOC ENRICHMENT RESULT ===\n")
print(f"IOC Type: SHA256")
print(f"IOC Value: {hash_value}")
print(f"MISP Matches: {len(attributes)}")

if not attributes:
    print("\nAssessment: No MISP match found.")
    print("Recommendation: Continue investigation using local telemetry and behavioral analysis.")
else:
    for attr in attributes:
        event = attr.get("Event", {})
        threat_level = event.get("ThreatLevel", {}).get("name", "Unknown")

        print("\n--- Match Found ---")
        print(f"Event ID: {event.get('id')}")
        print(f"Event Info: {event.get('info')}")
        print(f"Category: {attr.get('category')}")
        print(f"Type: {attr.get('type')}")
        print(f"Comment: {attr.get('comment')}")
        print(f"To IDS: {attr.get('to_ids')}")
        print(f"Threat Level: {threat_level}")
        print(f"Source Org: {event.get('Orgc', {}).get('name')}")

    print("\nAssessment: IOC matched threat intelligence in MISP.")
    print("Recommendation: Escalate for additional telemetry review and behavioral analysis.")
