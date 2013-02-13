#Merge .csv files as sheets of .xls file

- date: 2013-02-12 07:41
- tags: tips, python
- category: work

-------

I frequently generate multiple .csv files with data which I would like to put in a single spreadsheet. After googling a bit, I quickly found this small piece of python code that does the trick:

```python
import glob, csv, xlwt, os
wb = xlwt.Workbook()
for filename in glob.glob("./*.csv"):
    (f_path, f_name) = os.path.split(filename)
    (f_short_name, f_extension) = os.path.splitext(f_name)
    ws = wb.add_sheet(f_short_name)
    spamReader = csv.reader(open(filename, 'rb'))
    for rowx, row in enumerate(spamReader):
        for colx, value in enumerate(row):
            ws.write(rowx, colx, value)
wb.save("./compiled.xls")
```

Just copy this to a python file, put your csv files in the same folder and execute! In the resulting file, you may have to apply the "Text to columns" function from your favorite spreadsheet software.

I found this solution [here](http://stackoverflow.com/a/5777529/162264).
