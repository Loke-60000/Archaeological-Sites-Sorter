# Archaeological Sites Sorter

This repository contains two Python scripts for sorting archaeological sites based on different criteria. The first script `app.py` sorts the sites based on the commune name and Numéro INSEE, while the second script `app_bibli.py` sorts the sites based on their bibliography. The output files for both scripts are standalone executable files that do not require Python to be installed on the user's system.

## Dependencies

Both scripts use the following Python packages:

- `re`
- `openpyxl`
- `pyinstaller`

To install these packages, you can use pip:

pip install openpyxl pyinstaller

## Usage

### `App.py`

1. Place the `data.txt` file in the same directory as the script.
2. Open a terminal or command prompt in the same directory as the script.
3. Run `python app.py`.
4. the script will sort the data and generate an Excel file  in the same directory as the executable file.

### `app_bibli.py`

1. Place the `data.txt` file in the same directory as the script.
2. Open a terminal or command prompt in the same directory as the script.
3. Run `python app_bibli.py`.
4. the script will sort the data and generate an Excel file  in the same directory as the executable file.


### `Exe files`

You can also run the exe files in the output folder to use the scripts without using Python

1. Place the `data.txt` file in the same directory as the script.
2. Run one of the exe files in the same directory as the data as the data.txt file.
3. the exe will sort the data and generate an Excel file in the same directory as the executable file.

## Contributing

Contributions to the Archaeological Sites Sorter project are welcome. If you find any issues or have any suggestions, please open an issue or a pull request on the [GitHub repository](https://github.com/Loke-60000/Archaeological-Sites-Sorter).

## License

The Archaeological Sites Sorter project is licensed under the [MIT License](https://github.com/Loke-60000/Archaeological-Sites-Sorter/blob/main/LICENSE).
