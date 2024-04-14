from io import StringIO

import sys

from excercises.threating.barrier import main


class TestBarrier:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        In this case we wait until the people are older than 18 to vote, if the person in lower than that age
        we need to wait one more year to check it, when is fulfilled we break the barrier and allow them to vote.

        To make possible to test this code, we added the `join` to each thread, since we need to wait to all tests
        finish to check the output
        """
        assert {
            "ari (age 15) is getting older",
            "derrick (age 12) is getting older",
            "ari (age 16) is getting older",
            "derrick (age 13) is getting older",
            "derrick (age 14) is getting older",
            "ari (age 17) is getting older",
            "derrick (age 15) is getting older",
            "derrick (age 16) is getting older",
            "derrick (age 17) is getting older",
            "derrick can vote!",
            "charles can vote!",
            "ari can vote!",
        } == output
