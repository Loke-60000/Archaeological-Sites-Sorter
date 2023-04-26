# Archaeological Sites Sorter

This repository contains two Python scripts for sorting archaeological sites based on different criteria. The first script `sort_sites.py` sorts the sites based on the commune name and Numéro INSEE, while the second script `sort_bibliography.py` sorts the sites based on their bibliography. The output files for both scripts are standalone executable files that do not require Python to be installed on the user's system.

## Dependencies

Both scripts use the following Python packages:

- `re`
- `openpyxl`
- `pyinstaller`

To install these packages, you can use pip:

pip install openpyxl pyinstaller

## Usage

### `sort_sites.py`

1. Place the `data.txt` file in the same directory as the script.
2. Open a terminal or command prompt in the same directory as the script.
3. Run `pyinstaller --onefile sort_sites.py` to create an executable file.
4. The executable file will be created in the `dist` directory.
5. Run the executable file to sort the data and generate an Excel file named `sorted_data.xlsx` in the same directory as the executable file.

### `sort_bibliography.py`

1. Place the `data.txt` file in the same directory as the script.
2. Open a terminal or command prompt in the same directory as the script.
3. Run `pyinstaller --onefile sort_bibliography.py` to create an executable file.
4. The executable file will be created in the `dist` directory.
5. Run the executable file to sort the data and generate an Excel file named `bibliography_sorted_data.xlsx` in the same directory as the executable file.

## Contributing

Contributions to the Archaeological Sites Sorter project are welcome. If you find any issues or have any suggestions, please open an issue or a pull request on the [GitHub repository](https://github.com/Loke-60000/Archaeological-Sites-Sorter).

## License

The Archaeological Sites Sorter project is licensed under the [MIT License](https://github.com/Loke-60000/Archaeological-Sites-Sorter/blob/main/LICENSE).
