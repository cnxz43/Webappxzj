# -*- coding: utf-8 -*-


from urllib import parse,request
import json
# from retrying import retry
import requests
import string
from requests.auth import HTTPBasicAuth

# @retry(stop_max_attempt_number=7)
def open_url(req):
    print("trying...")
    res = request.urlopen(req)
    res = res.read()
    return res


def connect_commandplat(ne = "BADGS3" ,command_list = []):
    '''

    :param device:
    :param commandarr: 指令集 type：list
    :return:
    '''

    # url转码
    url = "http://" + "10.216.6.231/WebApi/mml/" + ne + "/" + "集中操作"
    url = parse.quote(url, safe=string.printable)

    # 指令集list 转码
    btcommands = bytes(json.dumps(command_list), encoding="utf-8")

    # 连接指令平台权限转码
    user = "wg_cmcc_luoxiaoyong"
    pwd = "1qaz@WSX"
    b64_auth = HTTPBasicAuth(user, pwd)

    # 头文件
    header_dict = {"Content-Type": "application/json;charset=UTF-8"}


    print("url",url)
    # 向平台发送post请求
    # url：平台地址；
    # data：post携带信息，即指令集合；
    # auth：权限信息；
    # headers：头文件
    r = requests.post(url=url,
                      data=btcommands,
                      auth=b64_auth,
                      headers=header_dict)
    #请求所得信息（解码）
    print ("result:\n",r.content.decode("utf-8"))
        # 请求所得信息（解码）
    return r.content.decode("utf-8")


def organize_result(ret):
    print("---organize_result---")
    ret = ret[1:-1]
    ret = ret.split(',')
    result = ''
    for r in ret:
        print("$$$",r)
        # rs = r.split(' ')
        # line = ''
        # for word in rs:
        #     # print("%%%",word)
        #     word = word.replace('\\r\\n', '\n')
        #     # print(word)
        #     if word != '':
        #         line += word + '\t'
        # print("###",line)
        result += r[1:-1].replace('\\r\\n', '\n').replace('\\x03','　')
        # print("^^^",r[1:-1].replace('\\r\\n', '\n'))
    print("org:", result)
    return result

def gen_image():
    # -*- coding: utf-8 -*-

    import os
    import pygame

    pygame.init()

    text = u"这是一段测试文本，test 123。"
    font = pygame.font.Font(os.path.join("fonts", "simsun.ttc"), 14)
    rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))

    pygame.image.save(rtext, "t.jpg")

if __name__=="__main__":
    # command_list = ["LST POOLBKPCTRL:;","DSP BKPSTATUS:;","DSP N7LNK:;","DSP MGW:;","LST OFI: QR=LOCAL;"]
    # res = connect_commandplat("SJGS10", command_list)

    # res =str(["mml\r\nWO      TSGS11/14B/KD/03/03       AD-40   TIME 181023 1557  PAGE    1\r\n\u0003<","ioexp;\r\nEXCHANGE IDENTITY DATA\r\n\r\nIDENTITY\r\nTSGS11/14B/KD/03/03\r\n\r\nEND\r\n\r\n\r\n\u0003<","allip:acl=a1;\r\nALARM LIST\r\n\r\nA1/APT \"TSGS11/14B/KD/0\" 025 180920   0038      \r\nEVENT REPORTING THRESHOLD REACHED\r\nENUM THRESHOLD LEVEL\r\n145  TH1       3\r\n\r\n\r\nA1/APT \"TSGS11/14B/KD/0\" 120 180920   0042      \r\nBLOCKING SUPERVISION\r\nR        LVB      NDV      BLO\r\nB5M6I        574     1147     1147\r\n\r\n\r\n\r\nA1/APT \"TSGS11/14B/KD/0\" 123 180920   0042      \r\nBLOCKING SUPERVISION\r\nR        LVB      NDV      BLO\r\nB5M6O        574     1147     1147\r\n\r\n\r\n\r\nEND\r\n\r\n\u0003<","saaep:sae=36;\r\nSIZE ALTERATION OF DATA FILES INFORMATION\r\n\r\nSAE    BLOCK    CNTRTYP  NI          NIU         NIE         NIR\r\n  36            THRESH1        7300        3544\r\nEND\r\n\r\n\u0003<","nrgwp:mg=all;\r\nMEDIA GATEWAY DATA\r\n\r\nMG       BCUID       STATUS  MGG      MGS      INFO            MC\r\nTSGM17      3251182  AVAIL   BS41MGG           MPTMTP            0\r\n                             BS13MGG           2-3-251-182\r\n                             BS47MGG\r\n                             BS2MGG\r\n                             BS21MGG\r\n                             TSGM17\r\n                             BICCMGG\r\n\r\nTSGM10      3254102  AVAIL   BS46MGG           MPTMTP            0\r\n                             BS15MGG           2-3-254-102\r\n                             BS23MGG\r\n                             BS4MGG\r\n                             BS22MGG\r\n                             BS1MGG\r\n                             TSGM10\r\n                             BICCMGG\r\n\r\nTSGM5       3254062  AVAIL   BS45MGG           MPTMTP            0\r\n                             BS33MGG           2-3-254-62\r\n                             BS20MGG\r\n                             BS19MGG\r\n                             TSGM5\r\n                             BICCMGG\r\n\r\nTSGM6       3254065  AVAIL   BS41MGG           MPTMTP            0\r\n                             BS13MGG           2-3-254-65\r\n                             BS47MGG\r\n                             BS2MGG\r\n                             BS21MGG\r\n                             TSGM6\r\n                             BICCMGG\r\n\r\nTSGM3       3254038  AVAIL   BS46MGG           MPTMTP            0\r\n                             BS15MGG           2-3-254-38\r\n                             BS23MGG\r\n                             BS4MGG\r\n                             BS22MGG\r\n                             BS1MGG\r\n                             TSGM3\r\n                             BICCMGG\r\n\r\nTSGM12      3254156  AVAIL   BS45MGG           MPTMTP            0\r\n                             BS33MGG           2-3-254-156\r\n                             BS20MGG\r\n                             BS19MGG\r\n                             BICCMGG\r\n                             TSGMG12\r\n\r\nEND\r\n\r\n\u0003<","exit\r\nNOT ACCEPTED\r\nSYNTAX FAULT\r\n\u0003<"]
    # )# print("1111",res)
    #
    # # print(str('\x03', encoding = "utf-8"))
    # print(res.encode('utf-8'))
    # print(str(res.encode('utf-8'),encoding='utf-8'))
    # print(res)
    # organize_result(res)

    gen_image()

