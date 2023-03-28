import requests
from bs4 import BeautifulSoup


class Weather:
    def __init__(self, url: str, file_path=False) -> None:
        """
        Initialiser of Weather class

        Parameters:
        url (str): BBC Weather URL to read data from or path to HTML file if
        file_path=True
        file_path (bool): True if reading from a file rather than a URL
        """
        if file_path:
            pageFile = open(url)
            self.soup = BeautifulSoup(pageFile.read(), "html.parser")
        else:
            pageResp = requests.get(url)
            self.soup = BeautifulSoup(pageResp.content, "html.parser")

    def setURL(self, url: str) -> None:
        """
        Sets URL and updates object's soup (BeautifulSoup) state

        Parameters:
        url (str): BBC Weather URL to read data from
        """
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, "html.parser")

    def getMaxT(self) -> int:
        """
        Returns today's forecast maximum temperature

        Returns:
        int: Today's forecast maximum temperature
        """
        tempLine = self.soup.find(
            class_="wr-value--temperature--c"
        )  # Today's max is first instance
        maxTemp = int(tempLine.text[:-1])
        return maxTemp

    def getMinT(self) -> int:
        """
        Returns today's forecast minimum temperature

        Returns:
        int: Today's forecast minimum temperature
        """
        tempLine = self.soup.find_all(class_="wr-value--temperature--c")[
            1
        ]  # Today's min is second instance
        minTemp = int(tempLine.text[:-1])
        return minTemp

    def getLoc(self) -> str:
        """
        Returns location of forecast currently being read

        Returns:
        str: Location of Weather forecast being read
        """
        locLine = self.soup.find(class_="wr-c-location__name")
        location = locLine.find(
            "span"
        ).previous_sibling  # Gets just the location avoiding weather warning
        return location
