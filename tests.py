from main import make_translite


def test__cyrillic_to_latin():
    text = "текст"
    assert make_translite(text) == "tekst"


def test__lower():
    text = "Текст"
    assert make_translite(text) == "tekst"
    assert make_translite(text.upper()) == "tekst"


def test__convert_space_to_snake_case():
    generate_text_with_space = lambda quantity: (" " * quantity).join("текст текст".split(" "))
    for quantity in range(1, 6):
        assert make_translite(generate_text_with_space(quantity)) == "tekst_tekst"


def test__strip():
    text = " текст "
    assert make_translite(text) == "tekst"


def test__single_space():
    text = ""
    assert make_translite(text) == ""


def test__text_with_digits():
    text = "текст1"
    assert make_translite(text) == "tekst1"


def test__text_with_latin():
    text = "текстtext"
    assert make_translite(text) == "teksttext"


def test__text_with_special_signs():
    text = "текст!@#$%^&*()<>?/\|\\"
    assert make_translite(text) == "tekst"


def test__text_with_snake_case():
    text = "текст_текст"
    assert make_translite(text) == "tekst_tekst"
