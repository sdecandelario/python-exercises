from io import StringIO

import sys

from excercises.threating.producer_consumer_queue import (
    consumer_pipeline,
    producer_pipeline,
    main,
)


class TestQueue:

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        output = set(printed_output.strip().split("\n"))

        """
        Here we are checking that extending from Queue the class pipeline,
        we are able to send and receive all the messages no losing anyone and we don't need to implement
        any custom lock system, since everything is handled by the queue
        """
        assert len(consumer_pipeline) == 10
        assert len(producer_pipeline) == 10
        assert {
            f"consumer: {consumer_pipeline}",
            f"producer: {producer_pipeline}",
            "queue size is 1",
            "queue size is 2",
            "queue size is 3",
            "queue size is 4",
            "queue size is 5",
            "queue size is 6",
            "queue size is 7",
            "queue size is 8",
        }.issubset(output)
