from qfluentwidgets import FluentIcon

from src.tasks.MyTimesTask import MyTimesTask


class dailycheck(MyTimesTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "日常任务"
        self.description = "检查日常任务是否完成"
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            '日常任务': "所有"
        })
        self.config_type["日常任务"] = {'type': "drop_down",
                                      'options': ['所有', '魔石矿山', '挖沙']}

    def run(self):
        self.log_info('日常任务开始运行!', notify=True)
        if self.config['日常任务'] == '所有':
            self.backtohome()
            self.enter('home_to_shijieditu')
            self.pvp()
            self.washa()
            self.taofa()
            self.ad_jiasu()
        elif self.config['日常任务'] == '魔石矿山':
            self.moshikuangshan()
        elif self.config['日常任务'] == '挖沙':
            self.washa()
        self.log_info('日常任务运行完成!', notify=True)

    def run_by_guaji(self):
            self.backtohome()
            self.enter('home_to_shijieditu')
            self.pvp()
            self.washa()
            self.taofa()
            self.ad_jiasu()





