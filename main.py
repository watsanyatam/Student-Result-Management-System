import argparse
import sys

from app.cli import DEFAULT_DATA_PATH, ResultApp
from app.exceptions import StorageError


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Student Result & Grade Management System"
    )
    parser.add_argument(
        "--data",
        default=DEFAULT_DATA_PATH,
        help=f"JSON data file (default: {DEFAULT_DATA_PATH})",
    )
    args = parser.parse_args(argv)

    try:
        app = ResultApp(data_path=args.data)
    except StorageError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    app.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
