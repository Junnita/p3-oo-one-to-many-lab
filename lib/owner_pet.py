class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner="None"):
        self.name = name
        self.owner = owner
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Pet type is invalid")
        Pet.add_pet(self)

    @classmethod
    def add_pet(cls, pet):
        cls.all.append(pet)


class Owner:
    pass

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        pass
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Pet type is invalid")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)