# -*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.font as tkfont
import urllib.request
import urllib.parse
import json


def getAns(content):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {'i': content, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb',
            'salt': '16104458370277', 'sign': '8c80ab716ab1d2d59121868c72216170', 'lts': '1610445837027',
            'bv': '02c2dd94fb562b4304f9b0c657990444', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'}
    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    ans = json.loads(html)['translateResult'][0][0]
    finall_ans = ans['tgt']
    return finall_ans



mainframe = tk.Tk()
mainframe.title("翻译")
mainframe.geometry('400x205+755+215')
mainframe.config(bg='white')

ft = tkfont.Font(family='微软雅黑', size=12, weight=tkfont.BOLD)
lb = tk.Label(master=mainframe, text='这里输出文本', font=ft)
lb.place(x=210, y=10, width=180, height=150)
en = tk.Entry(master=mainframe, text='好家伙', font=ft)
en.place(x=10, y=10, width=180, height=150)


def check():
    con = en.get()
    print(con)
    lb.config(text=getAns(con))


tk.Button(master=mainframe, text='查询', width=8, command=check).place(x=170, y=170)
tk.Button(master=mainframe, text='清除内容', width=8, command=en.delete(0, 1000)).place(x=40, y=170)
tk.Button(master=mainframe, text='退出', width=8, command=mainframe.destroy).place(x=290, y=170)

mainframe.mainloop()




