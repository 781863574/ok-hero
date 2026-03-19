from src.tasks.MyBaseTask import MyBaseTask
import json
import time
import os

class MyTimesTask(MyBaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.taofa_ad_flag = False
        self.today = time.strftime("%Y%m%d")
        self.today_log = f"logs/log_{self.today}.json"
        if not os.path.exists(self.today_log):
            self.log ={
                "pvp_buyticket_flag" : False,
            }
            with open(self.today_log, "w") as f:
                json.dump(self.log, f)
        else:
            with open(self.today_log, "r") as f:
                self.log = json.load(f)
    
    # 装饰器函数
    # def loop_check_one(is_f, feature):
    #     def loop_check(func):
    #         def wrapper(self, *args, **kwargs):
    #             while True:
    #                 if is_f == 'is':
    #                     if self.find_one(feature):
    #                         return func(self, *args, **kwargs)
    #                     else:
    #                         self.sleep(0.1)
    #                 elif is_f == 'not':
    #                     if self.find_one(feature):
    #                         break
    #                     else:
    #                         return func(self, *args, **kwargs)
    #         return wrapper
    #     return loop_check

    def loop_check_one(self, is_not, feature, func):
        if is_not == 'is':
            while True:
                if self.find_one(feature):
                    self.sleep(1)
                    func()
                    break
                else:
                    self.sleep(0.5)
        elif is_not == 'not':
            while True:
                if self.find_one(feature):
                    break
                else:
                    func()

    def loop_check_ocr(self, is_not, box, ocr_str, func):
        if is_not == 'is':
            while True:
                if self.ocr(box[0], box[1], box[2], box[3], match=ocr_str):
                    self.sleep(1)
                    func()
                    break
                else:
                    pass
                self.sleep(0.5)
        elif is_not == 'not':
            while True:
                if self.ocr(box[0], box[1], box[2], box[3], match=ocr_str):
                    break
                else:
                    func()
                self.sleep(0.5)

    def loop_ocr(self, box, func):
        while True:
            lv = self.ocr(box[0], box[1], box[2], box[3])
            if lv:
                func()
                return lv
            else:
                pass
            self.sleep(0.5)

    def pvp_buyticket(self):
        if self.log["pvp_buyticket_flag"] == False:
            for i in range(10):
                self.click_relative(0.54,0.61)
                self.sleep(0.1)
                self.click_relative(0.55,0.56)
                self.sleep(1)
                self.click_relative(0.50,0.10)
                self.sleep(0.1)
            self.log["pvp_buyticket_flag"] = True
            with open(self.today_log, "w") as f:
                json.dump(self.log, f)

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
            box = []
            level = self.loop_ocr(box, self.pvp_checklv)
            lv.append(level)
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
        self.loop_check_one('is', 'pvp_zhuye', self.pvp_buyticket)
        box = [0.51, 0.59, 0.54, 0.63]
        self.loop_check_ocr('not', box, '0/5', self.pvp_complete)


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
        while True:
            if self.find_one('washa_zhuye'):
                print("开始执行挖沙任务")
                while not (self.find_one('washa_wanbi', threshold=0.9)):
                    self.washa_wa()
                    self.washa_huan()
                print("挖沙任务完成")
                break
            else:
                self.sleep(0.1)

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

    def ocr_test(self):
        # fenzi = [1237,830,1330,880]
        # fenmu = [2432,1408,2432,1408]
        # box = [0,0,0,0]
        # for i in range(4):
        #     print(i)
        #     box[i] = fenzi[i]/fenmu[i]
        # print(box)
        box = [0.51, 0.59, 0.54, 0.63]
        ocr = self.ocr(box[0], box[1], box[2], box[3])
        str = ocr[0].name
        print(str)
        self.log_info('ocr识别信息: ' + str, notify=True)
        