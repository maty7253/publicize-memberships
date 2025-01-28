import requests

# Replace these with your credentials
TOKEN = "your_personal_access_token"
USERNAME = "your_github_username"

def get_organizations():
    """
    Fetches all organizations the user belongs to.
    Returns a list of organization names.
    """
    url = "https://api.github.com/user/orgs"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [org['login'] for org in response.json()]

def make_memberships_public(orgs):
    """
    Makes the user's membership public for each organization in the list.
    """
    for org in orgs:
        url = f"https://api.github.com/orgs/{org}/public_members/{USERNAME}"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.put(url, headers=headers)
        if response.status_code == 204:
            print(f"Membership publicized for {org}.")
        else:
            print(f"Failed to publicize membership for {org}: {response.status_code}")

if __name__ == "__main__":
    try:
        print("Fetching organizations...")
        organizations = get_organizations()
        print(f"Found {len(organizations)} organizations.")
        
        print("Making memberships public...")
        make_memberships_public(organizations)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
