import sys
from io import StringIO

from excercises.threating.join import main


class TestJoin:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        Since we are using the function `join` on the thread we wait for `myfunc` to end,
        for this reason we see all the output, because we are waiting before print the `main ended` statement
        """
        assert {
            "main started",
            "myfunc started with foo",
            "main ended",
            "myfunc ended",
        } == output
