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
    print("trig pin = gpio {}".format(trig))
    print("echo pin = gpio {}".format(echo))
    print("speed = {}".format(speed))
    print("samples = {}".format(samples))
    print("")

    value = sensor.Measurement(trig, echo)
    raw_distance = value.raw_distance(sample_size=samples, sample_wait=speed)

    imperial_distance = value.distance_imperial(raw_distance)
    metric_distance = value.distance_metric(raw_distance)
    print("The imperial distance is {} inches.".format(round(imperial_distance, 1)))
    print("The metric distance is {} centimetres.".format(round(metric_distance, 1)))


if __name__ == "__main__":
    main()
