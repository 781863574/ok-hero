from src.tasks.MyBaseTask import MyBaseTask

class MyTimesTask(MyBaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pvp_buyticket_flag = False
        self.taofa_ad_flag = False

    def pvp_buyticket(self):
        if self.pvp_buyticket_flag == False:
            for i in range(10):
                self.click_relative(0.54,0.61)
                self.sleep(0.1)
                self.click_relative(0.55,0.56)
                self.sleep(1)
                self.click_relative(0.50,0.10)
                self.sleep(0.1)
            self.pvp_buyticket_flag = True

    def pvp_checklv(self):
        lv = self.ocr(0.46,0.39,0.50,0.41)[0].name.replace(',','').replace('Lv.','').replace('？','0')
        return lv

    def pvp_complete(self):
        click1 = [0.41, 0.73]
        click2 = [0.50, 0.73]
        click3 = [0.59, 0.73]
        click = [click1, click2, click3]
        lv = []
        for i in click:
            self.click_relative(i[0], i[1])
            self.wait_feature('pvp_Lv')
            lv.append(self.pvp_checklv())
            self.back()
            self.sleep(0.1)
        min_value = min(lv)
        min_index = lv.index(min_value)
        self.sleep(0.5)
        if min_index == 0:
            self.click_relative(0.41,0.86)
        elif min_index == 1:
            self.click_relative(0.50,0.86)
        elif min_index == 2:
            self.click_relative(0.59,0.86)
        # 同时等待胜利或失败特征，使用循环检查
        import time
        start_time = time.time()
        timeout = 30  # 30秒超时
        
        while time.time() - start_time < timeout:
            if self.find_one('pvp_shengli') or self.find_one('pvp_baibei'):
                break
            self.sleep(0.1)  # 每0.1秒检查一次
        
        if time.time() - start_time >= timeout:
            self.log_warning('等待胜利或失败特征超时', log=True)
        self.click_relative(0.50,0.86)
        self.sleep(0.5)

    def pvp(self):
        # if not (self.find_one('ispvp', threshold=0.99)):
            # 进入pvp界面
            self.enter('shijieditu_to_pvp')
            # 购买pvp门票
            self.pvp_buyticket()
            # 开始执行pvp任务
            while not (self.find_one('pvp_wanbi',threshold=0.99)):
                self.pvp_complete()
            self.back()
            self.wait_feature('shijieditu')
            self.sleep(0.8)

    def washa_wa(self):
        click1 = [0.57, 0.70]
        click2 = [0.44, 0.70]
        click3 = [0.50, 0.64]
        click = [click1, click2, click3]
        for i in click:
            if (self.find_one('washa_chuhuo')) or (self.find_one('washa_chudahuo')):
                break
            self.click_relative(i[0], i[1])
            self.sleep(1.5)

    def washa_huan(self):
        if (self.find_one('washa_chuhuo')):
            self.click_relative(0.60, 0.24)
            self.sleep(0.1)
            self.click_relative(0.60, 0.24)
            self.sleep(0.1)
            self.click_relative(0.55, 0.56)
            self.sleep(1.5)
            self.click_relative(0.50, 0.78)
        elif (self.find_one('washa_chudahuo')):
            self.click_relative(0.45, 0.66)
            self.sleep(1.5)
            self.click_relative(0.50, 0.78)
        elif (self.find_one('washa_zhuye')):
            self.click_relative(0.60, 0.24)
            self.sleep(0.1)
            self.click_relative(0.55, 0.56)
            self.sleep(1.5)
            self.click_relative(0.50, 0.78)
        self.sleep(1.5)

    def washa(self):
        if not (self.find_one('iswasha', threshold=0.99)):
            # 进入星之海岸
            self.enter('shijieditu_to_washa')
            # 开始执行挖沙
            while not (self.find_one('washa_wanbi', threshold=0.99)):
                self.washa_wa()
                self.washa_huan()
            self.back()
            self.wait_feature('shijieditu')
            self.sleep(0.8)

    def taofa_ad(self):
        self.click_relative(0.46, 0.88)
        self.sleep(0.1)
        self.click_relative(0.45, 0.74)
        self.sleep(0.1)
        self.taofa_ad_flag = True

    def taofa_normal(self):
        self.click_relative(0.46, 0.88)
        self.sleep(0.5)
        self.click_relative(0.59, 0.44)
        self.sleep(0.5)
        self.click_relative(0.56, 0.74)
        self.sleep(0.5)
        for i in range(2):
            self.click_relative(0.50, 0.87)
            self.sleep(1.5)
            self.click_relative(0.50, 0.87)
            self.sleep(0.5)
        self.click_relative(0.61, 0.82)
        self.sleep(0.5)
        self.click_relative(0.61, 0.89)
        self.sleep(0.5)
        self.click_relative(0.61, 0.83)
        self.sleep(0.5)
        self.back()
        self.sleep(0.1)
        self.back()
        self.sleep(0.1)

    def taofa(self):
        if not (self.find_one('istaofa', threshold=0.99)):
            # 进入讨伐界面
            self.enter('shijieditu_to_taofa')
            # 开始执行讨伐任务
            self.taofa_normal()

    def ad_bonus_isfull(self):
        if (self.find_one('ad_bonus_unfull', threshold=0.99)):
            self.sleep(1)
            self.back()
            self.sleep(1)

    def ad_jiasu(self):
        self.click_relative(0.36, 0.34)
        self.sleep(0.5)
        click1 = [0.59, 0.27]
        click2 = [0.59, 0.37]
        click3 = [0.59, 0.47]
        click = [click1, click2, click3]
        for i in click:
            self.click_relative(i[0], i[1])
            self.sleep(0.5)
            self.ad_bonus_isfull()
        