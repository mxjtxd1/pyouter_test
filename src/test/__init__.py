from pyouter.router import Router

def dispatch():
    from test.test_hello import test_helloworld

    router=Router(
        test_hello = test_helloworld
    )
    return router