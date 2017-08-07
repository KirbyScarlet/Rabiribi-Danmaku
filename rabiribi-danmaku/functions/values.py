"""
some local static value here.
"""
from pygame.locals import *

# Screen border
class screenborder:
    SCREEN_LEFT = 35
    SCREEN_RIGHT = 415
    SCREEN_TOP = 15
    SCREEN_BOTTOM = 465

    SCREEN_WIDTH = 380
    SCREEN_HEIGHT = 450

    SCREEN_CENTER_X = 225
    SCREEN_CENTER_Y = 240

    SCREEN_ITEM_LINE = 165

    SCREEN_CENTER = (225, 240)

    SCREEN_MID_TOP = (225, 15)
    SCREEN_MID_BOTTOM = (225, 465)
    SCREEN_MID_LEFT = (35, 240)
    SCREEN_MID_RIGHT = (415, 240)

    SCREEN_TOP_LEFT = (35, 15)
    SCREEN_TOP_RIGHT = (415, 15)
    SCREEN_BOTTOM_TOP = (35, 465)
    SCREEN_BOTTOM_RIGHT = (415, 465)

# Control keys default
class defaultkey:
    MOVE_LEFT = K_LEFT
    MOVE_RIGHT = K_RIGHT
    MOVE_UP = K_UP
    MOVE_DOWN = K_DOWN

    MOVE_SLOW = K_LSHIFT
    SHOUTING = K_z
    AMULET = K_x
    BOOST = K_c

    SWITCH_MAGIC_LEFT = K_a
    SWITCH_MAGIC_RIGHT = K_s

    @classmethod
    def direction(cls):
        return (cls.MOVE_LEFT, cls.MOVE_RIGHT, cls.MOVE_UP, cls.MOVE_DOWN)

    @classmethod
    def settingkey(cls):
        pass

    @classmethod
    def __contains__(cls, name):
        return name in tuple(cls.__dict__.values())

    @classmethod
    def filter(cls, keys):
        return {
                cls.MOVE_LEFT: keys[cls.MOVE_LEFT],
                cls.MOVE_RIGHT: keys[cls.MOVE_RIGHT],
                cls.MOVE_UP: keys[cls.MOVE_UP],
                cls.MOVE_DOWN: keys[cls.MOVE_DOWN],
                cls.MOVE_SLOW: keys[cls.MOVE_SLOW],
                cls.SHOUTING: keys[cls.SHOUTING],
                cls.AMULET: keys[cls.AMULET],
                cls.BOOST: keys[cls.BOOST],
                cls.SWITCH_MAGIC_LEFT: keys[cls.SWITCH_MAGIC_LEFT],
                cls.SWITCH_MAGIC_RIGHT: keys[cls.SWITCH_MAGIC_RIGHT]
                }

# Local difficulty
class difficulty:
    EASY = 4
    NORMAL = 8
    HARD = 16
    HELL = 32
    BUNNY = 64
    EXTRA = 48

# damage type
class damagetype:
    # physical damage
    DANMAKU = 0x64706401
    # accident damage
    CRASH = 0x64616302
    # weapen damage
    AMULET = 0x64776103
    COCOABOMB = 0x64776304
    BOOST = 0x64776305
    # buff damage
    POISON = 0x64627006
    FREEZE = 0x64626607
    BURN = 0x64626208
    CURSE = 0x64626309
    # special buff damage
    REFLECT = 0x64730063
    ENDURANCE = 0x6473ffff
    INSTANT = 0x6473115c

class pausetypes: 
    NEUTRAL = 0x7000
    PAUSING = 0x7001
    UNPAUSING = 0x70ff

class mainmenu:
    START = 0x6d01
    EXTRA_START = 0x6d02
    PRACTICE_START = 0x6d03
    SPELL_PRACTICE = 0x6d04
    PLAY_DATA = 0x6d05
    REPLAY = 0x6d06
    MUSIC_ROOM = 0x6d08
    OPTIONS = 0x6d08
    MANUAL = 0x6d09
    QUIT = 0x4c00

class startmenu:
    CASUAL = 0x6d010001
    NOVICE = 0x6d010003
    NORMAL = 0x6d010007
    HARD = 0x6d01000f
    HELL = 0x6d01001f
    BUNNY_EXCLUSION = 0x6d01003f
    IMPOSSIBLE = 0x6d01007f

class extrastart:
    EXTRA = 0x6d02000b

class practicestart:
    CASUAL = 0x6d030001
    NOVICE = 0x6d030003
    NORMAL = 0x6d030007
    HARD = 0x6d03000f
    HELL = 0x6d03001f
    BUNNY_EXCLUSION = 0x6d03003f
    IMPOSSIBLE = 0x6d03007f

class ribbonattack:
    RIBBON_BLUE = 0x720000ff
    RIBBON_GREEN = 0x7200FF00
    RIBBON_YELLOW = 0x72ffff00
    RIBBON_RED = 0x72ff0000
    RIBBON_PURPLE = 0x72ff00ff
    RIBBON_CARROT = 0x727fff00
    RIBBON_EGG = 0x72ffffff

class playdata:
    HIGHSCORE = 0x6d056863
    HS_CASUAL = 0x6d056801
    HS_NOVICE = 0x6d056803
    HS_NORMAL = 0x6d056807
    HS_HARD = 0x6d05680f
    HS_HELL = 0x6d05681f
    HS_BUNNY_EXCLUSION = 0x6d05683f
    HS_IMPOSSIBLE = 0x6d05687f
    HS_EXTRA = 0x6d0568ff

    SPELL_CARD_COLLECTED = 0x6d057363
    SCC_SECTION1_STAGE1A = 0x6d05f11a
    SCC_SECTION1_STAGE1B = 0x6d05f11b
    SCC_SECTION1_STAGE2A = 0x6d05f12a
    SCC_SECTION1_STAGE2B = 0x6d05f12b
    SCC_SECTION1_STAGE3A = 0x6d05f13a
    SCC_SECTION1_STAGE3B = 0x6d05f13b
    SCC_SECTION1_STAGE4A = 0x6d05f14a
    SCC_SECTION1_STAGE4B = 0x6d05f14b
    SCC_SECTION1_STAGE5 = 0x6d05f150
    SCC_SECTION1_STAGE6 = 0x6d05f160
    SCC_SECTION2_STAGE1A = 0x6d05f21a
    SCC_SECTION2_STAGE2A = 0x6d05f21b
    SCC_SECTION2_STAGE2A = 0x6d05f22a
    SCC_SECTION2_STAGE2B = 0x6d05f22b
    SCC_SECTION2_STAGE3A = 0x6d05f23a
    SCC_SECTION2_STAGE3B = 0x6d05f23b
    SCC_SECTION2_STAGE4 = 0x6d05f240
    SCC_SECTION2_STAGE5 = 0x6d05f250
    SCC_SECTION2_STAGE6 = 0x6d05f260
    SCC_EXTRA = 0x6d05fe00

    BUFF_COLLECTED = 0x6d056275
    BF_AMULET_CUT = 0x6d05bf01
    BF_AMULET_DRAIN = 0x6d05bf02
    BF_ARREST = 0x6d05bf03
    BF_ATTACK_BOOST = 0x6d05bf04
    BF_ATTACK_DOWN = 0x6d05bf05
    BF_ATTACK_UP = 0x6d05bf06
    BF_BADGE_COPY = 0x6d05bf07
    BF_BAN_SKILL = 0x6d05bf08
    BF_BOOST_FAIL = 0x6d05bf09
    BF_BUNNY_LOVER = 0x6d05bf0a
    BF_BURN = 0x6d05bf0b
    BF_CURSED = 0x6d05bf0c
    BF_DEFENSE_BOOST = 0x6d05bf0d
    BF_DEFENSE_DOWN = 0x6d05bf0e
    BF_DEFENSE_DROP = 0x6d05bf0f
    BF_DEFENSE_LARGE_BOOST = 0x6d05bf10
    BF_DEFENSE_UP = 0x6d05bf11
    BF_DOUBLE_DAMAGE = 0x6d05bf12
    BF_ENDURANCE = 0x6d05bf13
    BF_FATIGUE = 0x6d05bf14
    BF_FREEZE = 0x6d05bf15
    BF_GIANT = 0x6d05bf16
    BF_GIVE_ATK_DOWN = 0x6d05bf17
    BF_GIVE_DEF_DOWN = 0x6d05bf18
    BF_HALO_BOOST_LV1 = 0x6d05bf19
    BF_HALO_BOOST_LV2 = 0x6d05bf1a
    BF_HALO_BOOST_LV3 = 0x6d05bf1b
    BF_HALO_BUFF = 0x6d05bf1c
    BF_HEALING = 0x6d05bf1d
    BF_HEALTH_ABSORB = 0x6d05bf1e
    BF_HEX_CANCEL = 0x6d05bf1f
    BF_HP_RECOVER = 0x6d05bf20
    BF_HP_REGEN = 0x6d05bf21
    BF_INSTANT_DEATH = 0x6d05bf22
    BF_LUCKY_SEVEN = 0x6d05bf23
    BF_MAXHP_UP = 0x6d05bf24
    BF_MAXMP_UP = 0x6d05bf25
    BF_MONA_DOWN = 0x6d05bf26
    BF_MORTALITY = 0x6d05bf27
    BF_MP_REGEN = 0x6d05bf28
    BF_NO_BADGES = 0x6d05bf29
    BF_NULL_MELEE = 0x6d05bf2a
    BF_NULL_SLOW = 0x6d05bf2b
    BF_NUMB = 0x6d05bf2c
    BF_PONISED = 0x6d05bf2d
    BF_POWER_ABSORB = 0x6d05bf2e
    BF_QUAD_DAMAGE = 0x6d05bf2f
    BF_QUICK_REFLEX = 0x6d05bf30
    BF_REFLECT_99 = 0x6d05bf31
    BF_REVENGE_300 = 0x6d05bf32
    BF_SHRINK = 0x6d05bf33
    BF_SP_RECOVER = 0x6d05bf34
    BF_SPEED_DOWN = 0x6d05bf35
    BF_SPEED_UP = 0x6d05bf36
    BF_SPEEDY = 0x6d05bf37
    BF_STAMINA_DOWN = 0x6d05bf38
    BF_STUNNED = 0x6d05bf39
    BF_SUPER_ARMOUR = 0x6d05bf3a
    BF_SURVIVAL_INSTINCT = 0x6d05bf3b
    BF_T_MINUS_ONE = 0x6d05bf3c
    BF_T_MINUS_TWO = 0x6d05bf3d
    BF_UNSTABLE = 0x6d05bf3e
    BF_ZERO_OFFENSE = 0x6d05bf3f

    ITEM_COLLECTED = 0x6d056963
    # ?

class musicroom:
    MUSIC_01 = 0x6d086d01
    # ?

class options:
    PLAYER = 0x6d086f01
    PLAYER_1 = 0x6d08f101
    PLAYER_2 = 0x6d08f102
    PLAYER_3 = 0x6d08f103
    PLAYER_4 = 0x6d08f104
    PLAYER_5 = 0x6d08f105

    GRAPHIC = 0x6d086f02
    GRAPHIC_16BIT = 0x6d08f216
    GRAPHIC_32BIT = 0x6d08f232
    
    BGM = 0x6d086f03
    BGM_OFF = 0x6d08f300
    BGM_WAV = 0x6d08f30a
    BGM_MIDI = 0x6d08f30d
    BGM_VOLUME = 0x6d08f3ff

    SOUND = 0x6d086f04
    SOUND_VOLUME = 0x6d08f4ff

    MODE = 0x6d086f05
    MODE_FULLSCREEN = 0x6d08f5ff
    MODE_WINDOW_640_480 = 0x6d08f511
    MODE_WINDOW_960_720 = 0x6d08f533
    MODE_WINDOW_1280_960 = 0x6d08f577

    SLOWMODE = 0x6d086f06
    SLOWMODE_OFF = 0x6d08f600
    SLOWMODE_ON = 0x6d08f6ff

    RESET =  0x6d086f07

    KEYCONFIG = 0x6d086f08
    KEYCONFIG_SHOUTING = 0x6d08f87a
    KEYCONFIG_AMULET = 0x6d08f878
    KEYCONFIG_BOOST = 0x6d08f863
    KEYCONFIG_SWITCH_MAGIC_LEFT = 0x6d08f861
    KEYCONFIG_SWITCH_MAGIC_RIGHT = 0x6d08f873
    KEYCONFIG_MOVE_SLOW = 0x6d08f80a
    KEYCONFIG_MOVE_UP = 0x6d08f826
    KEYCONFIG_MOVE_DOWN = 0x6d08f827
    KEYCONFIG_MOVE_LEFT = 0x6d08f828
    KEYCONFIG_MOVE_RIGHT = 0x6d08f829
    KEYCONFIG_RESET = 0x6d08f800
    KEYCONFIG_QUIT = 0x6d08f84c

class manual:
    STORY = 0x6d096d01
    CHARACTER_INTRODUCTION = 0x6d096d02
    CI_ERINA = 0x6d08d201
    CI_RIBBON = 0x6d08d202
    # ?

class quit:
    QUIT = 0x4c00
    # just for fun
    # actually useless
    # 
    # mov ax 4c
    # int 21h
    #