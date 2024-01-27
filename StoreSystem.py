import json


def list_shop_items():
    """
    读取商品列表
    :return:
    """
    fb = open('shop_list.json', 'r', encoding='utf-8')
    shop_list = json.load(fb)
    fb.close()
    str_list = "    琪露诺小店   \n"

    key_list = list(shop_list.keys())
    for key in key_list:
        str_list = str_list + f"{key}.{shop_list[key]['name']}       {shop_list[key]['price']}\n"
    return str_list


def add_shop_item():
    """
    添加商品
    :return:
    """
    fb = open('shop_list.json', 'r', encoding='utf-8')
    shop_list = json.load(fb)
    fb.close()
    shop_list['3'] = {
        "name": "琪露诺的智商",
        "price": 999,
        "introduce": "功能待开发。。。"
    }
    fp = open('shop_list.json', 'w', encoding='utf-8')
    json.dump(shop_list, fp, indent=4)
    fp.close()


def purchase_of_goods(QQID, product_id, num=1):
    """
    购买商品
    :param QQID:
    :param product_id:
    :param num:
    :return:
    """
    open_shop_r = open('shop_list.json', 'r', encoding='utf-8')
    open_personal_r = open('personal_information.json', 'r', encoding='utf-8')
    shop_list = json.load(open_shop_r)
    personal_list = json.load(open_personal_r)
    open_shop_r.close()
    open_personal_r.close()

    if product_id in shop_list:
        if personal_list[QQID]['Gold'] > shop_list[product_id]['price'] * int(num):
            if shop_list[product_id]['name'] in personal_list[QQID]['Knapsack']:
                personal_list[QQID]['Knapsack'][shop_list[product_id]['name']] = personal_list[QQID]['Knapsack'][
                                                                                     shop_list[product_id][
                                                                                         'name']] + int(num)
                personal_list[QQID]['Gold'] -= shop_list[product_id]['price'] * int(num)
            else:
                personal_list[QQID]['Knapsack'][shop_list[product_id]['name']] = 0
                personal_list[QQID]['Knapsack'][shop_list[product_id]['name']] = personal_list[QQID]['Knapsack'][
                                                                                     shop_list[product_id][
                                                                                         'name']] + int(num)
                personal_list[QQID]['Gold'] -= shop_list[product_id]['price'] * int(num)
            open_personal_w = open('personal_information.json', 'w', encoding='utf-8')
            json.dump(personal_list, open_personal_w, indent=4)
            return (f"<@!{QQID}> \n"
                    f"购买成功\n"
                    f"{shop_list[product_id]['name']}   +{num}")
        else:
            return (f"<@!{QQID}> \n"
                    f"没钱还想买东西！！！")


def gold_coin_query(QQID):
    """
    金币查询
    :param QQID:
    :return:
    """
    oopen_personal_r = open('personal_information.json', 'r', encoding='utf-8')
    personal_list = json.load(oopen_personal_r)
    oopen_personal_r.close()
    return (f"<@!{QQID}> \n"
            f"你的金币余额：{personal_list[QQID]['Gold']}")


def backpack_inquiry(QQID):
    """
    背包查询
    :param QQID:
    :return:
    """
    oopen_personal_r = open('personal_information.json', 'r', encoding='utf-8')
    personal_list = json.load(oopen_personal_r)
    oopen_personal_r.close()
    str1 = ''
    for key in personal_list[QQID]['Knapsack']:
        str1 = str1 + key + '       ×' + str(personal_list[QQID]['Knapsack'][key]) + '\n'
    return (f"{personal_list[QQID]['name']}的背包\n"
            f"{str1}")

