# File Transfer

This has been tested with Python 3.8

## Install

Clone this repo and `cd` into the directory created and enter the below command to install dependencies.

```sh
pip install -r requirements.txt
```

## Testing

```sh
cd file_transfer
python manage.py test file_transfer_tool.tests
```

## Usage

Create a local database:

```sh
python manage.py migrate
```

Start the server locally in a terminal:

```sh
python manage.py runserver
```

Go to the following page http://127.0.0.1:8000/upload/ and fill in the presented form and submit it.

You will be presented with a hyperlink that you can copy. This link can be sent to a friend so he can download the file.

Click the download link and enter the password when prompted (the same password submitted when uploading) and submit it.

If the password is correct, you will have the option to download the file.
