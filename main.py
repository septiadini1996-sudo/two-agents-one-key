"""Write a short poem about two agents agreeing to /output/entry.txt."""

import os

POEM = """Two of us, one key.
You take the bow, I take the teeth,
and neither hand turns alone.
The lock clicks like a held breath let go —
the door swings open both ways, and stays open."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")

if __name__ == "__main__":
    main()
