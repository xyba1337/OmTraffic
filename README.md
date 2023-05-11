![OmTraffic](OmTraffic.png)

<div align='center'>

  <a href='https://github.com/chroline/well_app/releases'>
  
  <img src='https://img.shields.io/github/v/release/xyba1337/omtraffic?color=%23FDD835&label=version&style=for-the-badge'>
  
  </a>
  
  <a href='https://github.com/xyba1337/omtraffic/blob/main/LICENSE'>
  
  <img src='https://img.shields.io/github/license/xyba1337/omtraffic?style=for-the-badge'>
  
  </a>

</div>

<br>

---

# :speech_balloon: OmTraffic 
OmTraffic is a fast and efficient Python script that enables you to send a large number of messages to random strangers on Omegle quickly. :rocket: It's for educational purposes only! :mortar_board:

## 🌟Star this repo if you enjoy using our tool and want it to stay updated and working

## :eyes: Preview 
It is recommended to use good premium proxies for the best performance. We can highly recommend you intenseproxy.com but don't use rotating proxies, they wont work!
If you use proxies with username and password, make sure that they are in the format of username:password@ip:port

![](https://github.com/xyba1337/OmTraffic/blob/main/Preview.gif)

## :rocket: Features 

* Sends messages with randomized emojis, prefix, suffix to avoid detections :robot:
* Multi-threaded for faster message sending :zap:
* Customizable message delay and number of threads :gear:
* Supports use of own proxies and every proxy type or automatic proxy scraping :globe_with_meridians:
* Configurable language settings :earth_americas:
* Typing spoofer :keyboard:

## :computer: How to Use 

1. Clone this repository to your local machine:

```sh
git clone https://github.com/xyba1337/OmTraffic.git
```

2. Install the required Python packages:
```sh
pip install -r requirements.txt
```

3. Configure the script by editing the config.yml file:
```yml
misc:
  threads: 20  # Number of threads to use for sending messages
  lang: "en"  # Language to use for Omegle (en, de, es, fr, and so on...) -> "Alpha 2"-> https://www.nationsonline.org/oneworld/country_code_list.htm 
  channel_type: "text"  # Text/Cam
  show_typing: true # Shows the "Typing..." message to the user on the other end before sending the message
proxy:
  use_own: true # "true" if using own proxies, "false" if scraping proxies
  type: "http"  # http/socks4/socks4a/socks5
  timeout: 10 # Proxy timeout in seconds
message:
  delay: 2  # Delay in seconds between each message
  use_emoji: true # Adds a random emoji to the end of each message
  use_prefix: false  # Adds a random string to the end of each message
  use_suffix: false  # Adds a random string to the start of each message
  delay_after: 2 # How long until disconnect after the message has been sent
  topics: [] # Topics/Keywords to queue inside of, Example: ["minecraft", "valorant"].

```

4. Run the script:
```python
python main.py
```

## :handshake: Contributions
Contributions to this project are highly appreciated. Feel free to submit a pull request or open an issue for any suggestions or improvements.

## :page_with_curl: License

This project is licensed under the MIT License. See the LICENSE file for details.

