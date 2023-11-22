#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def setUp(cls):
        """Set up resources"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """Clean up resources"""
        del cls.consol

    def tearDown(self):
        """Remove file.json"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Checks console.py against the PEP 8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, "PEP 8 style violations")

    def test_docstrings_in_console(self):
        """Checks for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test empty line input"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test the 'quit' command."""
        with patch("sys.stdout", new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                self.consol.onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_create(self):
        """Test create command inpout"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create SomtingElse")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd(
                "create User email='belboukayyoub@gmail.com' " "password='person'"
            )
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual('["[User]', f.getvalue()[:8])


if __name__ == "__main__":
    unittest.main()
