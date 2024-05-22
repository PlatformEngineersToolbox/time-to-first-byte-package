<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/PlatformEngineersToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/platformengineerstoolbox/black-and-white-circle-256.png" alt="PlatformEngineersToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/PlatformEngineersToolbox/time-to-first-byte-package/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/PlatformEngineersToolbox/time-to-first-byte-package?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package">
        <img src="https://img.shields.io/github/created-at/PlatformEngineersToolbox/time-to-first-byte-package?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/releases/latest">
        <img src="https://img.shields.io/github/v/release/PlatformEngineersToolbox/time-to-first-byte-package?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/releases/latest">
        <img src="https://img.shields.io/github/release-date/PlatformEngineersToolbox/time-to-first-byte-package?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/releases/latest">
        <img src="https://img.shields.io/github/commits-since/PlatformEngineersToolbox/time-to-first-byte-package/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/PlatformEngineersToolbox/time-to-first-byte-package/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This tool is designed to allow you to measure and display the 'Time To First Byte' (ttfb) for a given url. It can also help identify bottlenecks or latency issues that might be causing slow responses.

We also provide a simple [bash version](https://github.com/PlatformEngineersToolbox/time-to-first-byte) if you prefer that to a python package.

## Installation

```shell
pip install wolfsoftware.ttfb
```

## Usage

```
usage: ttfb [-h] [-d] [-v] [-V] [-m | -f] [-c COUNT] -u URL

Display the time-to-first-byte for any given url.

flags:
  -h, --help            show this help message and exit
  -d, --debug           Very noisy (default: False)
  -v, --verbose         Verbose output - show scan results as they come in (default: False)
  -V, --version         Show program's version number and exit.

exclusive flags:
  -m, --minimal         Show minimal set of timing values. (default: False)
  -f, --full            Show full set of timing values. (default: False)

optional:
  -c COUNT, --count COUNT
                        How many times to test [1-25] (default: 1)

required:
  -u URL, --url URL     The URL to test (default: None)
```

## Results Output

### Single Connection Test

##### Standard Output (Default)
```
-----------------------------------------------------------------------------------------------------------
                                          Time to First Byte Test
-----------------------------------------------------------------------------------------------------------
  Lookup Time: 0.005087   Connect Time: 0.025123   StartXfer Time (TTFB): 0.111106   Total Time: 0.111173
-----------------------------------------------------------------------------------------------------------
```

##### Minimal Output (-m)

```
----------------------------------------------------------
                 Time to First Byte Test
----------------------------------------------------------
  StartXfer Time (TTFB): 0.106124   Total Time: 0.106208
----------------------------------------------------------
```

##### Full Output (-f)

```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                               Time to First Byte Test
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Lookup Time: 0.004987   Connect Time: 0.022486   AppCon Time: 0.089366   PreXfer Time: 0.089427   Redirect Time: 0.000000   StartXfer Time (TTFB): 0.108404   Total Time: 0.108475
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Repeated Connection Test

It is also possible to specify how many connections to make when testing by adding the -c flag. This can be combined with the existing output flags (-m and -f)

```
-----------------------------------------------------------------------------------------------------------
                                          Time to First Byte Test
-----------------------------------------------------------------------------------------------------------
  Lookup Time: 0.005112   Connect Time: 0.034810   StartXfer Time (TTFB): 0.119705   Total Time: 0.119777
  Lookup Time: 0.005087   Connect Time: 0.023240   StartXfer Time (TTFB): 0.108551   Total Time: 0.108623
  Lookup Time: 0.004158   Connect Time: 0.021478   StartXfer Time (TTFB): 0.110971   Total Time: 0.111036
  Lookup Time: 0.005108   Connect Time: 0.022807   StartXfer Time (TTFB): 0.111455   Total Time: 0.111526
  Lookup Time: 0.004764   Connect Time: 0.022720   StartXfer Time (TTFB): 0.111475   Total Time: 0.111547
-----------------------------------------------------------------------------------------------------------
```

## Timing Key

| Time                                | Description                                                                                                                                                                                                                           |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Lookup time (time_namelookup)       | The time, in seconds, it took from the start until the name resolving was completed.                                                                                                                                                  |
| Connect time (time_connect)         | The time, in seconds, it took from the start until the TCP connect to the remote host was completed.                                                                                                                                  |
| AppCon time (time_appconnect)       | The time, in seconds, it took from the start until the SSL/SSH/etc connect/handshake to the remote host was completed.                                                                                                                |
| PreXfer time (time_pretransfer)     | The time, in seconds, it took from the start until the file transfer was just about to begin. This includes all 'pre-transfer' commands and negotiations that are specific to the particular protocol(s) involved.                    |
| Redirect time (time_redirect)       | The time, in seconds, it took for all redirection steps include name lookup, connect, pretransfer and transfer before the final transaction was started. 'time_redirect' shows the complete execution time for multiple redirections. |
| StartXfer time (time_starttransfer) | The time, in seconds, it took from the start until the first byte was just about to be transferred. This includes 'time_pretransfer' and also the time the server needed to calculate the result.                                     |
| Total time                          | The sum of all the other times.                                                                                                                                                                                                       |


## Response Times: The 3 Important Limits

Short note for your information.

* **0.1 second** – is about the limit for having the user feel that the system is reacting instantaneously, meaning that no special feedback is necessary except to display the result;
* **1.0 second** – is about the limit for the user’s flow of thought to stay uninterrupted, even though the user will notice the delay. Normally, no special feedback is necessary during delays of more than 0.1 but less than 1.0 second, but the user does lose the feeling of operating directly on the data;
* **10 seconds** – is about the limit for keeping the user’s attention focused on the dialogue. For longer delays, users will want to perform other tasks while waiting for the computer to finish, so they should be given feedback indicating when the computer expects to be done. Feedback during the delay is especially important if the response time is 

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
