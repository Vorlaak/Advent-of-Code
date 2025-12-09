def get_input() :
    #return("example.txt")
    return("input.txt")

def get_networks(text) :
    with open(text) as file :
        data = file.read().split('\n')
    dict = {}
    for line in data :
        pc_1 = line[0] + line[1]
        pc_2 = line[-2] + line[-1]
        if pc_1 not in dict :
            dict[pc_1] = [pc_2]
        elif pc_2 not in dict[pc_1] :
            dict[pc_1].append(pc_2)
        if pc_2 not in dict :
            dict[pc_2] = [pc_1]
        elif pc_1 not in dict[pc_2] :
            dict[pc_2].append(pc_1)
    return dict

def count(dict) :
    counter = 0
    networks = []
    for key, value in dict.items() :
        for pc in value :
            for sec_pc in dict[pc] :
                if sec_pc in value :
                    if ([key, pc, sec_pc] not in networks) and \
                       ([key, sec_pc, pc] not in networks) and \
                       ([pc, key, sec_pc] not in networks) and \
                       ([pc, sec_pc, key] not in networks) and \
                       ([sec_pc, key, pc] not in networks) and \
                       ([sec_pc, pc, key] not in networks) :  
                        networks.append([key, pc, sec_pc])
                    if key[0] == 't' :
                        counter += 1
                    if pc[0] == 't' :
                        counter += 1
                    if sec_pc[0] == 't' :
                        counter +=1
    return networks

def main() :
    textfile = get_input()
    net = get_networks(textfile)
    networks = count(net)
    good_nets = []
    for net in networks :
        for pc in net :
            if (pc[0] == 't') and (net not in good_nets) :
                good_nets.append(net)
    print(len(good_nets))

if __name__=="__main__":
    main()