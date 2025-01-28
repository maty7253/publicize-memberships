# Publicize Memberships

A simple script to make your GitHub organization memberships public with a single command. This was made for my friend @pilot2254

## Features
- Fetches all organizations the user belongs to.
- Automates the process of making organization memberships public using the GitHub API.
- Designed for simplicity and ease of use.

## Requirements
- Python 3.8 or later
- `requests` library (install via `pip install requests`)

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/maty7253/publicize-memberships.git
cd publicize-memberships
```

### 2. Install Dependencies
```bash
pip install requests
```

### 3. Generate a GitHub Personal Access Token
1. Navigate to **Settings > Developer Settings > Personal Access Tokens** on GitHub.
2. Create a token with `read:org` and `user` scopes.
3. Copy the token and keep it secure.

### 4. Run the Script
Replace `your_personal_access_token` and `your_github_username` in the script with your actual credentials.

```bash
python main.py
```

The script will:
- Fetch all organizations you belong to.
- Make your membership public for each organization.

### Example Output

```
Membership publicized for org1.
Membership publicized for org2.
...
```

## Customization
You can modify the script to:
- Exclude specific organizations.
- Add additional logging or error handling.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License. See `LICENSE` for details.
