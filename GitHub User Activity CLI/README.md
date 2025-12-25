# GitHub User Activity Tracker CLI

A basic GitHub user activity tracker written in Python. Retrieves the recent user activity using `requests` and looks through each event in the resulting JSON. Prints the appropriate output for each unique event.

Project specs can be found in [GitHub User Activity](https://roadmap.sh/projects/github-user-activity). [Solution link](https://roadmap.sh/projects/github-user-activity/solutions?u=685bd531692da1a94eaeb7af).


---

## Features

* Checks if the user name exists or have no recent activity
* Uses GitHub Events API to retrieve the user activities using `requests.get()`
* Lists all activities by checking the `event` key in the output JSON

---

## Requirements

* Python **3.8+**
* Standard library only (no external dependencies)

---

## Installation

1. Clone or download this repository
2. Ensure Python is installed:

```bash
python --version
```

3. Navigate to the project directory

---

## Usage

Run the application:

```bash
python activity_tracker.py
```

---

## Notes & Limitations

* 300 events at maximum can be retrieved due to the API limitations
* Does not properly fully differentiate between a user not existing or the user has no recent activities.
* Input is case-sensitive

---

## License

This project is for learning and personal use. Feel free to modify and expand it.


