import logging
from argparse import ArgumentParser

import cothread
from softioc import softioc, builder

from webScrapeBBCSkel.weather import Weather

from . import __version__

__all__ = ["main"]


def main(args=None):
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version=__version__)
    args = parser.parse_args(args)

    # Device prefix
    builder.SetDeviceName("bryn")

    # Create PVs
    maxTInput = builder.aIn("maxT", initial_value=-999)
    minTInput = builder.aIn("minT", initial_value=-999)
    urlOutput = builder.stringOut(
        "url", initial_value="https://www.bbc.co.uk/weather/2647114"
    )
    locInput = builder.stringIn("loc")

    # Get the IOC started
    builder.LoadDatabase()
    softioc.iocInit()

    def getTemps(weather: Weather):
        maxTemp = weather.getMaxT()
        minTemp = weather.getMinT()
        location = weather.getLoc()
        logging.info("New max =%i", maxTemp)
        logging.info("Previous max=%i", maxTInput.get())
        logging.info("New min =%i", minTemp)
        logging.info("Previous min=%i", minTInput.get())
        logging.info(location)
        maxTInput.set(maxTemp)
        minTInput.set(minTemp)
        locInput.set(location)
        cothread.Sleep(10)

    def runTemps():
        url = urlOutput.get()
        weather = Weather(url)
        getTemps(weather)
        while True:
            url = urlOutput.get()
            weather.setURL(url)
            getTemps(weather)

    cothread.Spawn(runTemps)

    cothread.WaitForQuit()


# test with: python -m webScrapeBBCSkel
if __name__ == "__main__":
    main()
