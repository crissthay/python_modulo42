
from ex0.data_processor import DataProcessor, NumericProcessor
from ex0.data_processor import TextProcessor, LogProcessor
import typing


class DataStream:

    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break

            if not handled:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{item}"
                )

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace(
                "Processor", " Processor"
            )
            print(
                f"{name}: total {proc.index} items processed, "
                f"remaining {len(proc.data)} on processor"
            )


def main():
    print("=== Code Nexus - Data Stream ===\n")

    ds = DataStream()

    print("Initialize Data Stream...")
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    num = NumericProcessor()
    ds.register_processor(num)

    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"Send first batch of data on stream: {data}")
    ds.process_stream(data)
    ds.print_processors_stats()

    print("Registering other data processors")
    txt = TextProcessor()
    log = LogProcessor()
    ds.register_processor(txt)
    ds.register_processor(log)

    print("Send the same batch again")
    ds.process_stream(data)
    ds.print_processors_stats()

    print(
        "Consume some elements from processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        try:
            num.output()
        except Exception:
            pass

    for _ in range(2):
        try:
            txt.output()
        except Exception:
            pass

    for _ in range(1):
        try:
            log.output()
        except Exception:
            pass

    ds.print_processors_stats()


if __name__ == '__main__':
    main()
