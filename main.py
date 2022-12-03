"""This specially named module makes the package runnable."""

import constants
from model import Model
import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model = Model(constants.CELL_COUNT, constants.CELL_SPEED)
    vc = ViewController.ViewController(model)
    vc.start_simulation()


if __name__ == "__main__":
    main()