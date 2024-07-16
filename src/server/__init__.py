from pyouter.router import Router

def dispatch():
    from server.data import dispatch as data_dispatch

    router=Router(
        data = data_dispatch()
    )
    return router