"""
调用和风天气API
下面的 xxx 改成自己的 key
"""

import requests


def city_id(city_name):
    """
    获取城市id
    :param city_name:
    :return:
    """
    # 设置API的URL和参数
    url = f"https://geoapi.qweather.com/v2/city/lookup?key=xxx&location={city_name}"

    # 发送GET请求v2
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析响应内容（假设是JSON格式）
        data = response.json()
        new_id = data['location'][0]['id']
        return new_id
    else:
        print("请求失败，状态码：", response.status_code)


def weather(city_name):
    city_id1 = city_id(city_name)
    # 实时天气
    # 设置API的URL和参数
    url = f"https://devapi.qweather.com/v7/weather/now?key=xxx&location={city_id1}"

    # 发送GET请求
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析响应内容（假设是JSON格式）
        data = response.json()
        real_time_time = data['now']['obsTime']  # 数据观测时间
        real_time_temp = data['now']['temp']  # 温度，默认单位：摄氏度
        real_time_text = data['now']['text']  # 天气状况的文字描述，包括阴晴雨雪等天气状态的描述
        real_time_windDir = data['now']['windDir']  # 风向
        real_time_windSpeed = data['now']['windSpeed']  # 风速，公里/小时
    else:
        return "请求失败..."

    txt = (f"实时天气    城市:{city_name}\n"
           f"数据时间：{real_time_time}\n"
           f"天气：{real_time_text}       温度：{real_time_temp}℃\n"
           f"风向：{real_time_windDir}    风速：{real_time_windSpeed} km/h\n")

    txt = txt + f'\n天气预报    城市:{city_name}\n'
    # 天气预报
    # 设置API的URL和参数
    url1 = f"https://devapi.qweather.com/v7/weather/3d?key=xxx&location={city_id1}"

    # 发送GET请求
    response1 = requests.get(url1)

    # 检查响应状态码
    if response1.status_code == 200:
        # 解析响应内容（假设是JSON格式）
        data1 = response1.json()

        for i in range(0, 3):
            today_fxDate = data1['daily'][i]['fxDate']  # 预报日期
            today_sunrise = data1['daily'][i]['sunrise']  # 日出时间，在高纬度地区可能为空
            today_sunset = data1['daily'][i]['sunset']  # 日落时间，在高纬度地区可能为空
            today_tempMax = data1['daily'][i]['tempMax']  # 预报当天最高温度
            today_tempMin = data1['daily'][i]['tempMin']  # 预报当天最低温度
            today_textDay = data1['daily'][i]['textDay']  # 预报白天天气状况文字描述，包括阴晴雨雪等天气状态的描述
            today_textNight = data1['daily'][i]['textNight']  # 预报晚间天气状况文字描述，包括阴晴雨雪等天气状态的描述

            txt = txt + (f"日期:{today_fxDate}\n"
                         f"日出时间:{today_sunrise}    日落时间:{today_sunset}\n"
                         f"最高温度:{today_tempMax}℃     最低温度:{today_tempMin}℃\n"
                         f"白天天气:{today_textDay}       夜晚天气:{today_textNight}\n")
    else:
        return "请求失败..."

    return txt


