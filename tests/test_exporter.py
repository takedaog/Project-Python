import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from export.exporter import export_to_xlsx

export_to_xlsx()  # Сохраняет файл eduplatform_export.xlsx



from export.exporter import export_to_csv

export_to_csv()  # Создаёт CSV-файл


from export.exporter import export_to_sql

export_to_sql()  # Сохраняет файл eduplatform_export.sql

