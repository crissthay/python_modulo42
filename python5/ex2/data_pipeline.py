from ex0.data_processor import NumericProcessor, TextProcessor, LogProcessor
from ex1.data_stream import DataStream as BaseDataStream
from typing import Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        text = [str(txt) for _, txt in data]
        print("CSV Output:")
        print(','.join(text))


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        lists = []
        for ind, value in data:
            lists.append('"item_' + str(ind) + '": "' + str(value) + '"')
        conteudo = ','.join(lists)
        print("JSON Output:")
        print("{" + conteudo + "}")


class DataStream(BaseDataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            listss = []
            for _ in range(nb):
                if proc.data:
                    tuplo = proc.output()
                    listss.append(tuplo)
            if listss:
                plugin.process_output(listss)


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
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {data2}")
    ds.process_stream(data2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()


if __name__ == '__main__':
    main()
