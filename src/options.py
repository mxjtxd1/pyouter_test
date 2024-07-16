from argparse import ArgumentParser
from pyouter.default import create_parser


def add_custom_arguments(parser: ArgumentParser):
    ''' 用户定制化参数选项
    
    * --cluster: 开发环境还是线上环境
    '''
    parser.add_argument(
        "--cluster",
        dest="cluster",
        help="cluster dev or pro",
        default="dev",
        nargs='?',
        type=str,
        metavar="CLUSTER"
    )



def get_args_parser():
    parser = create_parser("pyouter test")
    add_custom_arguments(parser)

    return parser


def show_help():
    """
    命令行选项说明:
    ==
    """

    help = '\n'.join([
        show_help.__doc__,
        add_custom_arguments.__doc__
    ])

    print(help)