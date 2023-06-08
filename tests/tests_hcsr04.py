import unittest
from unittest.mock import patch
from io import StringIO
from bin.hcsr04 import get_args, main


class TestHCSR04Sensor(unittest.TestCase):
    def test_get_args(self):
        """Test the get_args function"""

        args = ["-t", "17", "-e", "27"]
        with patch("sys.argv", ["bin/hcsr04"] + args):
            trig, echo, speed, samples = get_args()

            # Check if the parsed arguments match the expected values
            self.assertEqual(trig, 17)
            self.assertEqual(echo, 27)
            self.assertEqual(speed, 0.1)
            self.assertEqual(samples, 11)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("hcsr04sensor.sensor.Measurement.raw_distance")
    def test_main(self, mock_raw_distance, mock_stdout):
        """Test the main function"""

        trig = 17
        echo = 27
        speed = 0.1
        samples = 11
        raw_distance_value = 13.542656911364793

        expected_output = (
            f"trig pin = gpio {trig}\n"
            f"echo pin = gpio {echo}\n"
            f"speed = {speed}\n"
            f"samples = {samples}\n\n"
            f"{raw_distance_value}\n"
            "The imperial distance is 5.3 inches.\n"
            "The metric distance is 13.5 centimetres.\n"
        )

        # Configure the mock raw_distance method to return the desired raw_distance value
        mock_raw_distance.return_value = raw_distance_value

        with patch("sys.argv", ["bin/hcsr04", "-t", str(trig), "-e", str(echo)]):
            main()

        output = mock_stdout.getvalue()

        # Check if the output matches the expected output
        self.assertEqual(output.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
