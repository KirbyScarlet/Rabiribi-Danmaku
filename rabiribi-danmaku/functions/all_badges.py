class Badges:
    def __init__(self):
        self.health_plus = 0         # Max. Health +7.5%
        self.health_surge = 0       # Max. Health +12.5%
        self.mana_plus = 0          # Max. MP +12.5%
        self.mana_surge = 0         # Max. MP +20%
        self.crisis_boost = 0         # Attack +25% when HP <20%
        self.atk_grow = 0           # Attack damage output +1~2. Faster BPO recovery if >10 badges equipped.
        self.def_grow = 0           # All damage taken -1~2. Drop a recovery carrot if >10 badges equipped.
        self.atk_trade = 0          # Attack +25%. Damage taken +50%
        self.def_trade = 0          # Damage taken -20%. Attack -15%
        self.arm_strength = 0       # Piko Hammer attack +15%
        self.carrot_boost = 0       # Carrot Bomb attack +10% and more SP recover from Carrot Bombs.
        self.weaken = 0             # Reduce enemies' invincibility time after getting hit.
        self.self_defense = 0        # Increase Erina's invincibility time after getting hit.
        self.armored = 0            # Reduce knockback from attacks and reduce collision damage.
        self.lucky_seven = 0         # Deal 107% or 177% damage on every 7th hit.
        self.hex_cancel = 0          # No damage for every 6th hit taken but amulet charge drained for 3 seconds.
        self.pure_love = 0           # In Boss Battles, take almost no collision damage from female enemies.
        self.toxic_strike = 0         # add a poison effect to all attacks.
        self.frame_cancel = 0       # Cancel the fifth Piko Hammer Combo by pressing [down]
        self.health_wager = 0       # Max. MP +37.5. Max. Health -25%.
        self.mana_wager = 0        # Max. Health +17.5. Max. MP -32.5%.
        self.stamina_plus = 0       # Reduce all SP usage by 25%
        self.blessed = 0             # Increase Bunny Amulet recharge speed.
        self.hitbox_down = 0        # Reduce Erina's hitbox size.
        self,cashback = 0           # Increase EN gained from enemies.
        self.survival = 0            # Endure a tatal hit if HP > 1 point.
        self.top_form = 0           # Resist 'Speed Down', 'Attack Down', 'Defense Down', and 'numb' effects.
        self.tough_skin = 0         # Resist 'Toxic', Curse', and 'Burn' effects.
        self.erina_badge = 0        # Dmg. taken -10%. Item Effect +20%. Hold C to extend hammer combo 5.
        self.ribbon_badge = 0       # MP Usage -15%. Hold X after releasing charged shot for repeated shots.
        self.auto_trigger = 0        # Auto use Bunny Amulet if charge is 2 or above, drains all MP and SP.

def badges_check(badges_owner, enemy):
    pass
