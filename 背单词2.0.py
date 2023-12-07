import random
import time
import random
import tkinter as tk
from tkinter import filedialog
words = {}
wrong = {}

print("请选择单词库文件")
#调用文件管理器直接选择文件
def getfile():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename()
    print(filepath)
    return filepath

path = getfile()

#读取文本文件并生成单词字典
with open(path,encoding = 'utf-8') as f:    #编码改为utf-8，如有文件格式问题无法读取首先看编码
    for line in f:                                #遍历循环文件每一行
        line = line.split()
        words[line[0]] = line[1]

# 定义背单词函数
def memorize_words():
    jp_list = list(words.keys())  # 将日文转换为列表
    random.shuffle(jp_list)  # 将单词列表随机排序
    error = 0

    def overlook1():
        global wrong
        wrong_list = list(wrong.keys())
        random.shuffle(wrong_list)
        if error > 0 :
            if input("要复习吗？(Y/N)") == "Y":
                for word in wrong_list:
                    answer = input("「{}」は中国語でどういう意味? ".format(word))
                    if answer == wrong[word]:
                        print("正しい!")
                    elif answer in wrong[word]:
                        print("答对一部分，正解为「{}」".format(wrong[word]))
                    else:
                        print("違う！正解は 「{}」だ.".format(wrong[word]))
                print("恭喜！已完成复习！")
                time.sleep(5)
        else:
            print("没有错误，再接再励！")
            time.sleep(5)
    
    def overlook2():
        global wrong
        wrong_list = list(wrong.keys())
        random.shuffle(wrong_list)
        if error > 0 :
            if input("要复习吗？(Y/N)") == "Y":
                for word in wrong_list:
                    answer = input("「{}」は日本語でどういう意味? ".format(wrong[word]))
                    if answer == word:
                        print("正しい!")
                    else:
                        print("違う！正解は 「{}」だ.".format(word))
                print("恭喜！已完成复习！")
                time.sleep(5)
        else:
            print("没有错误，再接再励")
            time.sleep(5)

    q = input("请选择提示为汉语或日语（C/J)：")
    if q == "J" :
        for word in jp_list:
            answer = input("「{}」は中国語でどういう意味? ".format(word))
            if answer == words[word]:
                print("正しい!")
            elif answer in words[word]:
                print("答对一部分，正解为「{}」".format(words[word]))
            else:
                print("違う！正解は 「{}」だ.".format(words[word]))
                error += 1
                wrong[word] = words[word]
        print("已结束，共计错误{}题".format(error))
        overlook1()
    elif q == "C":
        for word in jp_list:
            answer = input("「{}」は日本語でどういう意味? ".format(words[word]))
            if answer == word:
                print("正しい!")
            else:
                print("違う！正解は 「{}」だ.".format(word))
                error = error + 1
                wrong[word] = words[word]
        print("已结束，共计错误{}题".format(error))
        overlook2()
    else:
        print("输入错误！请正确输入，并区分大小写！")
        time.sleep(5)

# 运行背单词函数
memorize_words()