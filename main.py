from pathlib import Path


def main() -> None:
    """Write the winning one-word internet description to /output/entry.txt."""
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        "Unsubscribe",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
