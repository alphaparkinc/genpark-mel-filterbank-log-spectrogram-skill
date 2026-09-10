import sys
import json
from client import MelFilterbank

mfb = MelFilterbank()

def handle_call(name, arguments):
    if name == "get_filterbank":
        n_f = arguments.get("num_filters", 4)
        sr = arguments.get("sample_rate", 8000)
        return {"filterbank": mfb.compute_filterbank(n_f, 16, sr)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
