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


def main():
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing")
    numeric = NumericProcessor()
    print("Invalide input:", numeric.validate(42))
    print("Valide input:", numeric.validate("hello"))
    print("Extracting 3 values...")
    datas = [1, 2, 3]
    print(f"Processing datas: {datas}")
    numeric.ingest(datas)
    print(numeric.output())
    print(numeric.output())
    print(numeric.output())
    print()
    print("Testing Text Processor...")
    text_val = TextProcessor()
    i = ["Thay", "ama", "taerae"]
    print(f"Try to validate input '{i}': {text_val.validate(i)}")
    print("Extracting 1 Value...")
    text_val.ingest(i)
    print(text_val.output())
    print()
    print("Texting Log Process")
    log = LogProcessor()
    d = {'log_level': 'NOTICE', 'log_message': 'Connection to server'}
    print(f"Try to validate input '{d}': {log.validate(d)}")
    print("Extracting 2 Value...")
    log.ingest(d)
    print(log.output())


if __name__ == '__main__':
    main()
