from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("http://www.zhihu.com/robots.txt")
rp.read()
print(rp)
rst = rp.can_fetch("Baiduspider", "https://zhuanlan.zhihu.com/p/61215293")
print(rst)