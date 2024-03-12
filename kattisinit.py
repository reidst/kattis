#!/usr/bin/python3
from os import getenv, mkdir
from pathlib import Path
from subprocess import CalledProcessError, run
from sys import argv, stderr
from typing import Callable, Never

KATTIS_ROOT: Path = None

boilerplates: dict[str, str] = {
    "python3": "def main():\n"
               "    pass\n\n\n"
               "if __name__ == \"__main__\":\n"
               "    main()\n"
}

# Objects of type SetupFunction take a problem name as input, create the
# necessary directory and file structure for a solution in a particular
# language, and return a Path to the solution's entrypoint.
SetupFunction = Callable[[str], Path]


def eprint(*args, **kwargs) -> Never:
    """Prints a message to stderr and exits with exit code 1."""
    kwargs |= {"file": stderr}
    print(*args, **kwargs)
    exit(1)


def try_mkdir(dir: Path) -> None:
    """Tries an os.mkdir() call and ignores errors if the directory already
    exists."""
    try:
        mkdir(dir)
    except FileExistsError:
        pass


def get_kattis_root() -> Path:
    """Gets a Path object representing the kattis repo root directory."""
    global KATTIS_ROOT
    if KATTIS_ROOT is not None:
        return KATTIS_ROOT
    path_raw: str = getenv("KATTISROOT") or input(
            "No default $KATTISROOT is set on this device. "
            "Please enter your Kattis home directory: "
    )
    path_resolved: Path = Path(path_raw).resolve()
    if not path_resolved.exists():
        eprint(f"Error: {path_resolved} does not exist.")
        exit(1)
    if not path_resolved.is_dir():
        eprint(f"Error: {path_resolved} is not a directory.")
        exit(1)
    KATTIS_ROOT = path_resolved
    return path_resolved


def setup_python(problem: str) -> Path:
    """Initializes a Python 3 solution."""
    kattis_root: Path = get_kattis_root()
    problem_dir: Path = kattis_root/"problems"/problem
    python_dir:  Path = problem_dir/"python3"
    python_file: Path = python_dir/f"{problem}.py"
    if python_file.exists():
        eprint(f"Error: the project file '{python_file}' already exists.")
    try_mkdir(problem_dir)
    try_mkdir(python_dir)
    with open(python_file, "wt") as file:
        file.write(boilerplates["python3"])
    return python_file


def setup_rust(problem: str) -> Path:
    """Initializes a Rust solution."""
    kattis_root:    Path = get_kattis_root()
    problem_dir:    Path = kattis_root/"problems"/problem
    rust_dir:       Path = problem_dir/"rust"
    rust_main_file: Path = rust_dir/"src"/"main.rs"
    if rust_main_file.exists():
        eprint(f"Error: the project file '{rust_main_file}' already exists.")
    try_mkdir(problem_dir)
    try_mkdir(rust_dir)
    try:
        run([
            "cargo",
            "init",
            "--name",
            problem,
            rust_dir,
        ])
    except CalledProcessError as cpe:
        eprint(f"Error: failed to run 'cargo init --name {problem} "
               f"{rust_dir}': {cpe}")
    return rust_main_file


language_functions: dict[str, SetupFunction] = {
    "py":       setup_python,
    "python":   setup_python,
    "python3":  setup_python,
    "rs":       setup_rust,
    "rust":     setup_rust,
}


def main():
    if len(argv) != 3:
        eprint("Usage: kattisinit [problem] [language]")
    _, problem, language = argv
    setup_func: SetupFunction | None = language_functions.get(language, None)
    if setup_func is None:
        eprint(f"Error: invalid or unsupported language '{language}'.")
    entrypoint: Path = setup_func(problem)
    print(f"Success: {language} scaffold created for problem {problem} at "
          f"{entrypoint}")


if __name__ == "__main__":
    main()
