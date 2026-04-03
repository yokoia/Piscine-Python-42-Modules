

from abc import ABC, abstractmethod
from typing import List, Any, Optional, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.__id = stream_id
        self.data = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return [data for data in data_batch if data != criteria]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"count": len(self.data)}

    def get_id(self) -> str:
        return (self.__id)


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = None

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.data = self.filter_data(data_batch)
            avg = self.get_stats().get("avgtemp", 0)
            count = 0
            for data in self.data:
                if isinstance(data, dict):
                    count = count + len(data)
                else:
                    raise ValueError("Data must be a dictionary")
            return f"{count} readings processed, avg temp: {avg}"
        except ValueError as e:
            print("Error", e)
            return "Error"
        except Exception as e:
            print("Error", e)
            return "Error"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        temp = []
        try:
            for data in self.data:
                if isinstance(data, dict):
                    if isinstance(data["temp"], (int, float)):
                        temp.append(data["temp"])
                else:
                    raise ValueError("ERROR: Data must be written like: "
                                     "<key:value>.")
            avgtemp = sum(temp) / len(temp)
            return {"avgtemp": avgtemp}
        except ValueError as e:
            print(e)
            return {"Errortemp": 404}
        except Exception as e:
            print("Error:", e)
            return {"Errortemp": 404}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = None

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.data = self.filter_data(data_batch)
            remain_units = self.get_stats().get("flow", 0)
            return (f"{len(self.data)} operations, net flow: "
                    f"+{remain_units} units")
        except Exception as e:
            print("Error", e)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        buy = []
        sell = []
        try:
            for data in self.data:
                if isinstance(data, str):
                    splited = data.split(':')
                    qty = int(splited[1])
                    if splited[0] == "buy":
                        buy.append(qty)
                    if splited[0] == "sell":
                        sell.append(qty)
                else:
                    raise ValueError("ERROR: Data must be written like: "
                                     "<item:number>.")
            flow = sum(buy) - sum(sell)
            return {"flow": flow}
        except ValueError as e:
            print(e)
            return {"Errorflow": 404}
        except Exception as e:
            print("Error:", e)
            return {"Errorflow": 404}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = None

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.data = self.filter_data(data_batch)
            errors = self.get_stats().get("error", 0)
            return f"{len(self.data)} events, {errors} error detected"
        except Exception as e:
            print("Error", e)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        error = 0
        try:
            for data in self.data:
                if isinstance(data, str):
                    if data == "error":
                        error += 1
                else:
                    raise ValueError("ERROR: data must be string")
            return {"error": error}
        except Exception as e:
            print("Error", e)
            return {"Error": 404}


class StreamProcessor:
    def __init__(self) -> None:
        self.__streams = []

    def add_stream(self, streams: List[DataStream]) -> None:
        for stream in streams:
            self.__streams.append(stream)

    def process_all(self) -> None:

        for stream in self.__streams:
            try:
                if isinstance(stream, SensorStream):
                    returning = stream.process_batch(stream.data)
                    splited = returning.split(',')
                    print(f"- Sensor data: {splited[0]}")
                elif isinstance(stream, TransactionStream):
                    returning = stream.process_batch(stream.data)
                    splited = returning.split(',')
                    print(f"- Transaction data: {splited[0]} processed")
                elif isinstance(stream, EventStream):
                    returning = stream.process_batch(stream.data)
                    splited = returning.split(',')
                    print(f"- Event data: {splited[0]} processed")
            except Exception as e:
                print(f"Error processing {stream.stream_id}: {e}")

    def filter_result(self) -> Dict[str, int]:
        alerts = 0
        large_tran = 0
        try:
            for stream in self.__streams:
                if isinstance(stream, SensorStream):
                    for data in stream.data:
                        if data.get("temp", 0) > 20:
                            alerts += 1
                if isinstance(stream, EventStream):
                    for data in stream.data:
                        if data == "error":
                            alerts += 1
                elif isinstance(stream, TransactionStream):
                    for data in stream.data:
                        if isinstance(data, str):
                            splited = data.split(':')
                            if splited[0] == "sell":
                                qty = int(splited[1])
                                if qty > 100:
                                    large_tran += 1
            return {"alerts": alerts, "large_tran": large_tran}
        except Exception as e:
            print("Error", e)
            return {"error": 404}


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")  # ####

    print("Initializing Sensor Stream...")
    sensor_list = [{"temp": 22.5, "humidity": 65, "pressure": 1013}]
    sensor_stream = SensorStream("SENSOR_001")
    sensor_stream.type = " Environmental Data"
    print(f"Stream ID: {sensor_stream.get_id()}, Type: {sensor_stream.type}")
    print("Processing sensor batch:", sensor_list)
    process1 = sensor_stream.process_batch(sensor_list)
    print("Sensor analysis:", process1)

    print("\nInitializing Transaction Stream...")  # ####
    tran_list = ["buy:100", "sell:150", "buy:75"]
    tran_stream = TransactionStream("TRANS_001")
    tran_stream.type = "Financial Data"
    print(f"Stream ID: {tran_stream.get_id()}, Type: {tran_stream.type}")
    print("Processing transaction batch:", tran_list)
    process2 = tran_stream.process_batch(tran_list)
    print("Transaction analysis:", process2)

    print("\nInitializing Event Stream...")  # ####
    event_list = ["login", "error", "logout"]
    event_stream = EventStream("EVENT_001")
    event_stream.type = "System Events"
    print(f"Stream ID: {event_stream.get_id()}, Type: {event_stream.type}")
    print("Processing event batch:", event_list)
    process3 = event_stream.process_batch(event_list)
    print("Event analysis:", process3)

    print("\n=== Polymorphic Stream Processing ===")  # ####
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    stream_manager = StreamProcessor()
    all_streams = [sensor_stream, tran_stream, event_stream]
    stream_manager.add_stream(all_streams)
    stream_manager.process_all()
    print("\nStream filtering active: High-priority data only")
    dictt = stream_manager.filter_result()
    print(f"Filtered results: {dictt["alerts"]} critical sensor alerts, "
          f"{dictt["large_tran"]} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
