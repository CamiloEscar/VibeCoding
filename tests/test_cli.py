"""Unit tests for the CLI module."""

from unittest.mock import patch

import pytest

from factorial_calculator.cli import CLI


class TestCLI:
    """Test suite for CLI class."""

    def test_cli_initialization(self) -> None:
        """Test CLI initialization."""
        cli = CLI()
        assert cli.calculator is not None
        assert cli.parser is not None

    def test_argument_mode_valid_input(self) -> None:
        """Test CLI with valid argument input."""
        cli = CLI()
        exit_code = cli.run(["5"])
        assert exit_code == 0

    def test_argument_mode_invalid_input(self) -> None:
        """Test CLI with invalid argument input."""
        cli = CLI()
        exit_code = cli.run(["invalid"])
        assert exit_code == 1

    def test_argument_mode_negative_input(self) -> None:
        """Test CLI with negative argument input."""
        cli = CLI()
        exit_code = cli.run(["-5"])
        assert exit_code == 1

    def test_range_mode_valid(self) -> None:
        """Test CLI range mode with valid inputs."""
        cli = CLI()
        exit_code = cli.run(["--range", "3", "5"])
        assert exit_code == 0

    def test_range_mode_invalid(self) -> None:
        """Test CLI range mode with invalid inputs."""
        cli = CLI()
        exit_code = cli.run(["--range", "-1", "5"])
        assert exit_code == 1

    def test_version_flag(self) -> None:
        """Test CLI version flag."""
        cli = CLI()
        with pytest.raises(SystemExit) as exc_info:
            cli.run(["--version"])
        assert exc_info.value.code == 0

    def test_help_flag(self) -> None:
        """Test CLI help flag."""
        cli = CLI()
        with pytest.raises(SystemExit) as exc_info:
            cli.run(["--help"])
        assert exc_info.value.code == 0

    def test_no_arguments_shows_help(self) -> None:
        """Test CLI with no arguments shows help."""
        cli = CLI()
        exit_code = cli.run([])
        assert exit_code == 0

    @patch("builtins.input", side_effect=["5", "quit"])
    def test_interactive_mode_valid_input(self, mock_input: object) -> None:
        """Test interactive mode with valid input."""
        cli = CLI()
        exit_code = cli.run(["--interactive"])
        assert exit_code == 0

    @patch("builtins.input", side_effect=["invalid", "quit"])
    def test_interactive_mode_invalid_input(self, mock_input: object) -> None:
        """Test interactive mode with invalid input."""
        cli = CLI()
        exit_code = cli.run(["--interactive"])
        assert exit_code == 0

    @patch("builtins.input", side_effect=["exit"])
    def test_interactive_mode_exit_command(self, mock_input: object) -> None:
        """Test interactive mode exit command."""
        cli = CLI()
        exit_code = cli.run(["--interactive"])
        assert exit_code == 0

    @patch("builtins.input", side_effect=["q"])
    def test_interactive_mode_quit_command(self, mock_input: object) -> None:
        """Test interactive mode quit command."""
        cli = CLI()
        exit_code = cli.run(["--interactive"])
        assert exit_code == 0

    @patch("builtins.input", side_effect=["", "5", "quit"])
    def test_interactive_mode_empty_input(self, mock_input: object) -> None:
        """Test interactive mode with empty input."""
        cli = CLI()
        exit_code = cli.run(["--interactive"])
        assert exit_code == 0

    @patch("builtins.input", side_effect=EOFError)
    def test_interactive_mode_eof(self, mock_input: object) -> None:
        """Test interactive mode with EOF."""
        cli = CLI()
        exit_code = cli.run(["--interactive"])
        assert exit_code == 0

    def test_handle_argument_mode_success(self) -> None:
        """Test _handle_argument_mode with successful calculation."""
        cli = CLI()
        exit_code = cli._handle_argument_mode("5")
        assert exit_code == 0

    def test_handle_argument_mode_failure(self) -> None:
        """Test _handle_argument_mode with failed calculation."""
        cli = CLI()
        exit_code = cli._handle_argument_mode("invalid")
        assert exit_code == 1

    def test_handle_range_mode_success(self) -> None:
        """Test _handle_range_mode with successful calculation."""
        cli = CLI()
        exit_code = cli._handle_range_mode("1", "3")
        assert exit_code == 0

    def test_handle_range_mode_failure(self) -> None:
        """Test _handle_range_mode with failed calculation."""
        cli = CLI()
        exit_code = cli._handle_range_mode("invalid", "3")
        assert exit_code == 1

    @patch("builtins.input", side_effect=KeyboardInterrupt)
    def test_keyboard_interrupt_handling(self, mock_input: object) -> None:
        """Test handling of keyboard interrupt."""
        cli = CLI()
        exit_code = cli.run(["--interactive"])
        assert exit_code == 1

    def test_output_format_argument_mode(self, capsys: pytest.CaptureFixture) -> None:
        """Test output format in argument mode."""
        cli = CLI()
        cli.run(["5"])
        captured = capsys.readouterr()
        assert "120" in captured.out
        assert "factorial" in captured.out.lower() or "5" in captured.out

    def test_output_format_range_mode(self, capsys: pytest.CaptureFixture) -> None:
        """Test output format in range mode."""
        cli = CLI()
        cli.run(["--range", "3", "5"])
        captured = capsys.readouterr()
        assert "6" in captured.out  # 3!
        assert "24" in captured.out  # 4!
        assert "120" in captured.out  # 5!

    def test_error_output_to_stderr(self, capsys: pytest.CaptureFixture) -> None:
        """Test that errors are output to stderr."""
        cli = CLI()
        cli.run(["invalid"])
        captured = capsys.readouterr()
        assert len(captured.err) > 0 or "Error" in captured.out


class TestCLIMain:
    """Test suite for main function."""

    def test_main_function_exists(self) -> None:
        """Test that main function exists and is callable."""
        from factorial_calculator.cli import main

        assert callable(main)

    @patch("sys.argv", ["factorial", "5"])
    @patch("sys.exit")
    def test_main_function_execution(self, mock_exit: object) -> None:
        """Test main function execution."""
        from factorial_calculator.cli import main

        main()
        mock_exit.assert_called_once()
