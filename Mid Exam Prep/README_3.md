# Dungeon Quest Manager

Играч влиза в подземие с начално здраве и енергия. След това въвежда команди, докато не въведе `"Exit"` или докато играта не приключи по друг начин.

## Вход:
- Първи ред: начално здраве (health)
- Втори ред: начална енергия (energy)
- След това: поредица от команди до `"Exit"`

## Видове команди:

### monster {name} {damage} {energy_cost}
- Ако играчът има достатъчно енергия: изразходва energy_cost и получава damage на здравето.
  - Ако damage >= текущото здраве → `{name} defeated you!` и играта приключва.
  - Иначе → `You slayed {name}!`
- Ако няма достатъчно енергия:
  - `Not enough energy to fight {name}!`
  - Продължава към следващата команда, без да губи здраве.

### potion {amount}
Увеличава здравето с amount (максимум до 100).
- `You healed for {реално_получени_точки} hp.`
- `Current health: {health} hp.`

### chest {gold}
Увеличава събраното злато.
- `You found {gold} gold.`

### trap {damage} {energy_loss}
Играчът губи damage от здравето и energy_loss от енергията.
- Ако здравето <= 0 → `You died to a trap!` и играта приключва.
- Ако енергията <= 0 → `You are too exhausted!` и играта приключва.
- Иначе → `You survived the trap.`

### rest {energy_gain}
Увеличава енергията с energy_gain (максимум до 100).
- `You rested and gained {реално_получена_енергия} energy.`
- `Current energy: {energy}.`

### boss {name} {health_needed} {energy_needed}
- Ако текущо здраве >= health_needed и енергия >= energy_needed:
  - `You defeated the boss {name}!`
  - Играта приключва с победа.
- Иначе:
  - `You were not prepared for {name}...`
  - Играта приключва с провал.

**Командата boss винаги приключва играта.**

---

## Изход (в зависимост от случая):

### Ако играчът умре (чудовище или капан):
- Само съответното съобщение за смърт.

### Ако е победен boss:
- Съобщението от boss.
- `Total gold collected: {total_gold}`

### Ако потребителят въведе `"Exit"` и играта още не е приключила:
- `You left the dungeon.`
- `Health: {health}`
- `Energy: {energy}`
- `Gold: {total_gold}`

---

## Допълнителни условия:
- Здравето и енергията са винаги в граници [0, 100].
- При `potion` и `rest` не може да се надвишават 100.
- Изпълнението приключва веднага при смърт или boss.
- Златото се събира само от chest.

