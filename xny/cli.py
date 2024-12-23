import argparse
from cache import update_cache
from fetch import fetch

def main():
    parser = argparse.ArgumentParser(description="Learn X in Y Minutes CLI")
    parser.add_argument("--update", action="store_true", help="Update cache")
    parser.add_argument("topic", type=str, help="Name of the Language or Resource")

    args, unknown_args = parser.parse_known_args()

    if unknown_args:
        print("Unrecognized arguments:\n" + "\n".join(f" {arg}" for arg in unknown_args) + "\n")
        parser.print_help()
    elif args.topic:
        fetch(args.topic)
    elif args.update:
        update_cache()
    else:
        print(f"|--X Something unexpected happened")

if __name__ == "__main__":
    main()
