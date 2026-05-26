from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.data = []
        self.index = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise IndexError("No data")
        value = self.data.pop(0)
        idx = self.index
        self.index += 1
        return (idx, value)  # ← tuplo correto


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(ex, (int, float)) for ex in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Expect Numeric...")
        if isinstance(data, list):
            for n in data:
                self.data.append(str(n))
        else:
            self.data.append(str(data))

    def output(self):
        return super().output()


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(s, str) for s in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Expect text...")
        if isinstance(data, list):
            for s in data:
                self.data.append(str(s))
        else:
            self.data.append(str(data))

    def output(self):
        return super().output()


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            return all(isinstance(d, dict) for d in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        if isinstance(data, dict):
            self.data.append(f"{data['log_level']}: {data['log_message']}")
        elif isinstance(data, list):
            for item in data:
                self.data.append(f"{item['log_level']}: {item['log_message']}")

    def output(self):
        return super().output()


class DataStream:

    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
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
