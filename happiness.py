#!/usr/bin/env python3
import argparse
import collections
import csv
import datetime
import pathlib
import random
import time

EMPTY_SALUTATION = ""
MAX_DELAY_SECONDS = 3


def get_args():
    """Return command-line arguments."""
    parser = argparse.ArgumentParser(description="Wishes you happy days.")
    parser.add_argument(
        "-d", "--days", type=pathlib.Path,
        help="csv file of special days",
    )
    parser.add_argument(
        "-s", "--salutations", type=pathlib.Path,
        help="text file of salutations to add at beginning of greeting",
    )
    return parser.parse_args()


def get_happiness(days_config):
    """Return a "Happy <day>!" string allowing for special days."""
    today = datetime.date.today()
    if days_config:
        with days_config.open("r", newline="") as f:
            days = collections.defaultdict(list)
            reader = csv.DictReader(f)
            for line in reader:
                date = datetime.datetime.strptime(line["date"], "%Y-%m-%d").date()
                days[date].append(line["text"])
        try:
            return " and ".join(days[today])
        except KeyError:
            pass
    return f"Happy {today:%A}!"  # Default to weekday name, e.g., Monday.


def get_random_salutation(salutations_config):
    """Return a uniformly random salutation from a text config file."""
    salutations = [EMPTY_SALUTATION]
    if salutations_config:
        with salutations_config.open("r") as f:
            salutations.extend(line.strip() for line in f)
    return random.choice(salutations)


def main():
    """Wish the user happy days."""
    args = get_args()
    happiness = get_happiness(args.days)
    salutation = get_random_salutation(args.salutations)
    if salutation != EMPTY_SALUTATION:
        # Salutations are responsible for any punctuation they need.
        happiness = f"{salutation} {happiness}"
    # Try to give the user a small, pleasant surprise.
    # Planning to use more for automated, chat bot applications.
    delay_seconds = random.randrange(MAX_DELAY_SECONDS)
    time.sleep(delay_seconds)
    print(happiness)


if __name__ == "__main__":
    main()
