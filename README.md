# OmTraffic
OmTraffic is a fast and efficient Python script that enables you to send a large number of messages to random strangers on Omegle quickly.
Educational purpouses only.

## Preview
It is recommended to use good premium proxies for the best performance.<br>
In this preview I used premium proxyscrape proxies with 100 threads, they are decent but something like webshare would be better.

![](https://github.com/xyba1337/OmTraffic/blob/main/Preview.gif)

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
misc:
  threads: 100  # Number of threads to use for sending messages
  lang: "en"  # Language to use for Omegle (en, de, es, fr, and so on...) -> "Alpha 2"-> https://www.nationsonline.org/oneworld/country_code_list.htm 
  channel_type: "text"  # Text/Cam
  show_typing: true # Shows the "Typing..." message to the user on the other end before sending the message
proxy:
  use_own: false # "true" if using own proxies, "false" if scraping proxies
  type: "http"  # http/socks4/socks4a/socks5
  timeout: 10 # Proxy timeout in seconds
message:
  content: "Hello, how are you?"  # The message to send
  delay: 2  # Delay in seconds between each message
  use_emoji: true # Adds a random emoji to the end of each message
  use_prefix: false  # Adds a random string to the end of each message
  use_suffix: false  # Adds a random string to the start of each message

```

4. Run the script:
```python
python main.py
```

## Contributions
Contributions to this project are highly appreciated. Feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

