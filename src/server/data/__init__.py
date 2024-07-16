from pyouter.router import Router

def dispatch():
    from server.data.read_data import read_data_txt

    router=Router(
        read_data_txt = read_data_txt
    )
    return router