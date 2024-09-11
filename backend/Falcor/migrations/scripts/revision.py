from alembic import command
from alembic.config import Config

from Falcor.env import Falcor_DIR

alembic_cfg = Config(Falcor_DIR / "alembic.ini")

# Set the script location dynamically
migrations_path = Falcor_DIR / "migrations"
alembic_cfg.set_main_option("script_location", str(migrations_path))


def revision(message: str) -> None:
    command.revision(alembic_cfg, message=message, autogenerate=False)


if __name__ == "__main__":
    input_message = input("Enter the revision message: ")
    revision(input_message)
