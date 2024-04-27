# yanawa.io Dropzone Uploader

[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/your-username/your-repo-name/releases) [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Dropzone Version](https://img.shields.io/badge/Dropzone-4.0+-green.svg)](https://aptonic.github.io/dropzone/)

This is a (personal) [Dropzone](https://aptonic.com/) action that uploads files with random names to [https://yanawa.io/temp/](https://yanawa.io/temp/). It is used and configured for personal use but can be adjusted via the `.env` file. This code was tested using Python 3.9.6.

## Configuration

This action uses environment variables from a `.env` file to configure the FTP (TLS/SSL) connection to the server as well as the URL that will be copied to the clipboard once the upload is complete.

## Requirements

* Python 3
* [Dropzone](https://aptonic.com/) 4.0 or higher

## How It Works

1. Drag and drop files onto the application.
2. The files are uploaded to the server using FTP.
3. The uploaded files are given random names using the `hashlib` library.
4. The URLs of the uploaded files are copied to the clipboard.

## Usage

To use this action, follow these steps:

1. Create a [new Dropzone action](https://i.imgur.com/pXii8Ns.png) and select "Files" as the handler.
2. Copy and paste the copy from the file `action.py` into your new action and add it to the grid.
2. Drag and drop one or more files onto the application.
3. The files will be uploaded to the server, and the URLs will be copied to the clipboard.
4. You can then paste the URLs into your desired application.

## Environment Variables

The following environment variables are required:

* `HTTP_URL`: the URL of the server (default: `https://host.yanawa.io`)
* `FTP_HOST`: the hostname of the FTP server (default: `host.yanawa.io`)
* `FTP_PORT`: the port number of the FTP server (default: `21`)
* `FTP_USERNAME`: the username to use for FTP authentication (default: `yanawa`)
* `FTP_PASSWORD`: the password to use for FTP authentication (default: `password`)

## Notes

* Make sure to create a `.env` file in the same directory as the action script with the required environment variables.
* This action uses the `ftplib` library to upload files to the server, so make sure it is installed.
* This action uses the `hashlib` library to generate random names for the uploaded files.
* This action uses the `dotenvfile` library. Make sure to install it.

**Info:** You can install libraries with `pip install <library>`.

## Author

**Kolja Nolte** <[kolja.nolte@gmail.com](mailto:kolja.nolte@gmail.com)> (https://www.kolja-nolte.com)

## Version

1.0.0

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
