# OmTraffic

OmTraffic is a Python script for sending messages to random strangers on Omegle. It is designed to simulate human-like behavior by sending messages with randomized emojis and using a rotating proxy list to avoid getting blocked by Omegle.

## Preview
It is recommended to use good premium proxies for the best performance.
In this preview I used premium proxyscrape proxies with 100 threads, they are decent but something like webshare would be better.

## Features

* Sends messages with randomized emojis
* Multi-threaded for faster message sending
* Customizable message delay and number of threads
* Supports use of own proxies or automatic proxy scraping (HTTP only)
* Configurable language settings

## How to Use

1. Clone this repository to your local machine:

```sh
git clone https://github.com/xyba1337/OmTraffic.git
```

2. Install the required Python packages:
```sh
pip install -r requirements.txt
```

3. Configure the script by editing the config.yml file:
```python
message: "Hello, how are you?"  # The message to send
message_delay: 2  # Delay in seconds between each message
threads: 10  # Number of threads to use for sending messages
use_own_proxies: "no"  # "yes" if using own proxies, "no" if scraping proxies
proxy_timeout: 10  # Proxy timeout in seconds
lang: "en"  # Language to use for Omegle
```

4. Run the script:
```python
python main.py
```

## Contributions
Contributions to this project are highly appreciated. Feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

