# Import the required libraries
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
import yaml, random, ctypes, itertools, requests, time, string, emoji_list
from requests import Session
import headerCollection
from urllib import parse

# Define a class for OmTraffic
class OmTraffic:
    # Define the class constructor
    def __init__(self):
        # Load the configuration from the YAML file
        with open("config.yml", "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)

        # Define the message, delay, number of threads, use of own proxies, proxy timeout, and language
        self.num_threads = cfg["misc"]["threads"]
        self.lang = cfg["misc"]["lang"]
        self.channel_type = cfg["misc"]["channel_type"]
        self.show_typing = cfg["misc"]["show_typing"]

        self.use_own_proxies = cfg["proxy"]["use_own"]
        self.proxy_timeout = cfg["proxy"]["timeout"]
        self.proxy_type = cfg["proxy"]["type"]

        self.delay = cfg["message"]["delay"]
        self.use_emoji = cfg["message"]["use_emoji"]
        self.rand_prefix = cfg["message"]["use_prefix"]
        self.rand_suffix = cfg["message"]["use_suffix"]
        self.topics = cfg["message"]["topics"]

        self.counter = 0
        self.failed_counter = 0
        self.proxies = []

        # Create a console object
        self.console = Console()

        # Define the console messages
        self.console.print("\n\nWelcome to OmTraffic", style="bold green")
        self.console.print("version 1.0.3", style="underline")
        self.console.print("\nMade with ❤️  by https://github.com/xyba1337\n\n")

        # Check if own proxies are used
        if self.use_own_proxies:
            with open("proxies.txt") as f:
                self.proxies = [line.strip() for line in f]
        else:
            api_url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={self.proxy_type}&timeout={str(self.proxy_timeout * 1000)}&country=all&ssl=all&anonymity=all"
            api_url2 = f"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/{self.proxy_type}.txt"
            api_url3 = f"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/{self.proxy_type}.txt"
            api_url4 = f"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/{self.proxy_type}.txt"

            try:
                response = requests.get(api_url)
                response2 = requests.get(api_url2)
                response3 = requests.get(api_url3)
                response4 = requests.get(api_url4)

                proxypool = response.text + "\r\n" + response2.text + "\r\n" + response3.text + "\r\n" + response4.text

                if response.status_code == 200:
                    self.proxies = proxypool.split("\r\n")
                    self.console.print(f"Found {len(self.proxies)} proxies", style="cyan")
                else:
                    self.console.print("Failed to fetch proxies")
            except requests.exceptions.RequestException as e:
                self.console.print(f"Error fetching proxies: {e}", style="red")

        with open("messages.txt") as f:
            self.messages = [line.strip() for line in f]

        # Create a proxy cycler
        self.proxy_cycler = itertools.cycle(self.proxies)

        # Create a message cycler
        self.message_cyler = itertools.cycle(self.messages)

        # Set the initial title
        ctypes.windll.kernel32.SetConsoleTitleW(f"Sent {self.counter} messages, failed {self.failed_counter} messages")

    def grabCCparam(self, s: Session) -> str:
        # Grab cc parameter
        url = f"https://waw{random.randint(1,4)}.omegle.com/check"

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

    
    def connectToServer(self, s: Session, ccParam: str) -> str:
        # Connect to server
        if ccParam is not None:
            if self.channel_type == "cam":
                url = f"https://front{random.randint(2,48)}.omegle.com/start?caps=recaptcha2,t3&firstevents=1&spid=&randid=WWCPUZHS&cc={ccParam}&lang={self.lang}&camera=OBS Virtual Camera&webrtc=1"
            else:
                url = f"https://front{random.randint(2,48)}.omegle.com/start?caps=recaptcha2,t3&firstevents=1&spid=&randid=WWCPUZHS&cc={ccParam}&lang={self.lang}"
            payload = {}

            if self.topics != []:
                url += "&topics=%s" % (parse.quote_plus(str(self.topics).replace(" ", "")))

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
                            "[bold][+][/] Connected to server [bold]" + client_id, style="cyan")
                        """ self.console.print(f"CONNECTED - {response.json()}") """ # Uncomment to see if you get a captcha
                        return client_id
                    else:
                        self.console.print("[bold][-][/] Failed to connect to server", style="red")
        
    def sendMessage(self, s: Session, clientId: str):
        # Send message
            url = f"https://front{random.randint(2,48)}.omegle.com/send"

            final_message = ""
            random_emoji = "" 
            random_prefix = ""
            random_suffix = ""

            if self.use_emoji: random_emoji = random.choice(emoji_list.all_emoji)

            if self.rand_prefix: random_prefix = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(3))

            if self.rand_suffix: random_suffix = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(3))

            message = next(self.message_cyler)

            final_message = f"{random_suffix} {message} {random_prefix} {random_emoji}"

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

    def disconnectFromServer(self, s: Session, clientId: str):
        url = f"https://front{random.randint(2,48)}.omegle.com/disconnect"
        payload = "id=" + clientId

        response = s.post(
            url, headers=headerCollection.plainHeaders, data=payload)

        if response.text == "win":
            self.console.print(
                "[bold][+][/] Disconnected from server [bold]" + clientId + "", style="blue")
        else:
            self.console.print("[bold][-][/] Failed to disconnect from server", style="red")
        
        time.sleep(self.delay)
            
        s.close()

    def fireTypeEvent(self, s: Session, clientId: str):
        url = f"https://front{random.randint(2,48)}.omegle.com/typing"
        payload = "id=" + clientId
        
        try:
            response = s.post(
                url, headers=headerCollection.plainHeaders, data=payload
            )

            if response.text == "win":
                self.console.print(
                "[bold][+][/] Fired type event [bold]" + clientId + "", style="blue")
            else:
                self.console.print(f"[bold][-][/] Failed to fire type event: {e}", style="red")

        except requests.exceptions.RequestException as e:
            self.console.print(f"{e}", style="red")
        
        time.sleep(self.delay)
            
        s.close()

    def mainAction(self):
        while True:
            session = requests.Session()

            # update title
            ctypes.windll.kernel32.SetConsoleTitleW(f"Sent {self.counter} messages, failed {self.failed_counter} messages")

            current_proxy = next(self.proxy_cycler)
            session.proxies = {
                "http": f"{self.proxy_type}://{current_proxy}",
                "https": f"{self.proxy_type}://{current_proxy}"
            }

            cc = self.grabCCparam(s = session)
            client_id = self.connectToServer(s = session, ccParam = cc)
            
            time.sleep(self.delay)

            if not client_id:
                self.failed_counter += 1
                continue

            if self.show_typing:
                self.fireTypeEvent(s = session, clientId = client_id)

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
                        
