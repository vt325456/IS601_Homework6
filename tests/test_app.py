"""
Test module for the REPL functionality of the App class.
"""
import pytest
from app import App
from app.plugins.menu import MenuCommand
from app.plugins.exit import ExitCommand

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_menu_command_execute(capfd):
    """Test the menu command in plugins"""
    menu_command = MenuCommand()
    menu_command.execute()
    captured = capfd.readouterr()
    assert "Calculator Program : Enter the command to perform operation" in captured.out


def test_exit_command_execute():
    """Test the exit command in plugins"""
    exit_command = ExitCommand()
    with pytest.raises(SystemExit) as e:
        exit_command.execute()
    assert str(e.value) == "Exiting..."
    