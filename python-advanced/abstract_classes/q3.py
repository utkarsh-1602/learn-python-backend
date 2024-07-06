from abc import ABC, abstractmethod

# Abstract Scanner class
class AbstractScanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def get_scanner_status(self):
        pass

# Abstract Printer class
class AbstractPrinter(ABC):
    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def get_printer_status(self):
        pass

# MFD1: Cheap device with low capabilities
class MFD1(AbstractScanner, AbstractPrinter):
    def scan_document(self):
        return "Document has been scanned with low resolution."

    def print_document(self):
        return "Document has been printed with low resolution."

    def get_scanner_status(self):
        return "Max resolution: Low, Serial number: SC01"

    def get_printer_status(self):
        return "Max resolution: Low, Serial number: PR01"

# MFD2: Medium-priced device with better capabilities
class MFD2(AbstractScanner, AbstractPrinter):
    def scan_document(self):
        return "Document has been scanned with medium resolution."

    def print_document(self):
        return "Document has been printed with medium resolution."

    def get_scanner_status(self):
        return "Max resolution: Medium, Serial number: SC02"

    def get_printer_status(self):
        return "Max resolution: Medium, Serial number: PR02"

# MFD3: Premium device with additional features like fax
class MFD3(AbstractScanner, AbstractPrinter):
    def scan_document(self):
        return "Document has been scanned with high resolution."

    def print_document(self):
        return "Document has been printed with high resolution."

    def get_scanner_status(self):
        return "Max resolution: High, Serial number: SC03"

    def get_printer_status(self):
        return "Max resolution: High, Serial number: PR03"

# Instantiate MFD1, MFD2, MFD3 to demonstrate their abilities
def main():
    mfd1 = MFD1()
    mfd2 = MFD2()
    mfd3 = MFD3()

    # Demonstrate scanning and printing
    print("MFD1 Scan:", mfd1.scan_document())
    print("MFD1 Print:", mfd1.print_document())
    print("MFD1 Scanner Status:", mfd1.get_scanner_status())
    print("MFD1 Printer Status:", mfd1.get_printer_status())

    print("\nMFD2 Scan:", mfd2.scan_document())
    print("MFD2 Print:", mfd2.print_document())
    print("MFD2 Scanner Status:", mfd2.get_scanner_status())
    print("MFD2 Printer Status:", mfd2.get_printer_status())

    print("\nMFD3 Scan:", mfd3.scan_document())
    print("MFD3 Print:", mfd3.print_document())
    print("MFD3 Scanner Status:", mfd3.get_scanner_status())
    print("MFD3 Printer Status:", mfd3.get_printer_status())

if __name__ == "__main__":
    main()
