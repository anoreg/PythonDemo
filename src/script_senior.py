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

print("---------------------------------multi thread start")
'''
线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。
每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。
指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存。
    线程可以被抢占（中断）。
    在其他线程正在运行时，线程可以暂时搁置（也称为睡眠） -- 这就是线程的退让。

线程可以分为:
    内核线程：由操作系统内核创建和撤销。
    用户线程：不需要内核支持而在用户程序中实现的线程。

Python3 线程中常用的两个模块为：
    _thread
    threading(推荐使用)
thread 模块已被废弃。用户可以使用 threading 模块代替。所以，在 Python3 中不能再使用"thread" 模块。为了兼容性，Python3 将 thread 重命名为 "_thread"。
'''
# 使用线程有两种方式：1. 函数; 2. 用类来包装线程对象。

# _thread.start_new_thread ( function, args[, kwargs] ), 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的
'''
function - 线程函数。
args - 传递给线程函数的参数,他必须是个tuple类型。
kwargs - 可选参数
'''
import time
import _thread

thread_count = 2

def print_time(threadName, delay):
    count = 0
    global thread_count
    while count < 3:
        time.sleep(delay) # seconds
        count += 1
        print ("%s: %s, count:%d" % ( threadName, time.ctime(time.time()), count))
    thread_count -= 1
    print("child thread count:" + str(thread_count))

try:
    _thread.start_new_thread(print_time, ("Thread-1", 1,))
    _thread.start_new_thread(print_time, ("Thread-2", 2,))
    while thread_count > 0:
        pass
except:
    print ("Error: 无法启动线程")

# threading, threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法
'''
threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
'''
# Thread class
'''
run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
'''
import threading

exitFlag = 0

class ChildThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("开始线程：" + self.name)
        print_mythread_time(self.name, self.delay, 3)
        print ("退出线程：" + self.name)

def print_mythread_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

thread1 = ChildThread(1, "Thread-1", 1)
thread2 = ChildThread(2, "Thread-2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")

# thread synchronize
class ThreadLock (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_thread_sync_time(self.name, self.delay, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_thread_sync_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = ThreadLock(1, "Thread-1", 1)
thread2 = ThreadLock(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")

# Queue
'''
Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步, 常用方法:
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''
import queue

exitFlag = 0

class ThreadQueue (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = ThreadQueue(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")


print("---------------------------------multi thread end")

print("----------------------------------net start")


print("----------------------------------net end")
