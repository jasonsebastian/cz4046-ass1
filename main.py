import argparse

from models.grid_environment import GridEnvironment


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('iteration',
                        choices=['value', 'policy'],
                        help='type of iteration (value or policy)')
    return parser.parse_args()


def main():
    args = parse_args()
    grid_environment = GridEnvironment()
    grid_environment.print_grid()


if __name__ == '__main__':
    main()
