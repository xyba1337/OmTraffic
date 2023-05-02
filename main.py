# Import the required libraries
from concurrent.futures import ThreadPoolExecutor
import time
import requests
from rich.console import Console
import headerCollection
import itertools
import ctypes
import yaml
import random

# Define a class for OmTraffic
class OmTraffic:
    # Define the class constructor
    def __init__(self):
        # Load the configuration from the YAML file
        with open("config.yml", "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)

        # Define the message, delay, number of threads, use of own proxies, proxy timeout, and language
        self.message = cfg["message"]
        self.delay = cfg["message_delay"]
        self.num_threads = cfg["threads"]
        self.use_own_proxies = cfg["use_own_proxies"]
        self.proxy_timeout = cfg["proxy_timeout"]
        self.lang = cfg["lang"]
        self.counter = 0
        self.failed_counter = 0
        self.proxies = []

        # Create a console object
        self.console = Console()

        # Define the console messages
        self.console.print("\n\nWelcome to OmTraffic", style="bold green")
        self.console.print("version 1.0.0", style="underline")
        self.console.print("\nMade with ❤️  by https://github.com/xyba1337\n\n")

        # Check if own proxies are used
        if self.use_own_proxies == "yes":
            with open("proxies.txt") as f:
                self.proxies = [line.strip() for line in f]
        elif self.use_own_proxies == "no":
            api_url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout={str(self.proxy_timeout * 1000)}&country=all&ssl=all&anonymity=all"

            try:
                response = requests.get(api_url)

                if response.status_code == 200:
                    self.proxies = response.text.split("\r\n")
                    self.console.print(f"Found {len(self.proxies)} proxies", style="cyan")
                else:
                    self.console.print("Failed to fetch proxies")
            except requests.exceptions.RequestException as e:
                self.console.print(f"Error fetching proxies: {e}", style="red")

        # Create a proxy cycler
        self.proxy_cycler = itertools.cycle(self.proxies)

        # Set the initial title
        ctypes.windll.kernel32.SetConsoleTitleW(f"Sent {self.counter} messages, failed {self.failed_counter} messages")


    def grabCCparam(self, s):
        # Grab cc parameter
        url = f"https://waw3.omegle.com/check"

        data = None

        method = "POST"

        try:
            response = s.request(method, url, headers=headerCollection.plainHeaders, data=data, cookies=None, timeout=self.proxy_timeout)
            response.close()
            cc = response.text

            return cc
        except Exception as e:
            self.console.print(e, style="red")
            self.failed_counter += 1

    
    def connectToServer(self, s, ccParam):
        # Connect to server
        if ccParam is not None:
            url = "https://front47.omegle.com/start?caps=recaptcha2,t3&firstevents=1&spid=&randid=WWCPUZHS&cc=" + ccParam + "&lang=" + self.lang

            payload = {}

            response = None
            try:
                response = s.post(
                    url, headers=headerCollection.jsonHeaders, data=payload)
                response.close()
            except Exception as e: 
                self.console.print(e, style="red")

            if response is not None:
                """ print(response.json()) """
                if 'application/json' in response.headers.get('Content-Type', ''):
                    if "clientID" in response.json() and response.json()["clientID"]:
                        client_id = response.json()["clientID"]
                        self.console.print(
                            "\n[bold][+][/] Connected to server [bold]" + client_id, style="cyan")
                        """ self.console.print(f"CONNECTED - {response.json()}") """ # Uncomment to see if you get a captcha
                        return client_id
                    else:
                        self.console.print("[bold][-][/] Failed to connect to server", style="red")
        
    def sendMessage(self, s, clientId):
        # Send message
            url = 'https://front47.omegle.com/send'
            emoji_list = ["😊", "🚀", "🎉", "🐻", "🍕", "🌈", "🎵", "🦄", "🍔", "🎁", "🎈", "🎄", "🎃", "🐶", "🐱", "🐰", "🐼", "🐬", "🐞", "🌻", "🍁", "🍓", "🍩", "🍭", "🍺", "🎬", "🎮", "🎤", "🎸", "🎭", "🎨", "📚", "💡", "💻", "🚲", "🏠", "✈️", "⛵️", "🏖️", "🏞️", "🏙️", "🌅", "🌌", "🌉", "🔥", "💥", "💫", "👑", "💍", "💄", "👓", "🧢", "👟", "🎒", "📱", "🔑", "💰", "📌", "📆", "📬", "📦", "🛍️", "🛒", "📷", "🎥", "🔭", "🔬", "🌡️", "🚑", "🚒", "🚔", "🚕", "🚀", "🛸", "🛵", "🛴", "🛹", "🏍️", "🏎️", "🚲", "🏠", "🏰", "⛪️", "🏥", "🏫", "🏢", "🏭", "🏦", "🏛️", "🌲", "🌳", "🌴", "🌵", "🌾", "🍀", "🍁", "🍂", "🍃", "🍇", "🍈", "🍉", "🍊", "🍋", "🍌", "🍍", "🥭", "🍎", "🍏", "🍐", "🍑", "🍒", "🍓", "🥝", "🍅", "🥑", "🥦", "🥕", "🌽", "🥔", "🍠", "🥐", "🍞", "🥖", "🥨", "🧀", "🥚", "🍳", "🥞", "🥓", "🥩", "🍔", "🍟", "🍕", "🌭", "🥪", "🌮", "🌯", "🥗", "🥘", "🍲", "🍛", "🍜", "🍝", "🍠", "🍢", "🍣", "🍤", "🍥"]

            random_emoji = random.choice(emoji_list)
            final_message = self.message + " " + random_emoji
            data = {
                'msg': final_message,
                'id': clientId
            }

            try:
                response = s.post(url, headers=headerCollection.plainHeaders,
                                        data=data, cookies=None, verify=True)
                response.close()
            except Exception as e: 
                self.console.print(e, style="red")

            if response.text == "win":
                self.console.print(
                    "[bold][+][/] Sent message with content: [italic]" + final_message, style="green")
                self.counter += 1
            else:
                self.console.print("Failed to send message", style="red")
                self.failed_counter += 1

    def disconnectFromServer(self, s, clientId):
        url = "https://front47.omegle.com/disconnect"
        payload = "id=" + clientId

        response = s.post(
            url, headers=headerCollection.plainHeaders, data=payload)

        if response.text == "win":
            self.console.print(
                "[bold][+][/] Disconnected from server [bold]" + clientId + "\n", style="blue")
        else:
            self.console.print("[bold][-][/] Failed to disconnect from server\n", style="red")
        
        time.sleep(self.delay)
            
        s.close()

    def mainAction(self):
        while True:
            session = requests.Session()

            # update title
            ctypes.windll.kernel32.SetConsoleTitleW(f"Sent {self.counter} messages, failed {self.failed_counter} messages")

            current_proxy = next(self.proxy_cycler)
            session.proxies = { "https": current_proxy }

            cc = self.grabCCparam(s = session)
            client_id = self.connectToServer(s = session, ccParam = cc)
            
            time.sleep(self.delay)

            if not client_id:
                self.failed_counter += 1
                continue

            self.sendMessage(s = session, clientId = client_id)
            
            time.sleep(self.delay)

            # Disconnect from server
            self.disconnectFromServer(s = session, clientId = client_id)


    def runProgram(self):
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            # Submit mainAction function to executor for each thread
            for i in range(self.num_threads):
             executor.submit(self.mainAction)

Om = OmTraffic()
Om.runProgram()
                        
