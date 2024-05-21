import sys

def display_banner():
    with open("s-auth.banner", "r") as f:
        banner = f.read()
    sys.stdout.write("\033[93m" + banner + "\033[0m")
