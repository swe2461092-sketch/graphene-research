import argparse, json, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="runs/graphene")
    parser.add_argument("--output", default="experiments/convergence")
    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    jobs = []
    for i, ecut in enumerate([30, 40, 50, 60, 70, 80, 90, 100], 1):
        fname = f"scf_ecut_{ecut}.in"
        with open(os.path.join(args.output, fname), "w") as f:
            f.write(f"! Convergence test ecutwfc={ecut}\n")
        jobs.append({"id": i, "file": fname, "ecutwfc": ecut, "status": "NOT_RUN"})
    with open(os.path.join(args.output, "manifest.json"), "w") as f:
        json.dump({"jobs": jobs}, f, indent=2)
    print(f"Prepared {len(jobs)} input files in {args.output}.")
    print("NO CALCULATIONS EXECUTED.")

if __name__ == "__main__":
    main()
