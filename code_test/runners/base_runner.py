from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from typedb.driver import TypeDB, TransactionType, Credentials, DriverOptions


class BaseRunner(ABC):
    def __init__(self, adoc_keys: List[str]):
        self.adoc_keys = adoc_keys
        self.success_count = 0
        self.failure_count = 0

        # TypeDB connection config
        self.username = "admin"
        self.password = "password"
        self.uri = "127.0.0.1:1729"

    def reset_counts(self):
        self.success_count = 0
        self.failure_count = 0

    def reset_local_databases(self):
        driver = TypeDB.driver(address=self.uri, credentials=Credentials(self.username,self.password), driver_options=DriverOptions())
        for database in driver.databases.all():
            database.delete()

    @abstractmethod
    def check_config(self, adoc_config: Dict[str, str]) -> bool:
        pass

    @abstractmethod
    def run_test(self, parsed_test, adoc_path: str):
        pass

    @abstractmethod
    def try_test(self, parsed_test, index: int, adoc_path: str):
        pass

    @abstractmethod
    def try_tests(self, parsed_tests, adoc_path: str, config: Dict[str, str]):
        pass