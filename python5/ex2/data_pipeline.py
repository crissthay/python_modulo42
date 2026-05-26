from typing import Protocol, Any
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
        return (idx, value)


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
            self.data.append(
                f"{data['log_level']}: {data['log_message']}"
            )
        else:
            for item in data:
                self.data.append(
                    f"{item['log_level']}: {item['log_message']}"
                )


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        text = [txt for _, txt in data]
        print("CSV Output:")
        print(",".join(text))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []

        for ind, value in data:
            items.append(f'"item_{ind}": "{value}"')

        print("JSON Output:")
        print("{" + ",".join(items) + "}")


class DataStream:
    def __init__(self):
        self.processors: list[DataProcessor] = []

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            outputs = []

            for _ in range(nb):
                if proc.data:
                    outputs.append(proc.output())

            if outputs:
                plugin.process_output(outputs)

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
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors\n")

    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    ds.register_processor(num)
    ds.register_processor(txt)
    ds.register_processor(log)

    print(f"Send first batch of data on stream: {data}")

    ds.process_stream(data)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")

    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)

    ds.print_processors_stats()

    data2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {data2}")

    ds.process_stream(data2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")

    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)

    ds.print_processors_stats()


if __name__ == "__main__":
    main()