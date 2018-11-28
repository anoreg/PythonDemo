'''
Created on Nov 16, 2018

@author: feiyi
'''
#---------------------------------RegEx(Regular Expression, 正则)
print("-------------------------------RegEx start")
'''
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。
'''
import re
# re.match(pattern, string, flag = 0), 尝试从字符串的起始位置匹配一个模式，若字符串开始不符合正则表达式，则匹配失败，函数返回None
'''
pattern    匹配的正则表达式
string    要匹配的字符串。
flags    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。多个标志使用OR(|)来指定
'''
# RegEx flag:
'''
re.I    使匹配对大小写不敏感
re.L    做本地化识别（locale-aware）匹配
re.M    多行匹配，影响 ^ 和 $
re.S    使 . 匹配包括换行在内的所有字符
re.U    根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''
# RegEx pattern:
'''
标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
反斜杠本身需要使用反斜杠转义。
由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符
^    匹配字符串的开头
$    匹配字符串的末尾。
.    匹配任意字符，除了换行符(\n, \r)，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]    用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]    不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*    匹配0个或多个的表达式。
re+    匹配1个或多个的表达式。
re?    匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}    匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
re{ n,}    精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
re{ n, m}    匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b    匹配a或b
(re)    匹配括号内的表达式，也表示一个组
(?imx)    正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)    正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)    类似 (...), 但是不表示一个组
(?imx: re)    在括号中使用i, m, 或 x 可选标志
(?-imx: re)    在括号中不使用i, m, 或 x 可选标志
(?#...)    注释.
(?= re)    前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)    前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
(?> re)    匹配的独立模式，省去回溯。
\w    匹配数字字母下划线
\W    匹配非数字字母下划线
\s    匹配任意空白字符，等价于 [\t\n\r\f]。
\S    匹配任意非空字符
\d    匹配任意数字，等价于 [0-9]。
\D    匹配任意非数字
\A    匹配字符串开始
\Z    匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z    匹配字符串结束
\G    匹配最后匹配完成的位置。
\b    匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B    匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等。    匹配一个换行符。匹配一个制表符, 等
\1...\9    匹配第n个分组的内容。
\10    匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
'''
print(re.match('www', 'www.runoob.com'))  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

# common patterns
pattern_phone_cn = "^1(3[0-9]|4[579]|5[^4]|6[6]|7[0135678]|8[0-9]|9[89])\\d{8}$" # 中国大陆手机号
pattern_int_positive = "^[0-9]*$" # 正整数
pattern_name = "^[a-zA-Z\u4e00-\u9fa5][a-zA-Z\u4e00-\u9fa50-9_]{1,15}$" # 由汉字、字母、数字、_、的组合，以字母或者汉字为开头, 最长16位 

matchObj = re.match(pattern_phone_cn, "18668194450")
print(matchObj, True if matchObj else False)

matchObj = re.match(pattern_int_positive, "11s")
print(matchObj, True if matchObj else False)

matchObj = re.match(pattern_name, "Fahy111111111111")
print(matchObj, True if matchObj else False)

# group(), 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
# groups(), 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# if matchObj:
#     print ("matchObj.group() : ", matchObj.group())
#     print ("matchObj.group(1) : ", matchObj.group(1))
#     print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print ("No match!!")

matchObj = re.match("(.*) (.*) (.*) (.*) (.*)", line, re.I)
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
    print ("matchObj.group(3) : ", matchObj.group(3))
    print ("matchObj.group(4) : ", matchObj.group(4))
    print ("matchObj.group(5) : ", matchObj.group(5))
    print("matchObj.groups() : ", matchObj.groups())
else:
    print ("No match!!")

# re.search(pattern, string, flag=0), 扫描整个字符串并返回第一个成功的匹配, 否则返回None
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

# re.sub(pattern, repl, string, count=0), 用于替换字符串中的匹配项
'''
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
 # 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
# repl 参数是一个函数
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# re.compile(pattern[, flags]), 用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
regStr = "one12twothree34four"
pt = re.compile(r"\d+") # 匹配至少一个数字
mt = pt.match(regStr)
print(mt)

mt = pt.match(regStr, 3, 10) # 从'1'的位置开始匹配
print(mt)
print(mt.group(0))   # 可省略 0
print(mt.start(0))   # 可省略 0
print(mt.end(0))     # 可省略 0
print(mt.span(0))    # 可省略 0

# findall(string[, pos[, endpos]]), 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
'''
string 待匹配的字符串。
pos 可选参数，指定字符串的起始位置，默认为 0。
endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
'''
result1 = pt.findall('runoob 123 google 456')
result2 = pt.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)

print("--------------------------------RegEx end")

print("----------------------------------cmd start")
import subprocess

subprocess.call(["ls", "-l"])
completeProcess = subprocess.run("ls -a", shell = True) # doesn't capture output
print(completeProcess) # returnCode = 0 meanings run successfully

completeProcess = subprocess.run(["ls","-A"] , stdout=subprocess.PIPE)
print(completeProcess.stdout.decode())

print("----------------------------------cmd end")

print("----------------------------------net start")
# 最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = "https://www.baidu.com"
# get request
resp = urlopen(url)
result = resp.read().decode("utf-8")
print(result)

# post request
url = "http://sdk.pay.coco4game.com/app_pay/Action_OrderId.aspx"
params={"gameid":"1364020563"}
data = urlencode(params).encode("utf-8") # 将数据转为byte类型
req = Request(url, data) # 将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req) as resp:
    result = resp.read().decode("utf-8")
print(result)

# socket
# socket.socket([family[, type[, proto]]])
'''
family: 套接字家族可以使AF_UNIX或者AF_INET
type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
protocol: 一般不填默认为0.
'''
'''
服务器端套接字
s.bind()    绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
s.listen()    开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
s.accept()    被动接受TCP客户端连接,(阻塞式)等待连接的到来
客户端套接字
s.connect()    主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
s.connect_ex()    connect()函数的扩展版本,出错时返回出错码,而不是抛出异常
公共用途的套接字函数
s.recv()    接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
s.send()    发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
s.sendall()    完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
s.recvfrom()    接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
s.sendto()    发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
s.close()    关闭套接字
s.getpeername()    返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
s.getsockname()    返回套接字自己的地址。通常是一个元组(ipaddr,port)
s.setsockopt(level,optname,value)    设置给定套接字选项的值。
s.getsockopt(level,optname[.buflen])    返回套接字选项的值。
s.settimeout(timeout)    设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
s.gettimeout()    返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
s.fileno()    返回套接字的文件描述符。
s.setblocking(flag)    如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
s.makefile()    创建一个与该套接字相关连的文件
'''

print("----------------------------------net end")

print("----------------------------------json start")
# json.dumps(): 对数据进行编码
# json.loads(): 对数据进行解码
import json
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

# Python 字典类型转换为 JSON 对象
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])


print("----------------------------------json end")
