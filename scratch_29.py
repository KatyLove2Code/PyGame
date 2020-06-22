"""
место под описание ошибок
"""

from pygame import *

WIN_WIDTH = 1920
WIN_HEIGHT = 1080
BACKGROUND_COLOR = "#FFFFFF"
PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30
PLATFORM_COLOR = "#000000"
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
Rect = bg.get_rect()

SPIKES = "1" #шипы


class Platform(sprite.Sprite):
    def __init__(self, groups, plat_type, x, y):
        super().__init__(groups[0], groups[1])
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        if plat_type == "-":
            self.image.fill(Color("#123456"))
            self.rect = self.image.get_rect().move(x, y)
        elif plat_type == SPIKES:
            self.image.fill(Color("#654321"))
            self.rect = self.image.get_rect().move(x, y)
        elif plat_type == "2":
            self.image.fill(Color("#011032"))
            self.rect = self.image.get_rect().move(x, y)
        elif plat_type == "3":
            self.image.fill(Color("#555353"))
            self.rect = self.image.get_rect().move(x, y)
        elif plat_type == "5":
            self.image.fill(Color("#125364"))
            self.rect = self.image.get_rect().move(x, y)




#1 - шипы
#2 - мобы
#5 - рычаг который триггерится при соприкосновении с игроком и убивающий то скопление из 4 мобов слева снизу от него
#3 - 'сокровище', типо бонуса
level = [
"----------------------------------------------------------------",
"----------------------------------------------------------------",
"----------------------------------------------------------------",
"---                         -                                ---",
"---                                                          ---",
"--- ---------------               -           --          ------",
"---        -       --         -   - -            -------     ---",
"---        -          --      - - - -       -                ---",
"----       -               ------------      -               ---",
"---        -----------  --              -    -       -----  ----",
"--- ------              -                     -  -           ---",
"---                     -              -           -       -----",
"---                        -------------        -            ---",
"--- ------------------   -                     -          ------",
"---                      -                    -       --     ---",
"---                      -----------------   -               ---",
"-------------------------                   -           -    ---",
"---                                       -----------------  ---",
"---                                                         ----",
"---                                                          ---",
"---                   -             ---  -----------------------",
"---   ------------        ----------                         ---",
"----             - -    -                                    ---",
"-----            -                                           ---",
"------           -       -             - ---                 ---",
"---              -   -         --------    -                 ---",
"---   ----       -        -                ----- - -- -----  ---",
"---   --------   -                                          ----",
"---            --- -       -    - -    --                    ---",
"---            ---          ---     --                     -----",
"---       --------                  --   -                ------",
"---       --------   -  --      ------       ----------  -------",
"---   ------------              ------    -                  ---",
"---0000000000000000000000000500000000000000000000000000000000---",
"---0000000000000000000000000000000000000000000000000000000030---",
"---0---------------200000000000000-00000000000--0000000000------",
"---00000000-0000000--000000000-000-0-000000000000-------00000---",
"---00000000-0000000000--000010-1-1-1-0000000-0000000000000000---",
"----0000000-020202020000000------------000000-000000000000000---",
"---01010100-----------00--00000000000000-0000-0000000-----00----",
"---0------00000000000000-000000000000000000000-00-00000000000---",
"---000000000000000000000-00010101001010-00000000000-0000000-----",
"---002000000000000001100000-------------00000000-000000000000---",
"---0------------------000-000000000000000000000-0000000000------",
"---0000000000000000000000-00002000200000000001-0000000--00000---",
"---0000000000000000000010-----------------000-000000000000000---",
"-------------------------0000000000000000000-00000000000-1000---",
"---000000000000000000000000000000000000000-----------------00---",
"---000000000000000000000000000000000000000000000000000000000----",
"---0000000000000000000010000000000000000000000020002000200000---",
"---00000000000000000000-000100000000---00-----------------------",
"---000------------00000000----------0000000000000000000000000---",
"----0000000000000-0-0000-000000000000000000000000000000000000---",
"-----000000000000-0000000000000000000001000000000000000000000---",
"------00000000000-0000000-0000000000000-0---00000000000000000---",
"---00000100000000-000-000000000--------0000-00000000000001000---",
"---000----1000000-00000000-0000000000000000-----0-0--0-----00---",
"---000--------001-000000000000000010000010000000000000000000----",
"---000000000000---0-0000000-1010-0-0000--00000000000000000000---",
"---000000000000---0000000000---00000--000000000000000000000-----",
"---0000000--------000000000000000000--000-0000001010010000------",
"---0000000--------000-00--000000------0000000----------00-------",
"---0x0------------11111111100000------1000-000000000000110000---",
"----------------------------------------------------------------",
"----------------------------------------------------------------",
"----------------------------------------------------------------"]
