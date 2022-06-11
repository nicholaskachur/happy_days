#!/usr/bin/env python3
import argparse
import datetime
import pathlib
import random
import time

EMPTY_GREETING = ""
MAX_DELAY_SECONDS = 3


def get_args():
    """Return command-line arguments."""
    parser = argparse.ArgumentParser(description="Wishes you happy days.")
    parser.add_argument(
        "-d", "--day", default=f"{datetime.date.today():%A}",
        help="which day to wish you happiness for"
    )
    parser.add_argument(
        "-g", "--greetings", type=pathlib.Path,
        help="text file of additional greetings"
    )
    return parser.parse_args()


def get_random_greeting(config):
    """Get a uniformly random greeting from a text config file."""
    greetings = [EMPTY_GREETING]
    if config:
        with config.open("r") as f:
            greetings.extend(line.strip() for line in f)
    return random.choice(greetings)


def main():
    """Wish the user happy days."""
    args = get_args()
    happiness = f"Happy {args.day}!"
    greeting = get_random_greeting(args.greetings)
    if greeting != EMPTY_GREETING:
        happiness = f"{greeting} {happiness}"
    delay_seconds = random.randrange(MAX_DELAY_SECONDS)
    time.sleep(delay_seconds)
    print(happiness)


if __name__ == "__main__":
    main()
