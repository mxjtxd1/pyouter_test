def read_data_txt(config,options):
    data_path = './data/data.txt'
    with open(data_path) as f:
        for line in f:
            print(line + ' ')