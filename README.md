# simple-stats-measurement-calculator

A short Python script that prints basic descriptive statistics for a list of numbers: sum, count, mean, median, mode, and range. Handy for checking statistics homework done by hand.

## Run it

You need Python 3. There is nothing to install.

```bash
python3 main.py
```

On Windows, use `python main.py` (or `py main.py`).

## Example output

With the sample list that ships in `main.py`:

```text
--- Standard Measurement & Statistics Calculator ---
Dataset: [15, 22, 34, 45, 22, 67, 89, 22, 45]
Total Sum: 361
Count of Items: 9
Calculated Mean: 40.11
Calculated Median: 34
Mode(s): 22
Range: 74 (min 15, max 89)
```

## Use your own numbers

Open `main.py` and edit the `sample` list at the bottom of the file:

```python
sample = [15, 22, 34, 45, 22, 67, 89, 22, 45]
```

## How the numbers are worked out

- **Mean**: the sum divided by the count.
- **Median**: the middle value after sorting. With an even count it is the average of the two middle values.
- **Mode**: every value that shows up the most times, so there can be more than one.
- **Range**: the largest value minus the smallest.

## License

MIT. See [LICENSE](LICENSE).
