"""test_app.py"""

from streamlit.testing.v1 import AppTest

at = AppTest.from_file("app.py").run()


def test_increment_and_add():
    """A user increments the number input, then clicks Add"""
    at.number_input[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Beans counted: 1"


def test_button_order():
    """The buttons are in the correct order"""
    assert at.button[1].label == "B"
    assert at.button[2].label == "A"


def test_get_button_by_key():
    assert at.button(key="submit").label == "Next"
    assert at.button("cancel").label == "Back"


def test_selection_box():
    assert at.selectbox[0].value == None
    assert at.selectbox[0].label == "A"
    assert at.selectbox[0].options == ["1", "2", "3"]
    assert at.selectbox[0].index == None
    assert at.selectbox[0].help == "Pick a number"
    assert at.selectbox[0].placeholder == "Pick me"
    assert at.selectbox[0].disabled == False
