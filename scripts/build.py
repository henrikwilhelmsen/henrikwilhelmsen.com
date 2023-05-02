"""Script to generate a distribution folder for the website"""
from pathlib import Path
from subprocess import check_call
from shutil import copy2, rmtree

PROJECT_DIR = Path(__file__).parent.parent
SOURCE_DIR = PROJECT_DIR / "source"
DIST_DIR = PROJECT_DIR / "dist"
SOURCE_SCSS = SOURCE_DIR.joinpath("scss", "main.scss")
DIST_CSS = DIST_DIR.joinpath("css", "main.css")

# all files needed for the distribution of the website, excluding css
DIST_FILES = [
    "index.html",
    "portfolio.html",
    "resume.html",
    "layered-peaks-haikei.svg",
    "mocap-shoot.jpg",
    "resume-henrik-wilhelmsen.pdf",
]


def sass_compressed() -> None:
    """Run sass to generate a compressed css file in the dist folder"""
    args = [
        "sass",
        SOURCE_SCSS.as_posix(),
        DIST_CSS.as_posix(),
        "--style=compressed",
        "--no-source-map",
    ]
    check_call(args=args)


def copy_to_dist() -> None:
    """Copy all files in the DIST_DIR list to the dist folder"""
    source_files = [x for x in SOURCE_DIR.rglob("*") if x.name in DIST_FILES]

    if DIST_DIR.exists():
        rmtree(DIST_DIR)
        DIST_DIR.mkdir(parents=True)

    for src in source_files:
        dst = Path(src.as_posix().replace("/source/", "/dist/"))

        if not dst.parent.exists():
            dst.parent.mkdir(parents=True)

        copy2(src=src, dst=dst)


def main() -> None:
    """Main function"""
    copy_to_dist()
    sass_compressed()


if __name__ == "__main__":
    main()
