[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/avmmodules/AVMYT">
    <img src="https://raw.githubusercontent.com/avmmodules/AVMYT/main/img/logo.png" alt="Logo" width="300">
  </a>

  <h3 align="center">AVMYT</h3>

  <p align="center">
    Get information from Youtube in a simple way!
    <br />
    <a href="https://github.com/avmmodules/AVMYT"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/avmmodules/AVMYT/issues">Report Bug</a>
    ·
    <a href="https://github.com/avmmodules/AVMYT/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![miniatura][miniatura]](https://pypi.org/project/AVMYT/)

If you want to watch the explanation in video, see the [link](https://www.youtube.com/avmmodules)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You need to make sure you have installed the following modules.
* BeautifulSoup
  ```s
  pip install bs4
  ```

* HTMLSession
  ```s
  pip install requests_html
  ```

* webbrowser
  ```s
  pip install webbrowser
  ```

### Installation

```python
pip install AVMYT
```

<!-- USAGE EXAMPLES -->
## Usage

* Example 1
    ```python
    import AVMYT as yt

    channel = yt.getChannelInfo("luisito")
    print(channel["name"] + " tiene " + channel["subs"] + " y un total de " + channel["videos"]) # prints info of Luisito Comunica
    ```

* Example 2
    ```python
    import AVMYT as yt

    yt.play("bad guy") # opens the song in Youtube
    ```

_For more examples, please refer to the [Examples packages](https://github.com/avmmodules/AVMYT/tree/main/examples)_

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/avmmodules/AVMYT/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Youtube: [/avmmodules](https://youtube.com/avmmodules)

Email: avmmodules@gmail.com

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/avmmodules/AVMYT.svg?style=for-the-badge
[contributors-url]: https://github.com/avmmodules/AVMYT/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/avmmodules/AVMYT.svg?style=for-the-badge
[forks-url]: https://github.com/avmmodules/AVMYT/network/members
[stars-shield]: https://img.shields.io/github/stars/avmmodules/AVMYT.svg?style=for-the-badge
[stars-url]: https://github.com/avmmodules/AVMYT/stargazers
[issues-shield]: https://img.shields.io/github/issues/avmmodules/AVMYT.svg?style=for-the-badge
[issues-url]: https://github.com/avmmodules/AVMYT/issues
[license-shield]: https://img.shields.io/github/license/avmmodules/AVMYT.svg?style=for-the-badge
[license-url]: https://github.com/avmmodules/AVMYT/blob/main/LICENSE
[miniatura]: https://raw.githubusercontent.com/avmmodules/AVMYT/main/img/miniatura.png
