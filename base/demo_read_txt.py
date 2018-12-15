with open("../data/login1.txt", "r", encoding="utf-8") as f:
    data_login = f.readlines()
    data_list=list()
    print(data_login)
    for data in data_login:
        # print(data)
        data_list.append(tuple(data.strip().split(",")))
    print(data_list)

