

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):
    def process(self, data: list[int]) -> str:
        try:
            lenn = len(data)
            summ = sum(data)
            return (f"Processed {lenn} numeric values, "
                    f"sum={summ}, avg={summ/lenn}")
        except (TypeError, ValueError, ZeroDivisionError):
            return (f"ERROR: {data} Numeric Error")

    def validate(self, data: list[int]) -> bool:
        try:
            summ = sum(data)
            if summ > 0:
                return True
            else:
                return False
        except (TypeError, ValueError):
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        try:
            lenn = len(data)
            word = len(data.split(' '))
            return (f"Processed text: {lenn} characters, {word} words")
        except (AttributeError, ValueError):
            return (f"ERROR: {data} Text Error")

    def validate(self, data: str) -> bool:
        try:
            word = len(data.split(' '))
            if word:
                return True
            else:
                return False
        except (AttributeError, ValueError):
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        try:
            alert = data.split(":")
            if (alert[0] == "ERROR"):
                level = "[ALERT]"
            elif (alert[0] == "INFO"):
                level = "[INFO]"
            else:
                level = "[UNKNOWN]"
            return (f"{level} {alert[0]} level detected:{alert[1]}")
        except Exception:
            return (f"ERROR: {data} is must be string")

    def validate(self, data: str) -> bool:
        try:
            splited = data.split(':')
            if len(splited) != 2:
                return False
            else:
                return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")  # ##################
    data = [1, 2, 3, 4, 5]
    numeric_object = NumericProcessor()
    print(f"Processing data: {data}")
    process = numeric_object.process(data)
    if numeric_object.validate(data) is True:
        verify = "Numeric data verified"
    else:
        verify = "Numeric data is not verified"
    print("Validation:", verify)
    print(numeric_object.format_output(process))

    print("\nInitializing Text Processor...")  # ##################
    data = "Hello Nexus World"
    text_object = TextProcessor()
    print(f"Processing data: \"{data}\"")
    process = text_object.process(data)
    if text_object.validate(data) is True:
        verify = "Text data verified"
    else:
        verify = "Text data is not verified"
    print("Validation:", verify)
    print(text_object.format_output(process))

    print("\nInitializing Log Processor...")  # #####################
    data = "ERROR: Connection timeout"
    log_object = LogProcessor()
    print(f"Processing data: \"{data}\"")
    process = log_object.process(data)
    if log_object.validate(data) is True:
        verify = "Log entry verified"
    else:
        verify = "Log entry is not verified"
    print("Validation:", verify)
    print(log_object.format_output(process))

    print("\n=== Polymorphic Processing Demo ===")  # ################
    print("Processing multiple data types through same interface...")
    print("Result 1:", numeric_object.process([2, 1, 3]))
    print("Result 1:", text_object.process("Protect data"))
    print("Result 3:", log_object.process("INFO: System ready"))

    print("\nFoundation systems online. Nexus ready for advanced streams.")
