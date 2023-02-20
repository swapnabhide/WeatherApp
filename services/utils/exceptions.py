class LocationError(Exception):
    """ 
    Exception raised when the address searched for is invalid
    
    Attributes:
        address -- input salary which caused the error
    """
    def __init__(self, address) -> None:
        self.address = address
        self.message = f"{address} is likely invalid, please recheck"
        super().__init__(self.message)
