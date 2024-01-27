from PIL import Image, ImageDraw, ImageFont


def text_processing(text: str, number_of_words_in_line=20):
    """
    文本处理
    :param text:
    :param number_of_words_in_line:
    :return: new_text
    """
    str_list = text.split('\n')

    new_str = ''
    for a_str in str_list:
        while len(a_str) > number_of_words_in_line:
            if len(a_str) > number_of_words_in_line:
                new_str = new_str + a_str[:number_of_words_in_line] + "\n"
                a_str = a_str[number_of_words_in_line:]
        new_str = new_str + a_str + "\n"
    return new_str


def image_height_calculation(text: str, size):
    """
    计算图像高度
    :param text:
    :param size:
    :return:
    """
    line_num = text.count('\n')
    altitude = (line_num - 1) * (size + 4) + size * 3
    return altitude


def picture_generation(text: str, address='./img/0001.png', size=16, number_of_words_in_line=20):
    # create an image
    new_text = text_processing(text, number_of_words_in_line)

    # get a font
    fnt = ImageFont.truetype("keai.ttf", size)

    max_long = 0
    for a_str in new_text.split('\n'):
        if max_long < fnt.getlength(a_str):
            max_long = fnt.getlength(a_str)

    out = Image.new("RGB", (int(max_long) + 30, image_height_calculation(new_text, size)), '#66ccff')
    # get a drawing context
    d = ImageDraw.Draw(out)
    # draw multiline text
    d.multiline_text((15, 16), new_text, font=fnt, fill=(0, 0, 0))

    out.save(address)


