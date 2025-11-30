class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        animals = ''
        if species == "mammal":
            animals += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"

        elif species == "fish":
            animals += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"

        elif species == "bird":
            animals += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        animals+= f"Total animals: {Zoo.__animals}"
        return animals

zoo_name = Zoo(input())
lines = int(input())

for _ in range(lines):
    animal = input().split(' ')
    species = animal[0]
    name = animal[1]

    zoo_name.add_animal(species, name)

species_to_print = input()
print(zoo_name.get_info(species_to_print))
