# Read current branch from .git/HEAD
# This information is then used to determine the current version of the
# documentation. If we are in "master" the version is set to "latest", for all
# other branches the name is used. This means the release branches should have
# names like "1.0".
def get_version():
    with open(".git/HEAD", "r") as versionfile:
        version = versionfile.read().replace('\n', '')

    version = version.replace('ref: refs/heads/', '')
    if version == 'master':
        version = 'latest'

    return version

if __name__ == "__main__":
    print(get_version())
