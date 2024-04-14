import sys
from io import StringIO

from excercises.threating.thread_pool import main


class TestThreadPool:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        Instead of generate multiple threads, we create a `ThreadPoolExecutor` with a maximum of three workers,
        then we send the arguments ("foo", "bar", "baz") to generate 3 threads and read the output generated
        """
        assert {
            "main begins",
            "myfunc started with foo",
            "myfunc started with bar",
            "myfunc started with baz",
            "myfunc ended with foo",
            "myfunc ended with bar",
            "myfunc ended with baz",
            "main ended",
        } == output
