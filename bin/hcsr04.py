#!/usr/bin/env python

from hcsr04sensor import sensor
import argparse


def get_args():
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(
        description="Script tests the HCSR04 sensor under different configurations"
    )

    parser.add_argument(
        "-t",
        "--trig",
        type=int,
        help="Trig Pin (Required - must be an integer, must \
                             use BCM pin values)",
        required=True,
    )

    parser.add_argument(
        "-e",
        "--echo",
        type=int,
        help="Echo Pin (Required - must be an integer, must \
                             use BCM pin values)",
        required=True,
    )

    parser.add_argument(
        "-sp",
        "--speed",
        type=float,
        help="Time between individual reading samples \
                             (Optional - must be a float, default\
                              is 0.1 seconds)",
        required=False,
        default=0.1,
    )

    parser.add_argument(
        "-ss",
        "--samples",
        type=int,
        help="Reading Sample Size (Optional - must be an \
                                integer, default is 11)",
        required=False,
        default=11,
    )

    args = parser.parse_args()

    trig = args.trig
    echo = args.echo
    speed = args.speed
    samples = args.samples

    return trig, echo, speed, samples


def main():
    """Main function to run the sensor with passed arguments"""

    trig, echo, speed, samples = get_args()

    print(f"trig pin = gpio {trig}")
    print(f"echo pin = gpio {echo}")
    print(f"speed = {speed}")
    print(f"samples = {samples}")
    print("")
    value = sensor.Measurement(trig, echo)
    raw_distance = value.raw_distance(sample_size=samples, sample_wait=speed)
    imperial_distance = value.distance(raw_distance) * 0.394
    metric_distance = value.distance(raw_distance)
    print(f"The imperial distance is {round(imperial_distance, 1)} inches.")
    print(f"The metric distance is {round(metric_distance, 1)} centimetres.")


if __name__ == "__main__":
    main()
