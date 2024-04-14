import sys
from io import StringIO

from excercises.threating.thread import main


class TestThread:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        Here is missing the output 'myfunc ended' because the thread is not finished when the function is ended.
        This happens because we added an sleep of 10 seconds inside of `myfunc` and this is called by a thread
        """
        assert {"main started", "myfunc started with foo", "main ended"} == output
