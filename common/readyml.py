import yaml
import os


def read_yml_data(yml_path):
    '''读取yaml'''
    f = open(yml_path, "r", encoding="utf-8")
    read_f = f.read()   # 读取文件
    # print(read_f)
    d = yaml.safe_load(read_f)
    # print(d)
    f.close()
    return d

if __name__ == '__main__':
    # 获取文件的绝对路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yml_path = os.path.join(os.path.dirname(cur_path),"ke11", "userinfo.yml")
    print(yml_path)  # D:\kecheng202107\userinfo.yml

    r = read_yml_data(yml_path)
    print(r)
