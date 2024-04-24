if __name__ == '__main__':

    pcs = []
    ips = []

    for i in range(100):
        pcs.append('P' + str(i + 1))
        ips.append('172.30.2.' + str(i + 1))

    with open(f'pc.csv', 'w') as file:
        file.write('pc_name, ip\n')
        for i in range(100):
            file.write(pcs[i] + ', ' + ips[i] + '\n')
    

