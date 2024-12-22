import argparse
from cache import update_cache

def main():
    parser = argparse.ArgumentParser(description="Learn X in Y Minutes CLI")
    parser.add_argument("--update", action="store_true", help="Update cache")

    args, unknown_args = parser.parse_known_args()

    if unknown_args:
        print("Unrecognized arguments:\n" + "\n".join(f" {arg}" for arg in unknown_args) + "\n")
        parser.print_help()
    elif args.update:
        update_cache()
    else:
        print(f"|--X Something unexpected happened")

if __name__ == "__main__":
    main()
