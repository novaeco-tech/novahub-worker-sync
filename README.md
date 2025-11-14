# Hub Worker: Sync

This is a decoupled worker service for the `hub` enabler.

Its sole purpose is to.

This service is intentionally decoupled from the main `hub-api` to ensure that a failure in this non-essential sync task can never crash the user-facing API.

## 🚀 Getting Started (Local Development)

This repository is configured to use **DevContainers** for a one-click setup.

1.  Make sure you have([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)) installed and running.
2.  Install the([https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)) in VS Code.
3.  Clone this repository: `git clone https://github.com/nova-ecosystem/hub-worker-sync.git`
4.  Open the cloned folder in VS Code.
5.  A pop-up will appear: "Folder contains a Dev Container... Reopen in Container?". Click **"Reopen in Container"**.

This will instantly download the pre-built `dev-python` image and install the dependencies from `src/requirements.txt`.