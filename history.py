import sqlite3
from urllib.parse import urlparse
import matplotlib.pyplot as plt

# 用于存储 网址-频次 关系的字典
dict_website = {}

# 程序入口
if __name__ == "__main__":
    # 连接数据库，路径要根据自己的情况做修改
    conn = sqlite3.connect(r'C:\Users\YuZhangWang\AppData\Local\Google\Chrome\User Data\Default\History')

    # 得到urls表中的所有记录
    cursor = conn.execute('select url from urls')

    # 填充词典
    for row in cursor:
        # 解析url得到的网址
        website = urlparse(row[0]).netloc

        # 更新网址的频次
        count = dict_website.setdefault(website, 0)
        dict_website[website] = count + 1

    # 按频次排序
    lst_his = sorted(dict_website.items(), key=lambda x: x[1], reverse=True)

    # 绘制饼图(前20个常用网址)
    plt.pie(x=[e[1] for e in lst_his[:20]], \
            labels=[e[0] for e in lst_his[:20]], \
            autopct='%1.2f%%')
    plt.show()
