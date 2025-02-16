import json

with open(r"c:\Users\Acer Aspire Lite\pp2\labs_pp2\lab4\json\sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 85)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU'}")
print("-" * 85)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""  
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu}")