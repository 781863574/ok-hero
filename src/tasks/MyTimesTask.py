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
        lv = self.ocr(0.46,0.388,0.505,0.412)[0].name.replace('Lv','').replace('.','').replace(',','').replace('？','0').replace('?','0')
        return lv

    def pvp_confirm(self):
        self.click_relative(0.43,0.87)
        self.sleep(0.5)

    def pvp_complete(self):
        click1 = [0.41, 0.73]
        click2 = [0.50, 0.73]
        click3 = [0.59, 0.73]
        click = [click1, click2, click3]
        lv = []
        for i in click:
            if i != click3:
                self.click_relative(i[0], i[1])
                self.sleep(0.5)
                level = self.pvp_checklv()
                lv.append(int(level))
                if int(level) < 2000:
                    self.click_relative(0.55,0.73)
                    # self.loop_check_one('is', 'pvp_confirm', self.pvp_confirm)
                    box = [0.415, 0.85, 0.45, 0.885]
                    self.loop_check_ocr('is', box, '确认', self.pvp_confirm)
                    break
                self.back()
            else:
                self.click_relative(0.59,0.86)
                # self.loop_check_one('is', 'pvp_confirm', self.pvp_confirm)
                box = [0.415, 0.85, 0.45, 0.885]
                self.loop_check_ocr('is', box, '确认', self.pvp_confirm)
        with open('logs/pvp.log',  "a") as f:
            f.write(str(lv) + '\t' + 'pvp_complete' + '\n')

    def pvp(self):
        self.loop_check_one('is', 'pvp_zhuye', self.pvp_buyticket)
        box = [0.50, 0.59, 0.538, 0.63]
        self.loop_check_ocr('not', box, '0/5', self.pvp_complete)


    def washa_wa(self):
        click1 = [0.57, 0.70]
        click2 = [0.44, 0.70]
        click3 = [0.50, 0.64]
        click = [click1, click2, click3]
        for i in click:
            self.click_relative(i[0], i[1])
            self.sleep(0.2)
            if (self.find_one('washa_chu1')) and not self.find_one('washa_chu3'):
                self.sleep(1)
                self.click_relative(0.60, 0.24)
                self.sleep(0.1)
                self.click_relative(0.60, 0.24)
                self.sleep(0.1)
                self.click_relative(0.55, 0.56)
                self.sleep(1.5)
                self.click_relative(0.50, 0.78)
                self.sleep(1.0)
                return None
            elif (self.find_one('washa_chu3')):
                self.sleep(2.5)
                self.click_relative(0.45, 0.66)
                self.sleep(1.5)
                self.click_relative(0.50, 0.78)
                self.sleep(1.0)
                return None
        self.sleep(0.2)
        self.click_relative(0.60, 0.24)
        self.sleep(0.1)
        self.click_relative(0.55, 0.56)
        self.sleep(1.5)
        self.click_relative(0.50, 0.78)
        self.sleep(1.0)

    def washa(self):
        box = [0.40, 0.28, 0.44, 0.305]
        self.loop_check_ocr('not', box, '0/300', self.washa_wa)

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
        box = [0.415, 0.85, 0.45, 0.885]
        ocr = self.ocr(box[0], box[1], box[2], box[3])
        str = ocr[0].name
        print(str)
        self.log_info('ocr识别信息: ' + str, notify=True)
        