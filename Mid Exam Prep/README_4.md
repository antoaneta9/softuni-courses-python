# Galactic Market Tycoon

Управляваш космически търговски хъб. Поддържаш баланс, репутация, технологично ниво, ресурси и флот. Обработвай команди, докато не бъде получена командата **`Shutdown`**.

## Начално състояние (вход)
1) `balance` — реално число  
2) `reputation` — цяло число  
3) `technology_level` — цяло число

Всички ресурси започват от 0. Начално няма кораби.

## Ресурси
Допустими типове: `ore`, `food`, `fuel`, `crystals`.

## Кораби
Всеки кораб има: `name`, `crew` (цяло), `capacity` (цяло), `fuel_usage` (цяло).

---

## Команди

Всяка команда е на отделен ред. Четенето приключва при **`Shutdown`**.

### 1) `BuyResource {type} {quantity} {price_per_unit}`
- Ако `type` ∉ {`ore`,`food`,`fuel`,`crystals`} → игнорирай.
- Ако `balance < quantity * price_per_unit` → отпечатай:  
  `Insufficient funds!`
- Иначе: намали `balance` със стойността и увеличи ресурса.

### 2) `SellResource {type} {quantity} {price_per_unit}`
- Ако `type` ∉ {`ore`,`food`,`fuel`,`crystals`} → игнорирай.
- Ако наличното количество на `type` е по-малко от `quantity` → отпечатай:  
  `Not enough {type}!`
- Иначе: намали ресурса и увеличи `balance`.

### 3) `HireShip {name} {crew} {capacity} {fuel_usage}`
- Цена за наемане: `crew * 100`.
- Ако `balance` е по-малък от цената → отпечатай:  
  `Cannot afford ship!`
- Иначе: намали `balance`, добави кораба към флота.

### 4) `FireShip {name}`
- Ако кораб с това име съществува → премахни и отпечатай:  
  `{name} has been dismissed.`
- Иначе отпечатай:  
  `{name} not found!`

### 5) `Mission {name} {mission_type}`
`mission_type` ∈ {`mining`, `trading`, `exploration`}.  
- Ако кораб с име `{name}` не съществува → отпечатай:  
  `Ship not found!`  
  (Командата приключва.)

Използва се ресурсът `fuel`. Отнемането на гориво става преди резултатите. Ако липсва достатъчно `fuel`, отпечатай **само** съответното съобщение за липса и не променяй нищо друго.

- **mining**
  - Изисква `fuel_needed = fuel_usage * 10`.
  - Ако `fuel < fuel_needed` → `Not enough fuel!`
  - Иначе: намали `fuel` с `fuel_needed`, увеличи `ore` с `R`, където `R` е цяло число в диапазона **[20..50]**, увеличи `reputation` с **1**, отпечатай:  
    `Mining mission successful!`

- **trading**
  - Изисква `fuel_needed = fuel_usage * 5`.
  - Ако `fuel < fuel_needed` → `Not enough fuel!`
  - Иначе: намали `fuel`; ако `food >= 10`, продай 10 `food` за цена `P` (реално число в диапазона **[20..50]**), увеличи `balance` с `P`, увеличи `reputation` с **2**. Отпечатай:  
    `Trading mission completed!`  
    (Ако `food < 10`, пак се счита за успешно изпълнена търговска мисия, но без промяна в `food` и приходи; `reputation` пак се увеличава с 2.)

- **exploration**
  - Изисква `fuel_needed = fuel_usage * 15`.
  - Ако `fuel < fuel_needed` → `Not enough fuel!`
  - Иначе: намали `fuel`. С вероятност **50%** → успех: увеличи `crystals` с `C`, където `C` е цяло число в **[5..15]**, увеличи `reputation` с **5**, отпечатай:  
    `Exploration result: success`
    Иначе → провал: корабът се губи (премахни от флота), намали `reputation` с **10**, отпечатай:  
    `Exploration result: failure`

### 6) `Research {points}`
- Цена: `points * 200`.
- Ако `balance` е по-малък от цената → отпечатай:  
  `Not enough money for research!`
- Иначе: намали `balance` с цената, увеличи `technology_level` с `points`.  
  Ако `technology_level >= 50` след операцията → увеличи `reputation` с **20**.

### 7) `PayCrew`
- `total_cost = Σ(crew * 50)` за всички кораби.
- Ако `balance >= total_cost` → намали `balance` с `total_cost`, увеличи `reputation` с броя кораби, отпечатай:  
  `Crew has been paid.`
- Иначе: намали `reputation` с **10**, отпечатай:  
  `Could not pay crew!`

### 8) `Tax`
- Данък = `balance * 0.10`. Намали `balance` с данъка. Намали `reputation` с **5**.

### 9) `Status`
Отпечатай точно в следния формат:
Balance: {balance}
Reputation: {reputation}
Technology: {technology_level}
Resources: ore={ore}, food={food}, fuel={fuel}, crystals={crystals}
Ships:

Name | Crew | Capacity | FuelUsage

{за всеки кораб по ред на добавяне}

Ако няма кораби, вместо списъка с редове отпечатай:
Ships: None

yaml
Copy code

### 10) `Shutdown`
- Прекратява входа.

---

## Поведение след `Shutdown`

Ако `reputation < 0`:
You have been blacklisted! Game Over.

makefile
Copy code

Иначе:
Hub Status:
Balance: {balance}
Reputation: {reputation}
Technology: {technology_level}
Resources: ore={ore}, food={food}, fuel={fuel}, crystals={crystals}
Ships count: {брой_кораби}

markdown
Copy code

---

## Ограничения и форматиране

- Нито един ресурс не може да става отрицателен.
- Всички парични суми при отпечатване се показват с **точност до 2 знака след десетичната запетая**.
- Командите се обработват в реда, в който са получени.
- За случайните стойности, когато са необходими, се използва равномерно разпределение в зададените граници.
- При `Mission` горивото винаги се приспада преди резултата.
- При провал на `exploration` корабът се премахва окончателно.