from io import StringIO

import sys

from excercises.threating.lock import main


class TestLock:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        Here we are making use of the lock mechanism of the threads, making that only one thread can access to
        the locked resource, in this case we make use of this to change the amount,
        even is this is delayed by the sleep or some other operation.
        With the lock we are able to perform the operation in the right order and with the right quantities.
        100 + 50 + 150 = 0
        """
        assert {
            "starting with balance of 100",
            "deposit thread updating...",
            "deposit thread finishing...",
            "withdrawal thread updating...",
            "withdrawal thread finishing...",
            "ending balance of 0",
        } == output
