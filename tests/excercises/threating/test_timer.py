from io import StringIO

import sys

import pytest

from excercises.threating.timer import main


class TestTimer:

    @pytest.mark.parametrize("interval,expected_output", [(5, ""), (1, "BOOM!\nBOOM!")])
    def test_output_timer_interval_bigger_than_sleep_show_nothing(
        self, interval: int, expected_output: str
    ):
        captured_output = StringIO()
        sys.stdout = captured_output

        main(interval)

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = printed_output.strip()

        """
        In the first case we don't obtain any output because the timer ends before the program, and as we know
        thread are something async, for this reason we don't wait to the thread to end.

        In the second case we see the output because the thread with the timer ends before our program sleep
        """
        assert expected_output == output
