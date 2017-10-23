import re
pattern = re.compile(ur'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}')
str = u''
print(pattern.search(str))
line = "我的电子邮件tom@gmail.com。 ";
re.findall(r'\d+',line)
print(s.search(str))

import re
pattern = re.compile(ur'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}')
str = u''
print(pattern.search(str))
line = "将什么发送到jerry123@163.com或者3123432@qq.com. ";
matchObj = re.match( r'(.*) huozhe (.*?) .*', line,“ ^w+[-+.]w+)*@w+([-.]w+)*.w+([-.]w+)*$” 
)
re.findall(r'\d+',line)
print(a.search(str))

import re
pattern = re.compile(ur'0?(13|14|15|18|17)[0-9]{9}')
str = u''
print(pattern.search(str))
line = "若遇特殊情况打电话给182123445678. ";
re.findall(r'\d+',line)
print(w.search(str))
matchObj = re.match( r'(.*) (.*?) .*', line,“ ^w+[-+.]w+)*@w+([-.]w+)*.w+([-.]w+)*$” 
)

