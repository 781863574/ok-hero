import time
from src.tasks.MyTriggerTask import MyTriggerTask
from src.tasks.dailycheck import dailycheck

class guaji(MyTriggerTask, dailycheck):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "挂机"
        self.description = "挂机"
        self.relog_flag = False
        self.isdaily_flag = False
        self.level = 0

    def run(self):
        # self.isdaily()
        try:
            self.guaji()
        except (ValueError, IndexError):
            print('挂机: 未找到等级')
        self.sleep(5)

    def guaji(self):
        self.error_detect()
        level_tmp = self.level
        self.level = int(self.ocr(0.47, 0.07, 0.53, 0.11)[0].name.replace(',', '').replace('.', ''))
        print(level_tmp, self.level)
        if(int(self.level) > 17000) and (self.level < level_tmp):
            self.click_relative(0.50, 0.96)
            self.sleep(1.5)
            self.click_relative(0.50, 0.78)
            self.sleep(1.5)
            self.click_relative(0.55, 0.81)
            self.sleep(1.5)
            self.click_relative(0.55, 0.56)
            self.sleep(10)
            self.click_relative(0.50, 0.10)
            now = time.strftime("%m%d-%H:%M")
            with open('logs/guaji.log',  "a") as f:
                f.write(str(level_tmp) + '\t' + str(self.level) + '\t' + str(now) + '\n')


    def isdaily(self):
        if (self.relog_flag == False):
            self.logout()
            self.login()
            self.relog_flag = True
        if (self.isdaily_flag == False):
            self.run_by_guaji()
            self.isdaily_flag = True
