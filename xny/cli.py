import argparse
from cache import update_cache
from fetch import fetch
from utils import fzf
from fetch import CACHE_DIR
from pathlib import Path

def ensure_cache_initialized():
    cache_path = Path(CACHE_DIR)
    if not cache_path.exists():
        print(f"|--> Cache directory {CACHE_DIR} not found. Initializing...")
        update_cache()

def main():
    parser = argparse.ArgumentParser(description="Learn X in Y Minutes CLI")
    parser.add_argument("--update", action="store_true", help="Update cache")
    parser.add_argument("--fzf", action="store_true", help="Open fzf selector")
    parser.add_argument("topic", nargs="?", type=str, help="Name of the Language or Resource")

    args, unknown_args = parser.parse_known_args()

    ensure_cache_initialized()

    if unknown_args:
        print("|--> Unrecognized arguments:\n" + "\n".join(f" {arg}" for arg in unknown_args) + "\n")
        parser.print_help()
    elif args.update:
        update_cache()
    elif args.fzf or not args.topic:
        matches = [(str(f), 1.0) for f in Path(CACHE_DIR).glob('*.md')]
        fzf(matches)
    elif args.topic:
        fetch(args.topic)
    else:
        print(f"|--X Something unexpected happened")

if __name__ == "__main__":
    main()
