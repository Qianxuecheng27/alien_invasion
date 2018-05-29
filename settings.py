class Settings():
    # 存储外星人入侵的所有设置的类
    def __init__(self):
        """初始化游戏的静态设置"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_limit = 3

        # bullet setting
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        #alien setting
        self.fleet_drop_speed = 10
        
        
        #游戏速度系数
        self.speedup_scale = 1.1
        #外星人点数提高洗漱
        self.score_scale = 1.5

        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """初始化游戏节奏相关的变量"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction=1(right) or -1(left)
        self.fleet_direction = 1

        #记分
        self.alien_points = 50

    def increase_speed(self):
        """提高游戏速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)