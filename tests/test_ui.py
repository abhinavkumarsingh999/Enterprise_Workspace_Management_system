import pytest

from src.ui.menu import Menu


def test_menu_object_creation():
    menu = Menu()

    assert menu is not None


def test_header(capsys):
    Menu.header()

    captured = capsys.readouterr()

    assert "ENTERPRISE WORKSPACE MANAGEMENT SYSTEM" in captured.out


def test_invalid_choice(capsys):
    Menu.invalid_choice()

    captured = capsys.readouterr()

    assert "Invalid choice" in captured.out


def test_clear(capsys):
    Menu.clear()

    captured = capsys.readouterr()

    assert captured.out.count("\n") >= 3


def test_press_enter(monkeypatch):

    monkeypatch.setattr(
        "builtins.input",
        lambda _: ""
    )

    Menu.press_enter()