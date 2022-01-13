"""Santa workshop tests."""
from santas_workshop import Product, Warehouse, ChildrenList, Child, Logistics, Carriage
import requests


def test_product_get_name():
    """Product class test."""
    n = Product('Swimming flippers', 25, 3, 1000)
    assert n.get_name() == 'Swimming flippers'


def test_product_get_material_cost():
    """Product class test."""
    n = Product('Swimming flippers', 25, 3, 1000)
    assert n.get_price() == 25


def test_product_get_weight():
    """Product class test."""
    n = Product('Swimming flippers', 25, 3, 1000)
    assert n.get_weight() == 1000


def test_product_get_production_time():
    """Product class test."""
    n = Product('Swimming flippers', 25, 3, 1000)
    assert n.get_production_time() == 3


def test_get_warehouse_api_response_check_status_code_equals_200():
    """Warehouse class test."""
    """Shecks that the HTTP status code equals 200."""
    response = requests.get("http://api.game-scheduler.com:8089/gift?name=swimming%20flippers")
    assert response.status_code == 200


def test_get_warehouse_api_response_check_gift_equals_swimming_flippers():
    """Warehouse class test."""
    response = requests.get("http://api.game-scheduler.com:8089/gift?name=swimming%20flippers")
    response_body = response.json()
    assert response_body["gift"] == "Swimming flippers"


def test_get_warehouse_api_response_check_weight_equals_1000():
    """Check whether api resoponse returns correct weight."""
    response = requests.get("http://api.game-scheduler.com:8089/gift?name=swimming%20flippers")
    response_body = response.json()
    assert response_body["weight_in_grams"] == 1000


def test_get_warehouse_api_response_check_correct_elements_returned():
    """Check for correct dictionary."""
    response = requests.get("http://api.game-scheduler.com:8089/gift?name=swimming%20flippers")
    response_body = response.json()
    assert len(response_body) == 4


def test_get_warehouse_api_response_no_elements_return_none():
    """If such gift not found, return None."""
    w = Warehouse()
    response = requests.get("http://api.game-scheduler.com:8089/gift?name=swimming%20flippers2")
    response_body = response.json()
    assert response_body == {"message": "Gift not found! Did you forget to supply the name "
                                        "of the gift as a query parameter?"}
    assert w.get_product_from_factory('Swimming flippers2') is None


def test_get_warehouse_api_response_return_elements_return_dict():
    """Warehouse class test."""
    w = Warehouse()
    p = w.get_product_from_factory("Swimming flippers")
    assert p in w.get_product("Swimming flippers")
    expected = {"gift": "Swimming flippers", "material_cost": 25, "production_time": 3, "weight_in_grams": 1000}

    assert w.get_product_from_factory("Swimming flippers").get_name() == expected['gift']
    assert w.get_product_from_factory("Swimming flippers").get_price() == expected["material_cost"]


def test_get_product_no_elements_return_none():
    """Warehouse class test."""
    w = Warehouse()
    assert w.get_product("Swimming flippers2") is None


def test_get_children_list_read_children_from_empty_file():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("ex15_wish_list.csv")
    c.read_children_from_file("test_empty_input.csv")
    assert len(c.get_children_list()) == 0


def test_get_children_list_read_file_one_nice_child():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("ex15_wish_list.csv")
    c.read_children_from_file("test_one_nice.csv")
    assert len(c.get_children_list()) == 1
    assert c.get_children_list()[0].name == "Aiden"
    assert c.get_children_list()[0].country == 'Canada'


def test_get_children_list_read_file_one_naughty_child():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("ex15_wish_list.csv")
    c.read_children_from_file("test_one_naughty.csv")
    assert len(c.get_children_list()) == 1
    assert c.get_children_list()[0].name == "Gregory"
    assert c.get_children_list()[0].country == 'Canada'


def test_get_children_list_read_file_two_children_have_same_name():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("ex15_wish_list.csv")
    c.read_children_from_file("test_two_same_name.csv")
    assert len(c.get_children_list()) == 2
    assert c.get_children_list()[0].name == "Libby"
    assert c.get_children_list()[1].name == "Libby"


def test_get_children_list_read_file_nice_children():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("ex15_wish_list.csv")
    c.read_children_from_file("ex15_nice_list.csv")
    result = [i.name for i in c.get_children_list()]
    assert len(c.get_children_list()) == 291
    expected = ['Libby', 'Keira', 'Lexie', 'Amelia', 'Evelyn', 'Carissa', 'Marisol', 'Dylan', 'Ben', 'Cain', 'Darius',
                'Edward', 'Freddie', 'Jenson', 'Armando', 'Jakob', 'Alvin', 'Peter', 'Louis', 'Spencer', 'Mason',
                'Rhys', 'Reid', 'Caden', 'Quinn', 'Lesley', 'Kai', 'Jess', 'Jaden', 'Ash', 'Skyler', 'Jordan', 'Aubrey',
                'Alexis', 'Eleanor', 'Scarlett', 'Rachael', 'Lorelei', 'Phoebe', 'Ariel', 'Kimberly', 'Chloe', 'Sofie',
                'Jodie', 'Hollie', 'Baylee', 'Brennan', 'Harper', 'Lance', 'Scott', 'Ollie', 'Marc', 'Otto', 'Mark',
                'Denzel', 'Toby', 'Tobias', 'Elliot', 'Ellis', 'Sean', 'Dominik', 'Gunnar', 'Darryl', 'Josh', 'Jackson',
                'Dayton', 'Evan', 'Levi', 'Harvey', 'Ewan', 'Drew', 'Rylan', 'Shane', 'Josiah', 'Max', 'Dillion',
                'Albert', 'Nathan', 'Nathaniel', 'Joaquin', 'Declan', 'Benton', 'Stan', 'Steve', 'Lewis', 'Javier',
                'Roy', 'Nicholas', 'Simeon', 'Milo', 'Calvin', 'James', 'Jon', 'Ernest', 'Patrick', 'Logan', 'Atticus',
                'Luke', 'Rodney', 'Lucas', 'Vaughn', 'Marcel', 'Victor', 'Noah', 'Jimmy', 'Gail', 'Frankie', 'Bella',
                'Polly', 'Nora', 'Lacey', 'Georgina', 'Addison', 'Natalie', 'Adeline', 'Ariana', 'Astrid', 'Charlotte',
                'Paisley', 'Brooklyn', 'Angel', 'Gabbie', 'Angelika', 'Nadia', 'Hazel', 'Francesca', 'Arya', 'Caitlin',
                'Myra', 'Eden', 'Dolly', 'Eliza', 'Josie', 'Ivy', 'Georgia', 'Ariella', 'Arianna', 'Meredith',
                'Abigail', 'Miriam', 'Holly', 'Annie', 'Matteo', 'Olly', 'Kian', 'Zack', 'Arlo', 'Archer', 'Parker',
                'Fabian', 'Montgomery', 'Kevin', 'Jesse', 'Tate', 'Luis', 'Travis', 'Carl', 'Fletcher', 'Eddie',
                'Lenno', 'Sidney', 'Dennis', 'Jensen', 'Sam', 'Oscar', 'Perry', 'Ted', 'Ralph', 'Fraser', 'Neil',
                'Herman', 'Russell', 'Wayne', 'Wyatt', 'Hector', 'Miles', 'Zach', 'Damian', 'Isaac', 'Tristan', 'Hans',
                'Curtis', 'Hugo', 'Casey', 'Kylie', 'Nicole', 'Ada', 'Adele', 'Agnes', 'ALbert', 'Allen', 'Mario',
                'Brian', 'Tiffany', 'Veronica', 'Jodi', 'Vivian', 'Sara', 'Connie', 'Ella', 'Leo', 'Philip', 'Craig',
                'Brendan', 'Jeff', 'Shaun', 'Orville', 'Kent', 'Derek', 'Donald', 'Earl', 'Leon', 'Roger', 'Seth',
                'Stella', 'Loretta', 'Laura', 'Michelle', 'Gina', 'Selena', 'Alice', 'Beverly', 'Dolores', 'Stefanie',
                'Yvonne', 'Irma', 'Mariah', 'Maureen', 'Denise', 'Howard', 'Karl', 'Martin', 'Sebastian', 'Kilian',
                'Eugene', 'Estelle', 'Arnold', 'Arthur', 'Gerald', 'Margarita', 'Franz', 'Marcus', 'Marvin', 'Mathias',
                'Niko', 'Naomi', 'Paula', 'Raphael', 'Rupert', 'Sabrina', 'Ruth', 'Sven', 'Tim', 'Timothy', 'Gilbert',
                'Gustav', 'Klaus', 'Lars', 'Dirk', 'Emilia', 'Emma', 'Eva', 'Gwen', 'Ramona', 'Casper', 'Kayleigh',
                'Fern', 'Daisy', 'Maria', 'Mimi', 'Tessa', 'Esther', 'Martha', 'Jasmin', 'Ida', 'Leonie', 'Zoe',
                'Courtney', 'Matilda', 'Stephanie', 'Dale', 'Elle', 'Leia', 'Carley', 'Sophie', 'Gabrielle', 'Alexa',
                'Mariam', 'Catherine', 'Anya', 'Stacy']
    assert len(result) == len(expected)
    assert result == expected


def test_get_nice_children():
    """ChildrenList class test."""
    c = ChildrenList()
    ago = Child('Ago', 'Estonia', ['Playstation'])
    mati = Child('Mati', 'Latvia', ['Guitar', 'Bowling table'])
    kati = Child('Kati', 'Poland', ['Car', 'Swimming flippers'])
    children = [ago, mati, kati]
    c.add_nice_children(children)
    assert len(c.get_nice_children()) == 3
    assert c.get_nice_children() == [ago, mati, kati]


def test_get_naughty_children():
    """ChildrenList class test."""
    c = ChildrenList()
    jaanus = Child('Jaanus', 'Estonia', ['Playstation'])
    mikk = Child('Mikk', 'Estonia', ['Guitar', 'Bowling table'])
    charlie = Child('Charlie', 'USA', ['Car', 'Swimming flippers'])
    children = [jaanus, mikk, charlie]
    c.add_nice_children(children)
    assert len(c.get_nice_children()) == 3
    assert c.get_nice_children() == [jaanus, mikk, charlie]


def test_get_children_wishes_empty_file():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("test_empty_input.csv")
    assert len(c.get_wishes()) == 0


def test_get_child_has_more_than_five_wishes_take_only_five():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("test_more_than_five_wishes_per_child.csv")
    assert len(c.get_wishes()['Ago']) == 5
    assert c.get_wishes()['Ago'] == ['game1', 'game2', 'game3', 'game4', 'game5']


def test_get_children_wishes_one_line():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("test_one_wish.csv")
    assert len(c.get_wishes()) == 1
    for i in c.get_wishes():
        assert i == "Cain"
        assert c.get_wishes()[i] == ["VHS player", "Harry Potter and the Philosopher's Stone"]


def test_get_children_wishes_bigger_one():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("test_few_wishes.csv")
    assert len(c.get_wishes()) == 8
    expected = {'Libby': ['Zebra Jumpy', 'Princess dress', 'Lego death star'],
                'Keira': ['LED light up sneakers', '7200 Riot Points gift card'],
                'Lexie': ['Mermaid barbie', 'Pink fluffy pen', 'World of Warcraft: Shadowlands Collectors Edition'],
                'Amelia': ['Wall-mount diamond pickaxe', 'Magic: The Gathering Commander Legends booster box'],
                'Evelyn': ['Wall-mount diamond pickaxe', '7200 Riot Points gift card', 'Avocado'],
                'Carissa': ['Baby Yoda plushie', 'Nintendo Switch', 'Football shoes'],
                'Marisol': ['Magic: The Gathering Commander Legends booster box'],
                'Dylan': ['Roller skates', 'Cyberpunk 2077']}
    result = c.get_wishes()
    assert expected == result
    assert len(expected['Libby']) == 3
    assert expected['Libby'] == ['Zebra Jumpy', 'Princess dress', 'Lego death star']
    assert 'Roller skates' in expected['Dylan']
    assert 'Cyberpunk 2077' in expected['Dylan']


def test_get_children_dict():
    """ChildrenList class test."""
    c = ChildrenList()
    c.read_wishes_from_file("ex15_wish_list.csv")
    c.read_children_from_file("test_few_nice.csv")
    # Libby = Child('Libby', 'United Kingdom', ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    # Keira = Child('Keira', 'Germany', ['LED light up sneakers', '7200 Riot Points gift card'])
    # Lexie = Child('Lexie', 'Canada', ['Mermaid barbie', 'Pink fluffy pen', 'World of Warcraft: Shadowlands Collectors Edition'])
    # result = {'Libby': Libby, 'Keira': Keira, 'Lexie': Lexie}
    assert len(c.get_children_dict()) == 3
    # assert c.get_children_dict() == result


def test_child():
    """Child class test."""
    c = Child("Ago", "Tallinn", ['Monopoly', 'Puzzle'])
    assert c.name == "Ago"
    assert c.country == "Tallinn"
    assert len(c.wishlist) == 2
    assert c.get_wishes() == ['Monopoly', 'Puzzle']


# Part two (test Logistics)

def test_get_children():
    """Logistics class test."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    lexie = Child("Lexie", "Canada",
                  ['Mermaid barbie', 'Pink fluffy pen', 'World of Warcraft: Shadowlands Collectors Edition'])
    amelia = Child("Amelia", "South Africa",
                   ['Wall-mount diamond pickaxe', 'Magic: The Gathering Commander Legends booster box'])
    evelyn = Child("Evelyn", "Puerto Rico", ['Wall-mount diamond pickaxe', '7200 Riot Points gift card', 'Avocado'])
    c = [libby, keira, lexie, amelia, evelyn]
    logistic = Logistics(c)

    assert len(logistic.get_children()) == 5
    assert logistic.get_children() == c


def test_children_from_countries_to_deliver():
    """Logistic class test."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    evelyn = Child("Evelyn", "Puerto Rico", ['Wall-mount diamond pickaxe', '7200 Riot Points gift card', 'Avocado'])
    c = [libby, keira, evelyn]
    logistic = Logistics(c)

    logistic.children_from_countries_to_deliver()
    ret = logistic.get_children_from_countries_to_deliver()
    assert len(ret) == 3
    assert "United Kingdom" in ret and "Germany" in ret and "Puerto Rico" in ret
    assert libby in ret["United Kingdom"]
    assert keira in ret["Germany"]
    assert evelyn in ret["Puerto Rico"]


def test_import_products_from_warehouse():
    """Logistic class test."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])

    c = [libby]

    logistic = Logistics(c)

    # zebra_jumpy = Product("Zebra Jumpy", 25, 1, 1337)
    # princess_dress = Product("Princess dress", 17, 5, 278)
    # lego_death_star = Product("Lego death star", 599, 30, 2000)
    # expected = {'Zebra Jumpy': zebra_jumpy, 'Princess dress': princess_dress, 'Lego death star': lego_death_star}
    assert len(logistic.get_products()) == 0
    logistic.import_products_from_warehouse()
    ret = logistic.get_products()
    assert len(ret) == 3
    assert isinstance(ret["Zebra Jumpy"], Product)
    assert isinstance(ret["Princess dress"], Product)
    assert isinstance(ret["Lego death star"], Product)

    assert ret["Zebra Jumpy"].name == "Zebra Jumpy"
    assert ret["Princess dress"].name == "Princess dress"
    assert ret["Lego death star"].name == "Lego death star"

    assert ret["Zebra Jumpy"].price == 25
    assert ret["Princess dress"].price == 17
    assert ret["Lego death star"].price == 599

    assert ret["Zebra Jumpy"].production_time == 1
    assert ret["Princess dress"].production_time == 5
    assert ret["Lego death star"].production_time == 30

    assert ret["Zebra Jumpy"].weight == 1337
    assert ret["Princess dress"].weight == 278
    assert ret["Lego death star"].weight == 2000

    c.append(keira)
    logistic.import_products_from_warehouse()

    assert len(logistic.get_products()) == 5


def test_country_of_origin():
    """Logistic class test."""
    """Test childrens country of origin, if there is a country but no children from such country,then
    the function must return empty list."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    evelyn = Child("Evelyn", "Puerto Rico", ['Wall-mount diamond pickaxe', '7200 Riot Points gift card', 'Avocado'])

    jaden = Child("Jaden", "Germany", ['Dungeons and Dragons 5th Edition Starter Set',
                                       'New phone', 'Ninja Turtles backpack'])
    c = [libby, keira, evelyn]
    logistic = Logistics(c)

    assert logistic.country_of_origin("United Kingdom") == [libby]
    assert logistic.country_of_origin("Germany") == [keira]
    assert logistic.country_of_origin("Puerto Rico") == [evelyn]

    assert logistic.country_of_origin("Estonia") == []

    c.append(jaden)
    assert logistic.country_of_origin("Germany") == [keira, jaden]


def test_get_products_total_volume():
    """Logistic class test."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    c = [libby, keira]
    logistic = Logistics(c)
    assert logistic.get_products_total_volume() == 0
    result = 1337 + 278 + 2000 + 250 + 10
    logistic.import_products_from_warehouse()
    assert logistic.get_products_total_volume() == result


def test_products_total_volume_per_child():
    """Logistic class test."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    jaden = Child("Jaden", "Germany", ['Dungeons and Dragons 5th Edition Starter Set',
                                       'New phone', 'Ninja Turtles backpack'])
    c = [libby, keira, jaden]
    logistic = Logistics(c)
    logistic.children_from_countries_to_deliver()
    logistic.import_products_from_warehouse()

    keira_result = sum([250, 10])
    jaden_result = sum([1000, 200, 350])
    libby_result = sum([1337, 278, 2000])
    assert len(logistic.products_total_volume_per_child("Germany")) == 2
    assert logistic.products_total_volume_per_child("Germany")[keira] == keira_result
    assert logistic.products_total_volume_per_child("Germany")[jaden] == jaden_result
    assert logistic.products_total_volume_per_child("United Kingdom")[libby] == libby_result


def test_products_total_volume_per_child_return_none():
    """Logistic class test."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    c = [libby, keira]
    logistic = Logistics(c)
    assert logistic.products_total_volume_per_child("Estonia") is None


def test_amount_of_carriages_needed_to_carry_products_to_country():
    """Logistic class test."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    c = [libby, keira]
    logistic = Logistics(c)
    logistic.import_products_from_warehouse()
    logistic.children_from_countries_to_deliver()
    logistic.products_total_volume_per_child("Germany")
    assert logistic.amount_of_carriages_needed_to_carry_products_to_country("Germany") == 1


def test_amount_of_carriages_needed_to_carry_products_to_country_returns_zero_if_country_not_exist():
    """Logistic class test."""
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    c = [libby, keira]
    logistic = Logistics(c)
    logistic.children_from_countries_to_deliver()
    assert logistic.amount_of_carriages_needed_to_carry_products_to_country("Estonia") == 0


def test_pack_carriages_to_country():
    """Logistic class test."""
    keira = Child("Keira", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    lexie = Child("Lexie", "Canada",
                  ['Mermaid barbie', 'Pink fluffy pen', 'World of Warcraft: Shadowlands Collectors Edition'])
    amelia = Child("Amelia", "South Africa",
                   ['Wall-mount diamond pickaxe', 'Magic: The Gathering Commander Legends booster box'])
    evelyn = Child("Evelyn", "Puerto Rico", ['Wall-mount diamond pickaxe', '7200 Riot Points gift card', 'Avocado'])
    libby = Child("Libby", "United Kingdom", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    c = [keira, lexie, amelia, evelyn, libby]
    logistic = Logistics(c)
    logistic.import_products_from_warehouse()
    logistic.children_from_countries_to_deliver()
    logistic.pack_carriages_to_country("Germany")
    assert len(logistic.get_packed_carriages_to_countries()) == 1
    assert len(logistic.get_packed_carriages_to_countries()["Germany"]) == 1
    for c in logistic.get_packed_carriages_to_countries():
        ret = logistic.get_packed_carriages_to_countries()[c][0]
        assert ret.country == "Germany"
        assert keira in ret.products
        assert ret.products[keira] == ['LED light up sneakers', '7200 Riot Points gift card']


def test_pack_carriages_to_country_more_carriages():
    """Logistic class test."""
    keira = Child("Keira", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    lexie = Child("Lexie", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    amelia = Child("Amelia", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    evelyn = Child("Evelyn", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    libby = Child("Libby", "Germany", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    caden = Child("Caden", "Germany", ['New phone', "Lego death star", 'Car carpet'])
    quinn = Child("Quinn", "Germany",
                  ["Small watering can", 'Wall-mount diamond pickaxe', "Lego death star", 'Avocado'])
    lesley = Child("Lesley", "Germany", ["Zebra Jumpy", 'Wall-mount diamond pickaxe', "Lego death star", 'Avocado'])
    kai = Child("Kai", "Germany", ["Small watering can", 'LED light up sneakers', "Lego death star"])
    jess = Child("Jess", "Germany", ["Carbon fiber road bike", 'LED light up sneakers', "Lego death star"])
    ash = Child("Ash", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    skyler = Child("Skyler", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    jordan = Child("Jordan", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    aubrey = Child("Aubrey", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    rico = Child("Rico", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    alexis = Child("Alexis", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    eleanor = Child("Eleanor", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])

    c = [keira, lexie, amelia, evelyn, libby, caden, quinn, lesley, kai, jess, ash, skyler, jordan, aubrey, rico,
         alexis, eleanor]
    logistic = Logistics(c)
    logistic.import_products_from_warehouse()
    logistic.children_from_countries_to_deliver()
    logistic.pack_carriages_to_country("Germany")
    assert len(logistic.get_packed_carriages_to_countries()["Germany"]) == 4


def test_pack_all_carriages_to_countries():
    """Logistic class test."""
    alexis = Child("Alexis", "Germany", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    eleanor = Child("Eleanor", "Estonia", ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"])
    c = [alexis, eleanor]
    logistic = Logistics(c)
    logistic.import_products_from_warehouse()
    logistic.children_from_countries_to_deliver()
    logistic.pack_all_carriages_to_countries()

    assert len(logistic.get_packed_carriages_to_countries()) == 2
    assert "Germany" in logistic.get_packed_carriages_to_countries()
    assert "Estonia" in logistic.get_packed_carriages_to_countries()
    assert logistic.get_packed_carriages_to_countries()["Germany"][0].country == "Germany"
    assert logistic.get_packed_carriages_to_countries()["Estonia"][0].country == "Estonia"
    assert logistic.get_packed_carriages_to_countries()["Germany"][0].products[alexis] == \
           ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"]
    assert logistic.get_packed_carriages_to_countries()["Estonia"][0].products[eleanor] == \
           ["Carbon fiber road bike", 'Zebra Jumpy', "Lego death star"]


def test_delivery_notes_for_carriage_per_country():
    """Logistic class test. Write into file."""
    libby = Child("Libby", 'Germany', ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", 'Germany', ['LED light up sneakers', '7200 Riot Points gift card'])
    lexie = Child("Lexie", 'Estonia',
                  ['Mermaid barbie', 'Pink fluffy pen', 'World of Warcraft: Shadowlands Collectors Edition'])

    amelia = Child("Amelia", 'Germany', ['Zebra Jumpy', 'Princess dress', 'Lego death star', 'LED light up sneakers',
                                         '7200 Riot Points gift card'])

    c = [libby, keira, lexie, amelia]
    logistic = Logistics(c)
    logistic.import_products_from_warehouse()
    logistic.children_from_countries_to_deliver()
    logistic.pack_all_carriages_to_countries()
    logistic.delivery_notes_for_carriage_per_country("Germany", "result.txt")
    with open('expected_output_one_country.txt', 'r') as file1, open('result.txt', 'r') as file2:
        assert file1.read() == file2.read()


# def test_write_delivery_notes_for_carriage_all_nice_children():
#     """Logistic class test. Write into file. Test all nice children."""
#     c = ChildrenList()
#     c.read_wishes_from_file("ex15_wish_list.csv")
#     c.read_children_from_file("ex15_nice_list.csv")
#     l = Logistics(c.get_children_list())
#     l.import_products_from_warehouse()
#     l.children_from_countries_to_deliver()
#     l.pack_all_carriages_to_countries()
#     l.delivery_notes_for_carriage_all("result.txt")
#     with open('expected_output_all_nice_children.txt', 'r') as file1, open('result.txt', 'r') as file2:
#         assert file1.read() == file2.read()
#

def test_write_delivery_notes_for_carriage_empty():
    """Logistic class test. Write into file."""
    c = []
    logistic = Logistics(c)
    logistic.import_products_from_warehouse()
    logistic.children_from_countries_to_deliver()
    logistic.pack_all_carriages_to_countries()
    logistic.delivery_notes_for_carriage_all("result.txt")
    with open('expected_output_empty.txt', 'r') as file1, open('result.txt', 'r') as file2:
        assert file1.read() == file2.read()


def test_carriage_delivery_note_empty():
    """Carriage class test."""
    c = Carriage("Germany", {}, {})
    assert c.delivery_note() == ''


def test_carriage_delivery_note_some_input():
    """Carriage class test."""
    some1 = Child("some1", "Germany", ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    some2 = Child("some2", "Germany", ['LED light up sneakers', '7200 Riot Points gift card'])
    c = Carriage("Germany", {some1: ['Zebra Jumpy', 'Princess dress', 'Lego death star'],
                             some2: ['LED light up sneakers', '7200 Riot Points gift card']}, {some1: 3615, some2: 260})

    expected = r"""                        DELIVERY ORDER
                                                          _v
                                                     __* (__)
             ff     ff     ff     ff                {\/ (_(__).-.
      ff    <_\__, <_\__, <_\__, <_\__,      __,~~.(`>|-(___)/ ,_)
    o<_\__,  (_ ff ~(_ ff ~(_ ff ~(_ ff~~~~~@ )\/_;-"``     |
      (___)~~//<_\__, <_\__, <_\__, <_\__,    | \__________/|
      // >>     (___)~~(___)~~(___)~~(___)~~~~\\_/_______\_//
                // >>  // >>  // >>  // >>     `'---------'`

FROM: NORTH POLE CHRISTMAS CHEER INCORPORATED
TO: /GERMANY/

//=======[]===================================================[]==================\\
|| Name  ||                       Gifts                       || Total Weight(kg) ||
|]=======[]===================================================[]==================[|
|| some1 || Zebra Jumpy, Princess dress, Lego death star      || 3.615            ||
|| some2 || LED light up sneakers, 7200 Riot Points gift card || 0.26             ||
\\=======[]===================================================[]==================//"""
    assert c.delivery_note() == expected
