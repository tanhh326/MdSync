from threading import Thread

import pyperclip

from plt import csdn, jianshu, juejin, sifou, zhihu
from common import MdFile, configureChromiumPage

if __name__ == '__main__':
    md_file = MdFile().parse('md/测试标题.md')
    pyperclip.copy(md_file.content)
    configureChromiumPage()
    Thread(target=csdn.publish, args=[md_file]).start()
    Thread(target=jianshu.publish, args=[md_file]).start()
    Thread(target=juejin.publish, args=[md_file]).start()
    Thread(target=sifou.publish, args=[md_file]).start()
    Thread(target=zhihu.publish, args=[md_file]).start()
