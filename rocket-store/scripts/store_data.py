import sys
import json
from Rocketstore import Rocketstore

def main():
    if len(sys.argv) < 3:
        print("Usage: python store_data.py <operation> <collection> [key] [data_json]")
        sys.exit(1)

    operation = sys.argv[1].lower()
    collection = sys.argv[2]
    
    rs = Rocketstore()
    # Optional: configure storage area
    # rs.options(data_storage_area="./rocket_db", data_format=Rocketstore._FORMAT_MARKDOWN)

    if operation == "post":
        key = sys.argv[3]
        data = json.loads(sys.argv[4])
        result = rs.post(collection, key, data, Rocketstore._FORMAT_MARKDOWN)
        print(json.dumps(result))
    elif operation == "get":
        key = sys.argv[3] if len(sys.argv) > 3 else "*"
        result = rs.get(collection, key)
        print(json.dumps(result))
    elif operation == "delete":
        key = sys.argv[3] if len(sys.argv) > 3 else None
        result = rs.delete(collection, key)
        print(json.dumps(result))
    else:
        print(f"Unknown operation: {operation}")

if __name__ == "__main__":
    main()
