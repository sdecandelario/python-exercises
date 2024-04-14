from io import StringIO

import sys

from excercises.threating.many_threads import main


class TestManyThreads:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        We see all the output here because we wait until all the threds finishes.
        We can't guaranty the order of the output because in each execution the threads can end in different order
        """
        assert {
            "main started",
            "myfunc1 started with foo",
            "myfunc2 started with bar",
            "myfunc3 started with baz",
            "myfunc1 ended",
            "myfunc2 ended",
            "myfunc3 ended",
            "main ended",
        } == output
