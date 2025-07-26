# country_picker/__main__.py

from .cli import parse_args
from .main_window import start_app

def main():
    args = parse_args()
    start_app(preselect_country=args.select)

if __name__ == "__main__":
    main()
