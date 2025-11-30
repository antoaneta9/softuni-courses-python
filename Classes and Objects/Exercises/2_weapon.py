class Weapon:

    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
        else:
            return 'no bullets left'
        return 'shooting...'

    def __repr__(self):
        return f'Remaining bullets: {self.bullets}'

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)