import argparse
import os
import argparse
import re
import requests
import json
from PIL import Image, ImageFile


def smms_upload(img):
    # 判断图片是否大于5M
    compress_image(img)
    with open(img, 'rb') as img_file:
        try:
            smms_url = 'https://sm.ms/api/v2/upload'
            response = requests.post(
                smms_url,
                files={'smfile': img_file, 'format': 'json'},
                headers={'Authorization': smms_token}
            )
            print("upload finish")
            img_new_url = json.loads(response.text)
            cloud_path = img_new_url['data']['url']
            return cloud_path
        except BaseException as err:
            print(f"error in upload to smms:{err}")

def compress_image(outfile, mb=5*1024, quality=85):
     """不改变图片尺寸压缩到指定大小
     :param outfile: 压缩文件保存地址
     :param mb: 压缩目标，KB
     :param quality: 初始压缩比率
     :return: 压缩文件地址，压缩文件大小
     """

     o_size = os.path.getsize(outfile) // 1024
     if o_size <= mb:
         return outfile

     ImageFile.LOAD_TRUNCATED_IMAGES = True
     while o_size > mb:
         im = Image.open(outfile)
         try:
             im.save(outfile, quality=quality)
         except Exception as e:
             print(e)
             break
         o_size = os.path.getsize(outfile) // 1024
     return outfile


def convert2url(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    outs = []
    for line in lines:
        if re.search('\!\[.*\)', line) is not None:
            images_offline = re.findall('\!\[.*\)', line)  # 找到每段中所有的图片本地链接
            for item in images_offline:
                # 对每个链接进行替换
                img_path = re.search('(?<=\()(.+?)(?=\))', item).group()
                # 判断图片路径是否为网络路径
                if re.search('[a-zA-z]+://[^\s]*', img_path) is None:
                    img_file = os.path.join(path_md, img_path)
                    images_online = smms_upload(img_file)
                    if images_online is not None:
                        line = line.replace(img_path, images_online)
                        outs.append(line)
        else:
            outs.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(outs)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", help="the path of your post file")
    ap.add_argument("-t", "--token", help="the token of your smms count")

    args = ap.parse_args()
    path_md = args.path
    smms_token = args.token

    md_list = os.listdir(path_md)
    md_list = [item for item in md_list if item.endswith('md')]
    for item in md_list:
        file_path = os.path.join(path_md, item)
        convert2url(file_path)
