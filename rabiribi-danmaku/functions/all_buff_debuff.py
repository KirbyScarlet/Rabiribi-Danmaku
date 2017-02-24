class AllBuffs:
    def __init__(self):
        """
        define all buffs
        """
        self.speed_down = 0
        # Speed lowered by 20%
        self.numb = 0
        # All movement ceases intermittently
        self.ponised = 0
        # Lose HP over time
        self.attack_down = 0
        # Attack lowered by 25%
        self.defense_down = 0
        # Defense lowered by 25%
        self.cursed = 0
        # Take 50% of damage given.
        # Enemies with "Cursed" take 2% damage of their Max. HP
        # with a maximum damage of 666 points
        self.stunned = 0
        # All movement ceases.
        self.ban_skill = 0
        # Can't perform physical, non-magic attacks.
        self.mona_down = 0
        # Lose MP over time
        self.freeze = 0
        # When attacking, lose 3% HP every second.
        self.burn = 0
        # Lose 15% HP every 2 seconds.
        # Enemies with "Burn" lose 2-3 HP every 0.05 Seconds
        self.attack_up = 0
        # Attack raised by 25%
        self.defense_up = 0
        # Defense raised by 25%
        self.hp_recover = 0
        # Recover 1-3 HP every 0.25 seconds
        self.sp_recover = 0
        # Improve SP recovery rate.
        self.shrink = 0
        # Speed increased by 30%, attack lowered by 15%.
        # and damage taken increased by 30%
        # something else happens too
        self.giant = 0
        # Speed decreased by 50%, attack raised by 50%
        # and damage taken reduced by 50%
        # Something esle happens too.
        self.arrest = 0
        # A chance to slow down opponents by 20% when attacking
        self.speed_up = 0
        # Speed increased by 25%.
        self.badge_copy = 0
        # Opponent's badge perks are replicated.
        self.null_melee = 0
        # No damage taken from physical attacks.
        # Damage taken from carrot bomb increased by 62.5%
        self.defense_boost = 0
        # Damage taken reduced by 10-50%
        # 5%-25% in Boss Rush mode
        self.defense_drop = 0
        # Damage taken increased by 100%-300%
        self.stamina_down = 0
        # SP consumption increased by 325%
        self.null_slow = 0
        # Cannot be slowed down.
        self.super_armour = 0
        # No stun effect after being damaged
        self.quad_damage = 0
        # Attack raised by 400%
        self.double_damage = 0
        # Attack raised by 200%
        self.speedy = 0
        # Movement speed increased by 20%
        self.maxhp_up = 0
        # Max. HP increased proportional to characters unlocked.
        # Enemies with this status have a 10% Max. HP increase.
        self.maxmp_up = 0
        # Max. MP increased proportional to characters unlocked.
        # Enemieswith this status have greater attack frequency.
        self.amulet_cut = 0
        # Amulet consumption lowered by 25%.
        self.hp_regen = 0
        # Recover 2 HP every 1.5 seconds.
        # Enemies with this status recover 2% of Max. HP.
        self.mp_regen = 0
        # Recover 2MP every second.
        self.give_atk_down = 0
        # A chance to give opponents "Attack Down" when attacking.
        self.give_def_down = 0
        # A chance to give opponents "Defense Down" when attacking.
        self.unstable = 0
        # Speed changes randomly
        self.boost_fail = 0
        # Lose BP over time.
        self.hex_cancel = 0
        # No damage taken from every 6th attack.
        self.lucky_seven = 0
        # Every 7th successful attack inflicts 77% more damage.
        self.quick_reflex = 0
        # Lowers stun time by 75%.
        self.defense_large_boost = 0
        # Damage taken reduced by 50-100%.
        # 25%-50% in Boss Rash
        self.endurance = 0
        # Immune to all attacks, but lose HP over time.
        self.fatigue = 0
        # Speed and jump height lowered by 20%.
        self.reflect_99 = 0
        # 100% of damage taken reflected back to opponent.
        # Only applicable for attacks above 99 points.
        # Opponent's health will not fall below 1 HP
        self.survival_instinct = 0
        # HP cannot fall below 1.
        self.amulet_drain = 0
        # Lose amulet charge over time.
        self.mortality = 0
        # Lose all invulnerability when performing any moves.
        self.no_badges = 0
        # Lose effects from equipped badges.
        self.instant_death = 0
        # All attacks cause 4444 points of damage.
        self.health_absorb = 0
        # Absorb HP equal to 2 times the damage given.
        self.power_absorb = 0
        # Inflict a 100% SP, 33% MP, and 25% BP reduction in the opponent.
        self.revenge_300 = 0
        # "Instant death" status dealt to opponent.
        # Triggered when damage taken from one attack >300 points.
        self.bunny_lover = 0
        # Damage taken reduced by 50% when the opponent is a bunny
        self.healing = 0
        # Recover HP over time.
        self.t_minus_two = 0
        # Gain "T Minus One" status after a successful attack.
        self.t_minus_one = 0
        # Gain "Attack Boost" status after a successful consecutive attack.
        self.attack_boost = 0
        # Bullet hell density increased.
        self.zero_offense = 0
        # Attack reduced by 100%
        self.halo_buff = 0
        # Damage taken reduced by 10% after three "Game Over"
        # Status removed after "Halo Boost" expires.
        # Does not apply above Normal difficulty
        self.halo_boost_lv1 = 0
        # Damage taken -15%. Amulet recharges 33% faster.
        # Recover 1 HP for every three successful attacks.
        # Gained after 3-4 "Game Over", No buff above "Normal"
        self.halo_boost_lv2 = 0
        # Damage taken -27.5%. Amulet recharges 67% faster.
        # Recover 1 HP for every two successful attacks.
        # Gained after 5-6 "Game Over", No buff above "Noraml"
        self.halo_boost_lv3 = 0
        # Damage taken -40%. Amulet recharges 100% faster.
        # Recover 1 HP for every successful attack.
        # Gained after 7+ "Game Over", No buff above "Normal"

