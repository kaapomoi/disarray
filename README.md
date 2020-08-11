disarray
===
A playlist auto-shuffler for Spotify, since they have no idea how to shuffle while playing.

### Installation

##### Install python3

[Python 3.8.5](https://www.python.org/downloads/release/python-385/)

[Python installation on windows](https://docs.python.org/3/using/windows.html)

Add python to **PATH**

##### Clone this repository

```bash
git clone https://github.com/kaapomoi/disarray.git
```

##### Create a spotify developer application

Log into the [Spotify Developer portal](https://developer.spotify.com/dashboard/applications), click on **CREATE AN APP**, the name and desc of the app doesn't matter.

Now you need to setup a Redirect URI for the app. Click on **EDIT SETTINGS** and copy `http://localhost:8888/callback/` into the Redirect URIs field, then click **ADD** and **SAVE**.

You'll need the Client ID and Client Secret for the next section.

### Usage

##### Windows

You can use **disarray** via a batch file with these commands:
```bash
CHCP 65001
python <WHERE_YOU_CLONED_THIS_REPO>\disarray\main.py <your-client-secret> <your-client-id> <your-spotify-username> "<name-of-playlist>"
pause
```

##### UNIX

todo