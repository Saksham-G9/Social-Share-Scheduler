import os
import pathlib
import sys

NOTEBOOKS_DIR = pathlib.Path(__file__).parent
REPO_DIR = NOTEBOOKS_DIR.parent
DJANGO_PROJECT_ROOT = REPO_DIR / "social_share_schedular"
DJANGO_SETTINGS_MODULE = "social_share_schedular.settings"


def init(verbose=False):
    os.chdir(REPO_DIR)
    sys.path.insert(0, str(REPO_DIR))
    if verbose:
        print(f"Changed working directory to: {REPO_DIR}")
        print(f"Added to Python path: {REPO_DIR}")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ.setdefault("INNGEST_DEV", "1")
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    # os.environ.setdefault(
    #     "DATABASE_URL",
    #     "postgres://postgres:postgres@localhost:5432/postgres",
    # )
    import django

    django.setup()