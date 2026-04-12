import time

from ok import BaseTask

class MyBaseTask(BaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = {
            'home_to_shijieditu': (0.62,0.53,'shijieditu'),
            'shijieditu_to_pvp': (0.39,0.42,'pvp_zhuye'),
            'shijieditu_to_washa': (0.60,0.59,'washa_zhuye'),
            'shijieditu_to_taofa': (0.57,0.73,'taofa_zhuye'),
        }

    def backtohome(self):
        while not (self.find_one('backtohome')):
            self.back()
            self.sleep(0.1)
        self.back()

    def wait_shijieditu(self):
        self.wait_feature('shijieditu')
        self.sleep(0.8)

    def enter(self, through):
        # 等待进入指定界面，使用循环检查
        start_time = time.time()
        timeout = 30  # 30秒超时
        
        while time.time() - start_time < timeout:
            if self.find_one(self.position[through][2]):
                break
            else:
                self.click_relative(self.position[through][0], self.position[through][1])
                self.sleep(1)  # 每0.1秒检查一次
        self.sleep(0.8)

    def loop_ocr_click(self, box, ocr_str, click):
        while True:
            if self.ocr(box[0], box[1], box[2], box[3], match=ocr_str):
                self.click_relative(click[0], click[1])
                break
            else:
                pass
            self.sleep(0.1)

    def loop_check_ocr(self, is_not, box, ocr_str, func):
        if is_not == 'is':
            while True:
                if self.ocr(box[0], box[1], box[2], box[3], match=ocr_str):
                    func()
                    break
                else:
                    pass
                self.sleep(0.1)
        elif is_not == 'not':
            while True:
                if self.ocr(box[0], box[1], box[2], box[3], match=ocr_str):
                    break
                else:
                    func()
                self.sleep(0.1)

    def moshikuangshan(self):
        self.click_relative(0.62,0.53)
        self.wait_feature('shijieditu')
        self.sleep(0.8)
        self.click_relative(0.40,0.25)
        self.wait_feature('wakuang_zhuye')
        self.sleep(0.8)
        self.click_relative(0.54,0.61)
        self.sleep(0.8)
        for i in range(3):
            self.click_relative(0.45,0.56)
            self.sleep(0.8)
            self.click_relative(0.50,0.10)
            self.sleep(0.8)
            self.click_relative(0.50,0.10)
            self.sleep(0.8)
        for i in range(3):
            self.click_relative(0.55,0.56)
            self.sleep(0.8)
            self.click_relative(0.50,0.10)
            self.sleep(0.8)
        self.click_relative(0.50,0.10)
        self.sleep(0.8)
        # 点击扫荡
        self.click_relative(0.55,0.89)
        self.sleep(0.1)
        self.click_relative(0.58,0.56)
        self.sleep(0.1)
        self.click_relative(0.56,0.61)
        self.sleep(0.8)
        self.back()
        self.sleep(0.8)
        self.back()
        self.sleep(0.8)

    def wulin(self):
        # 等待世界地图加载
        self.wait_feature('shijieditu')
        self.sleep(0.8)
        # 进入雾林
        self.click_relative(0.52,0.22)
        self.sleep(0.1)
        self.click_relative(0.58,0.47)
        self.wait_feature('wulin_zhuye')
        self.sleep(0.8)
        # 开始执行
        self.click_relative(0.59,0.82)
        self.sleep(0.8)
        self.click_relative(0.55,0.55)
        self.sleep(0.8)
        self.wait_feature('wulin_jieshu')
        self.sleep(0.8)
        self.click_relative(0.50,0.87)
        self.sleep(0.8)
        self.wait_feature('wulin_zhuye')
        self.sleep(0.8)
        self.back()

    def yuansuyundao(self):
        # 等待世界地图加载
        self.wait_feature('shijieditu')
        self.sleep(0.8)
        # 进入元素云岛(风)
        self.click_relative(0.39,0.61)
        self.sleep(0.1)
        self.click_relative(0.57,0.63)
        self.sleep(0.1)
        self.wait_feature('yuansuyundao_feng')
        self.sleep(0.8)
        # 开始执行扫荡
        self.click_relative(0.61,0.89)
        self.sleep(0.1)
        self.click_relative(0.56,0.62)
        self.sleep(0.8)
        # 回到世界地图
        self.back()
        self.sleep(0.1)
        self.back()
        self.sleep(0.1)

    def tiankongzhita(self):
        # 等待世界地图加载
        self.wait_feature('shijieditu')
        self.sleep(0.8)
        # 进入天空之塔
        self.click_relative(0.50,0.55)
        self.sleep(0.1)
        self.click_relative(0.43,0.48)
        self.sleep(0.1)
        self.wait_feature('tiankongzhita')
        self.sleep(0.8)
        # 开始执行挑战
        for i in range(3):
            self.click_relative(0.50,0.87)
            self.sleep(0.1)
            self.wait_feature('tiankongzhita_shengli')
            self.sleep(0.8)
            self.click_relative(0.50,0.87)
            self.sleep(0.8)
            self.wait_feature('tiankongzhita')
            self.sleep(0.8)
        self.back()