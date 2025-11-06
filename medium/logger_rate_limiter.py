"""
Problem: Logger Rate Limiter
Design logger that prints messages if not printed in last 10 seconds.
"""

class Logger:
    def __init__(self):
        self.msg_timestamps = {}  # message → last printed time

    def should_print_message(self, timestamp, message):
        """
        Solution: Use hash map to store last print time
        Time: O(1) per call, Space: O(m) m = unique messages
        """
        if message in self.msg_timestamps:
            if timestamp < self.msg_timestamps[message] + 10:
                return False

        self.msg_timestamps[message] = timestamp
        return True

# Test
if __name__ == "__main__":
    logger = Logger()
    print(logger.should_print_message(1, "foo"))   # True
    print(logger.should_print_message(2, "bar"))   # True
    print(logger.should_print_message(3, "foo"))   # False
    print(logger.should_print_message(11, "foo"))  # True