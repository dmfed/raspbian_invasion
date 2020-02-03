class Settings:
    def __init__(self):
        self.screen_width = 830
        self.screen_height = 1000
        self.bg_color = (138, 76, 169)
        self.bg_image = 'images/background.png'
        self.ship_image = 'images/ship2_small.png'
        self.ship_speed = 8.0
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 10
        self.bullet_sound = 'sounds/bullet.ogg'
        self.alien1_image = 'images/alien1.png'
        self.alien2_image = 'images/alien2.png'
        self.aliens_images = [self.alien1_image, self.alien2_image]
        self.alien_speed = 6.0
        self.fleet_drop_speed = 30
        self.fleet_direction = 1
        self.fleet_sound = 'sounds/fleet.ogg'
        self.collision_sound = 'sounds/collision.ogg'
        self.waves = 3