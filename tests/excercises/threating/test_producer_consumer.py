from io import StringIO

import sys

from excercises.threating.producer_consumer import (
    main,
    producer_pipeline,
    consumer_pipeline,
)


class TestAccount:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        Thanks to the lock mechanism we are able to send and get the messages in the right order, with the final message
        THE END send as the end signal
        """
        assert len(consumer_pipeline) == 11
        assert len(producer_pipeline) == 11
        assert {
            f"consumer: {consumer_pipeline}",
            f"consuming message of {consumer_pipeline[0]}",
            f"consuming message of {consumer_pipeline[1]}",
            f"consuming message of {consumer_pipeline[2]}",
            f"consuming message of {consumer_pipeline[3]}",
            f"consuming message of {consumer_pipeline[4]}",
            f"consuming message of {consumer_pipeline[5]}",
            f"consuming message of {consumer_pipeline[6]}",
            f"consuming message of {consumer_pipeline[7]}",
            f"consuming message of {consumer_pipeline[8]}",
            f"consuming message of {consumer_pipeline[9]}",
            "consuming message of THE END",
            f"producer: {producer_pipeline}",
            f"producing message of {producer_pipeline[0]}",
            f"producing message of {producer_pipeline[1]}",
            f"producing message of {producer_pipeline[2]}",
            f"producing message of {producer_pipeline[3]}",
            f"producing message of {producer_pipeline[4]}",
            f"producing message of {producer_pipeline[5]}",
            f"producing message of {producer_pipeline[6]}",
            f"producing message of {producer_pipeline[7]}",
            f"producing message of {producer_pipeline[8]}",
            f"producing message of {producer_pipeline[9]}",
            "producing message of THE END",
        } == output
