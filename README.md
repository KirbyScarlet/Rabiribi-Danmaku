================================
    rabiribi-danmaku 游戏企划  
================================

本作由同名游戏rabiribi改编
暂未获得授权
@KirbyScarlet

此游戏类型为纵版弹幕通关类游戏

（1）：欢迎屏幕
	
	游戏欢迎界面采用 press any key to continue
	
	主界面内容：
	
		start game
		extra mode
		spell practice
		practice mode
		music house
		replay
		options
		quit
	
	详细内容提示：
	
	1：start game：
		两个剧情，分为 一周目 和 二周目
	2：extra mode：
		extra选择确定的界面，然后选择人物
	3：spell practice：
		练习 boss 的 spell 攻击，上下为选择 spell 类型和难度，左右为选择人物
	4：practice mode：
		先选择 关卡 ，再选择人物，只能练习进入过的关卡
	5：replay：
		可以查看保存的replay
	6：music house：
		通过已经听过的 music 解锁模式进行
	7：options：
		修改按键设置，修改语言，修改全屏方式
		
（2）：难度设置

	采用 5 个难度等级，
	
		easy：几乎站着不动都不会受伤的难度，适合对游戏完全不了解的玩家
		normal：对此类游戏有一定的了解，适合一般玩家
		hard：想挑战一下自己，有一定难度的模式，适合高端玩家
		hell：是时候表演真正的技术了！
		bunny exclusion：抖M玩法

（3）：模式设置
	
	分为 一周目 和 二周目 和 extra
	
	一周目：
		分为6个stage，根据选择的人物不同，会出现不同的boss。
	
	extra模式：
		难度介于 normal 和 hard 之间
		normal 模式任意人物无续关通过 一周目 后即可开启 extra 模式
		extra 中可选的人物为通过 一周目 的人物
		
	二周目：
		分为6个stage，根据选择人物的不同，会出现不同的boss。
		一周目 任意人物任意难度通过后，可开启对应难度，对应人物的 二周目
	
（4）：人物设置

	主人公为 erina 和 ribbon
	
	其中，erina 只负责伤害判定，ribbon 只负责输出
	
	伤害判定：
		人物采用血条制，默认为100，打过一个关卡最大值+10，血量+10
		可以通过获取血瓶道具和徽章道具增加最大血量
		extra模式血量初始值为150
		不同弹幕类型和不同难度系数将会造成不同的伤害
		受伤后不会回到初始位置，会被弹幕击退一定距离，会产生硬直，会产生无敌状态以及清屏
	
	擦弹判定：
		erina 判定点为人物正中心2个像素大小
		擦弹范围为10个像素大小
		根据难度不同，擦弹一定数量产生能量，并获得威力加成
	
	输出设定：
		游戏开始前可选择7种输出类型，其中第七种要求hard难度二周目通过后开启
		选择之后游戏过程中不可更改，【高密度状况的弹幕预判跟不上切换操作】
		高速攻击时为较密的弹幕攻击，低速攻击为魔法攻击附带低密度的弹幕攻击
		extra模式允许更改输出类型，只能更改一周目通关后的输出类型
	
	bomb设定和boost设定：
		bomb为护身符，默认4个，可随游戏时间推移恢复
		bomb过程中产生硬直，清屏弹幕，以及对boss产生伤害。
		击破任意boss可获得一定奖励，可用于恢复少量护身符和增加bp
		当bp量多余一半总量时可以boost，为对应攻击方式的boost
		
	威力设定：
		威力基数为定值
		短时间内可通过 擦弹 和 造成伤害 获得威力加成
		一段时间内没有造成伤害 或 没有擦弹判定 将减少威力加成
		spell阶段内威力加成比率减少，未受伤将不会减少威力加成
	
	击破设定：
		boss的spell攻击附带时间限制
		超过spell时间后，boss附带 攻击力x4，ribbon附带 攻击力x2
		若无伤击破，无论是否在时间内，计算bonus
		耐久攻击无时间限制
	
（5）：其他设定

	游戏本体为刷分类游戏，分数加点：
		输出伤害
		击破后mp数量
		bonus值
		不包括擦弹数量【否则spell时间外的擦弹数量～23333333
	
（6）：具体boss设定【待定】
	
	一周目：(12)
		stage1: cocoa, ashuri
		stage2: kotri(g), pandora
		stage3: rita, saya
		stage4: (nieve, nixie), (vanilla, chocolate)
		stage5: miru
		stage6: noah,???
	二周目：(7)
		stage1: seana(1), cicini
		stage2: seana(2), syaro
		stage3: aruraune, lilith
		stage4: kotri(r)
		stage5: miriam
		stage6: rumi
	extra:(1)
		kotri(b)
		irisu
