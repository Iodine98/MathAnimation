from subprocess import call
from pathlib import Path


def run_file(filename: str) -> None:
    call(["manim", "-pqh", Path(Path(__file__).parent.absolute(), filename)])


def run() -> None:
    files = [
        "intro.py",
        "operations.py",
        "p_union.py",
        "p_intersection.py"
    ]
    for file in files:
        run_file(file)


if __name__ == '__main__':
    run()
