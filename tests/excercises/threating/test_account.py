from io import StringIO

import sys

from excercises.threating.account import main


class TestAccount:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        Here we have the problem that since we have an sleep for one second (simulating a database operation),
        we found that when the first operation (deposit) is gonna make the changes, the second one (withdrawal)
        is gonna make the changes for the original quantity (100) and not the expected one (150)
        """
        assert {
            "starting with balance of 100",
            "deposit thread updating...",
            "deposit thread finishing...",
            "withdrawal thread updating...",
            "withdrawal thread finishing...",
            "ending balance of -50",
        } == output
