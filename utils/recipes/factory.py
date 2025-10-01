from random import randint
from faker import Faker
from faker_food import FoodProvider


fake = Faker("pt_BR")
fake.add_provider(FoodProvider)


def make_recipe():
    return {
        "ingredients": "\n" + "\n".join([fake.ingredient() for _ in range(20)]),
        "id": randint(1, 1000),
        "title": fake.sentence(nb_words=6),
        "description": fake.sentence(nb_words=12),
        "preparation_time": fake.random_number(digits=2, fix_len=True),
        "preparation_time_unit": "Minutos",
        "servings": fake.random_number(digits=2, fix_len=True),
        "servings_unit": "Porção",
        "preparation_steps": fake.text(3000),
        "created_at": fake.date_time(),
        "author": {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
        },
        "category": {"name": fake.word()},
        "cover": {"url": "https://picsum.photos/seed/%s/1280/720/" % randint(1, 1000)},
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(make_recipe())
