from santas_workshop import Product, Warehouse, ChildrenList, Child
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
