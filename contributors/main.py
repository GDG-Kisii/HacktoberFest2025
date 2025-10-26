import argparse
from project_tracker import ProjectTracker

def main():
    parser = argparse.ArgumentParser(description="Hacktoberfest 2025 Project Tracker CLI")
    parser.add_argument("--enable-notifications", action="store_true", help="Enable email notifications")
    parser.add_argument("--add-contributor", nargs=3, metavar=('NAME','USERNAME','EMAIL'), help="Add a new contributor")
    parser.add_argument("--add-contribution", nargs=4, metavar=('USERNAME','REPO','TYPE','MESSAGE'), help="Add contribution")
    
    args = parser.parse_args()

    tracker = ProjectTracker(enable_notifications=args.enable_notifications)

    if args.add_contributor:
        name, username, email = args.add_contributor
        tracker.add_contributor(name, username, email)

    if args.add_contribution:
        username, repo, ctype, message = args.add_contribution
        tracker.add_contribution(username, repo, ctype, message)

if __name__ == "__main__":
    main()
