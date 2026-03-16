from ok import TriggerTask


class MyTriggerTask(TriggerTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = {
            'home_to_shijieditu': (0.62,0.53,'shijieditu'),
            'shijieditu_to_pvp': (0.39,0.42,'pvp_zhuye'),
            'shijieditu_to_washa': (0.60,0.59,'washa_zhuye'),
            'shijieditu_to_taofa': (0.57,0.73,'taofa_zhuye'),
        }

    def error_detect(self):
        if (self.find_one('error')):
            self.sleep(1)
            self.click_relative(0.50, 0.96)
            self.sleep(1)

    def login(self):
        while (self.find_one('login_zhuye')) or not self.find_one('home'):
            for i in range(2):
                self.click_relative(0.50, 0.70)
                self.sleep(1)
            self.click_relative(0.44, 0.64)
            self.sleep(1)
            self.click_relative(0.50, 0.50)
            self.sleep(1)
            if (self.find_one('home')):
                break
        for i in range(10):
            self.click_relative(0.50, 0.95)
            self.sleep(1)
        self.sleep(5)

    def logout(self):
        self.click_relative(0.205, 0.018)
        self.sleep(5)
        self.click_relative(0.63, 0.37)
        self.sleep(5)
        while not (self.find_one('login_zhuye')):
            self.click_relative(0.50, 0.95)
            self.sleep(1)

    def ad_cancel(self):
        self.click_relative(0.50, 0.96)
        self.sleep(1.5)

    def ad_maoxianrizhi(self):
        self.click_relative(0.37, 0.59)
        self.sleep(0.5)
        self.click_relative(0.45, 0.66)
        self.sleep(0.5)
        self.click_relative(0.45, 0.60)
        self.sleep(0.5)
        self.click_relative(0.50, 0.10)
        self.sleep(0.5)

    def ad_zhaohuan(self):
        self.enter('home_to_shijieditu')
        self.enter('shijieditu_to_taofa')
        self.click_relative(0.62, 0.96)
        self.sleep(0.5)
        self.click_relative(0.41, 0.88)
        self.sleep(0.5)
        self.click_relative(0.56, 0.64)
        self.sleep(1.5)
        self.click_relative(0.50, 0.91)
        self.sleep(0.5)


