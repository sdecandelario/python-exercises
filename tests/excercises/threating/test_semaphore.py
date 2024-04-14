from io import StringIO

import sys

from excercises.threating.semaphore import main


class TestSemaphore:

    def test_output(self):
        """
        TODO need to find a way to proper implement the test
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        TODO
        """
        assert {
            "starting with balance of 100",
            "deposit thread updating...",
            "deposit thread finishing...",
            "withdrawal thread updating...",
            "withdrawal thread finishing...",
            "ending balance of -50",
        } == output
