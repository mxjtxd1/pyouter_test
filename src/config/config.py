def load_config(options):
    if options.cluster == 'dev':
        config = {'server_ip':'127.0.0.1'}
    elif options.cluster == 'pro':
        config = {'server_ip':'192.168.0.1'}

    return config