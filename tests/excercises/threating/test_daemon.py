from io import StringIO

import sys

from excercises.threating.daemon import main


class TestDaemon:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        Here is missing the output 'myfunc ended' because the thread is not finished when the function is ended.
        This happens because we used the `daemon` parameter when creating the thread,
        so when the `main` function ends we don't wait for `myfunc`
        """
        assert {"main started", "myfunc started with foo", "main ended"} == output
