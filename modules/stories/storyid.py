class Storyids(object):
    def __init__(self, min_length: int = 12) -> None:
        self._min_length = max(int(min_length), 0)
        pass

    def encode(self, num: int) -> int:
        # Count the number of digits in n
        num_digits = len(str(num))
        # Calculate the number of digits needed to match the target value
        num_zeros = self._min_length - num_digits
        # Create a string of zeros with the appropriate number of digits
        zeros = "0" * num_zeros
        # Concatenate the zeros and the original integer to create the final value
        large_int = zeros + str(num)
        return large_int

    def decode(self, large_int: int) -> int:
        # Convert the large integer to a string
        str_int = str(large_int)
        # Remove leading zeros
        str_int = str_int.lstrip("0")
        # Convert the string back to an integer
        num = int(str_int)
        return num
