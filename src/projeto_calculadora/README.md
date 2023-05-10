https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/

https://pyinstaller.org/en/stable/

```bash
$ pip install pyinstaller

$ pyinstaller --name="Calculadora" --noconfirm --onefile --add-data='files/;files/' --icon='files/icon.png' --noconsole --clean --log-level=WARN  .\main.py

$ pyinstaller __localcode/Calculadora.spec

#  --distpath --workpath
```
