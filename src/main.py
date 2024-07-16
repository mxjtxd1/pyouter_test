from pyouter.app import App
from pyouter.router import Router

from options import get_args_parser
from config.config import load_config

def main_dispatch():
    """ 主路由

    """
    from test import dispatch as test_dispatch
    from server import dispatch as server_dispatch

    router = Router(
        init = lambda config,options: print('server_ip:{}'.format(config['server_ip'])),
        test = test_dispatch(),
        server = server_dispatch()
    )

    return router


def run():
    """ 入口函数
    
    """

    # 获取命令行参数
    args_parser = get_args_parser()
    options = args_parser.parse_args()
    # 加载配置文件
    config = load_config(options)

    app = App(
        config=config,
        parser=args_parser
    )

    app.use(
        router=Router(
            pyouter_test = main_dispatch()
        )
    )

    app.run()


if __name__=="__main__":
    run()