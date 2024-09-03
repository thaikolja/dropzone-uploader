# Dropzone Uploader

![GitLab Release](https://img.shields.io/gitlab/v/release/thaikolja%2Fdropzone-uploader?style=flat&label=version) ![GitLab Stars](https://img.shields.io/gitlab/stars/thaikolja%2Fdropzone-uploader?style=flat&label=gitlab%20stars&color=%23eb763c)
 ![GitHub Stars](https://img.shields.io/github/stars/thaikolja/dropzone-uploader?style=flat&label=github%20stars) ![GitLab License](https://img.shields.io/gitlab/license/thaikolja%2Fdropzone-uploader?color=green) ![Gitlab Pipeline Status](https://img.shields.io/gitlab/pipeline-status/thaikolja%2Fdropzone-uploader)

This is a **private** [Dropzone](https://aptonic.com/) action that uploads one or more files with random names to [https://uploads.yanawa.io](https://uploads.yanawa.io), which links to a 100 GB [Storage Box provided by Hetzner](https://www.hetzner.com/storage/storage-box/). It is used and configured for personal use but can be adjusted easily via, as explained in this `README.md`.

**Note:** `v1.0.0` uses FTP over TLS. `v1.1.0` and above, however, use SFTP. To download the version with FTP support, see the "Usage" section. **In a future version, you can easily switch from FTP to SSL and vice versa.**

## Preview

<video width="100%" height="auto" poster="auto" controls>
  <source src="https://uploads.yanawa.io/mVdCXjSY.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Configuration

This action uses environment variables from a `.env` file to configure the FTP (TLS/SSL) connection to the server as well as the URL that will be copied to the clipboard once the upload is complete.

## Requirements

- Python 3
- [Dropzone](https://aptonic.com/) 4.0 or higher

### Python Modules

The following Python modules are required and can be downloaded via `pip install <module_name>` (without the `<` and `>`):

- `paramiko`: Module providing support for SFTP. **Required since `v1.1.0`.**
- `ftplib`: FTP over TSL support. **Only required for `v1.0.0`.**
- `hashlib`: Module to generate random names for the uploaded files.
- `dotenvfile`: Module to parse values from `.env` files.

## Installation

### From GitLab

```bash
git clone https://gitlab.com/thaikolja/dropzone-uploader.git
```

### From GitHub

```bash
git clone https://hublab.com/thaikolja/dropzone-uploader.git
```

### As .zip Archive

[Download the repository as a .zip archive here.](https://gitlab.com/thaikolja/dropzone-uploader/-/archive/main/dropzone-uploader-main.zip)

#### Older Version

Every version is saved as a Git tag. To download the repository with a specific version tag, use the `--branch` flag in Git:

```bash
git clone --branch v1.0.0 https://gitlab.com/thaikolja/dropzone-uploader.git
```

## Usage

To use this action, follow these steps:

1. Create a [new Dropzone action](https://i.imgur.com/pXii8Ns.png) and select "Files" as the handler.
2. Copy and paste the copy from the file `action.py` into your new action and add it to the grid.
3. **IMPORTANT:** Create a file named `.env` in the same folder with `actions.py` with the structure of `.env.example` and your added values.
4. Drag and drop one or more files onto the application.
5. The files will be uploaded to the server, and the URLs will be copied to the clipboard.
6. You can then paste the URLs into your desired application.

## How It Works

1. Drag and drop files onto the application.
2. The files are uploaded to the server using FTP.
3. The uploaded files are given random names using the `hashlib` library.
4. The URLs of the uploaded files are copied to the clipboard.

## Environment Variables

The following environment variables are **required** and will be parsed from your `.env` file:

- `HTTP_URL`: the URL of the server)
- `FTP_HOST`: the hostname of the FTP server)
- `FTP_PORT`: the port number of the FTP server (default: `21`)
- `FTP_USERNAME`: the username to use for FTP authentication)
- `FTP_PASSWORD`: the password to use for FTP authentication)

## Author

**Kolja Nolte** <[kolja.nolte@gmail.com](mailto:kolja.nolte@gmail.com)> (https://www.kolja-nolte.com)

## Version

### v1.1.0

- **Replaced** FTP with SFTP for secure file transfers
- **Changed** code so that there are **no more default values**; instead, you must create a `.env` file with the structure of `.env.example` in the root directory of your `.py` script
- **Added** `paramiko` import module (required)
- **Updated** upload directory to `/mnt/storage/backup/uploads` (this is where my personal Storage Box is located)
- **Removed** unused `ftplib` import module
- **Fixed** port type issue by converting the port to an integer
- **Enhanced** file verification with error handling

### v1.0.0

- Initial release with FTP over TLS protocol support

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
