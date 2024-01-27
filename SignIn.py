import time
import json
import random


def add_user(QQID, old_dict, name):
    """
    添加新成员信息
    :param name:
    :param QQID:
    :param old_dict:
    :return:
    """
    old_dict[QQID] = {
        "name": name,
        "Last_check_time": "2022-01-01",
        "Gold": 0,
        "Likability": 0,
        "Fortune": {
            "time": "2022-01-01",
            "PeachBlossomLuck": 0,
            "CareerLuck": 0,
            "FinancesLuck": 0,
            "LuckGrade": "",
            "Comments": ""
        },
        "Knapsack": {

        }
    }
    fb = open('personal_information.json', 'w', encoding='utf-8')
    json.dump(old_dict, fb, indent=4)
    fb.close()


def check_sign_in(QQID, name):
    """
    判断今天是否签到
    :param name:
    :param QQID:
    :return:
    """
    fb = open('personal_information.json', 'r', encoding='utf-8')
    personal_information_dict = json.load(fb)
    fb.close()

    if QQID in personal_information_dict:
        if personal_information_dict[QQID]['Last_check_time'] == time.strftime('%Y-%m-%d', time.localtime()):
            return True
        else:
            return False
    else:
        add_user(QQID, personal_information_dict, name)
        return False


def determine_level_favorability(likability):
    """
    判断好感度等级
    :param likability:
    :return:
    """
    if 100 > likability > 0:
        return "陌生Lv1"
    elif 200 > likability > 100:
        return "熟悉Lv2"
    elif 300 > likability > 200:
        return "朋友Lv3"
    elif 400 > likability > 300:
        return "好友Lv4"
    elif 500 > likability > 400:
        return "挚友Lv5"
    elif 600 > likability > 500:
        return "恋人Lv6"
    elif likability > 600:
        return "夫妻Lv7"


# 签到
def sign_in(QQID, name):
    """
    签到
    :param QQID:id
    :param name:名称
    :return:str
    """
    if check_sign_in(QQID, name):
        return f"今天已经签到过了"
    else:
        fb = open('personal_information.json', 'r', encoding='utf-8')
        personal_information_dict = json.load(fb)
        fb.close()

        personal_information_dict[QQID]['Last_check_time'] = time.strftime('%Y-%m-%d', time.localtime())

        add_gold = random.randrange(0, 100)
        add_likability = round(random.random() * 10, 2)

        personal_information_dict[QQID]['Gold'] += add_gold
        personal_information_dict[QQID]['Likability'] += add_likability
        personal_information_dict[QQID]['name'] = name

        fb = open('personal_information.json', 'w', encoding='utf-8')
        json.dump(personal_information_dict, fb, indent=4)
        fb.close()

        return (f"签到成功\n"
                f"金币+{add_gold}\n"
                f"好感度+{add_likability}\n"
                "好感度等级:" + determine_level_favorability(personal_information_dict[QQID]['Likability']))


def favorability_inquiry(QQID):
    """
    好感度查询
    :param QQID:
    :return:
    """
    open_personal_r = open('personal_information.json', 'r', encoding='utf-8')
    personal_list = json.load(open_personal_r)
    open_personal_r.close()

    return (f"<@!{QQID}> \n"
            f"好感度：{personal_list[QQID]['Likability']}\n"
            f"好感度等级：{determine_level_favorability(personal_list[QQID]['Likability'])}")
