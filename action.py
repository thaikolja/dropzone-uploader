# Dropzone Action Info
# Name:                 yanawa.io Dropzone Uploader
# Description:          Lädt eine Datei mit Zufallsnamen auf https://uploads.yanawa.io/ hoch.
# Handles:              Files
# Creator:              Kolja Nolte
# URL:                  https://www.kolja-nolte.com
# Events:               Dragged
# KeyModifiers:         Command, Option, Control, Shift
# SkipConfig:           No
# RunsSandboxed:        Yes
# Version:              1.0.0
# MinDropzoneVersion:   4.0
# PythonPath:           /usr/bin/python3

# Import the dotenvfile module, which provides a way to load environment variables from a .env file
import dotenvfile

# Import the paramiko module for SFTP
import paramiko

# Import the os module, which provides a way to interact with the operating system
import os

# Import the hashlib module, which provides a way to generate hash values
import hashlib

# Import the randint function from the random module, which generates a random integer
from random import randint

# Load the environment variables from the .env file and store them in a dictionary called env
env = dotenvfile.loadfile('.env')

# Define a dictionary called info that stores configuration information
info = {
    # The URL of the SFTP server
    'url': env.get('HTTP_URL'),

    # The hostname of the SFTP server
    'host': env.get('FTP_HOST'),

    # The port number of the SFTP server
    'port': env.get('FTP_PORT', 22),

    # The username to use for SFTP authentication
    'username': env.get('FTP_USERNAME'),

    # The password to use for SFTP authentication
    'password': env.get('FTP_PASSWORD')
}


# Define a function called verify that takes a file path as input and returns True if the file exists, False otherwise
def verify(file: str) -> bool:
    # Use the os.path.isfile function to check if the file exists
    return os.path.isfile(file)


# Define a function called dragged that is called when files are dragged and dropped onto the application
def dragged():
    # Set the determinate property of the dz object to True, indicating that the upload process has started
    dz.determinate(True)

    # Set the begin property of the dz object to a message indicating that the upload process has started
    dz.begin(f"Lade {len(items)} Datei(en) hoch...")

    # Set the percent property of the dz object to 1, indicating that the upload process has started
    dz.percent(1)

    # Get the list of files to be uploaded
    files = items

    # Get the number of files to be uploaded
    files_count = len(files)

    # Initialize a counter to keep track of the number of files uploaded
    uploaded_files = 0

    # Initialize a list to store the names of the uploaded files
    uploaded_files_names = []

    # Establish an SFTP connection to the server using paramiko
    transport = paramiko.Transport((info['host'], int(info['port'])))
    transport.connect(username=info['username'], password=info['password'])

    sftp = paramiko.SFTPClient.from_transport(transport)

    # Define the remote directory path
    remote_directory = '/mnt/storage/backup/uploads/'

    # Iterate over the list of files to be uploaded
    for file in files:
        # Check if the file exists using the verify function, and skip it if it doesn't
        if not verify(file):
            continue

        # Increment the uploaded files counter
        uploaded_files += 1

        # Update the progress bar by setting the percent property to the current progress
        dz.percent(int(100 * uploaded_files / files_count))

        # Get the filename and file extension from the file path
        file_name = os.path.basename(file)
        _, file_extension = file_name.rsplit('.', 1)

        # Generate a random number and convert it to a string
        random_number = randint(1, 128).__str__()

        # Generate a random name for the uploaded file using the hashlib library
        random_name = hashlib.md5(random_number.encode()).hexdigest()[:8]

        # Create a new filename by combining the random name with the original file extension
        new_file_name = f"{random_name}.{file_extension}"

        # Print current directory as absolute
        print(sftp.getcwd())

        # Open the file in binary read mode and upload it to the specified remote directory
        sftp.put(file, os.path.join(remote_directory, new_file_name))
        # Add the new filename to the list of uploaded files
        uploaded_files_names.append(new_file_name)

    # Set the percent property to 100 to indicate that the upload process is complete
    dz.percent(100)

    # Close the SFTP connection
    sftp.close()
    transport.close()

    # Set the finish property of the dz object to a message indicating that the upload process is complete
    dz.finish(f"{uploaded_files} Datei(en) hochgeladen und URLs in die Zwischenablage kopiert.")

    # Check if only one file was uploaded, and if so, set the text property of the dz object to the URL of the
    # uploaded file
    if files_count == 1:
        dz.text(f"{info['url']}/{new_file_name}")
    else:
        # If multiple files were uploaded, set the text property to a list of URLs for each file
        dz.text("\n".join([info['url'] + '/' + file_name for file_name in uploaded_files_names]))
