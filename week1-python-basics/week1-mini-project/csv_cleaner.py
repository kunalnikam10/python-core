import csv

class CsvDataCleaner:
  def __init__(self, input_file, output_file):
    self.input_file= input_file
    self.output_file= output_file
    self.cleaned_data =[]

  def read_csv(self):
    try:
      with open(self.input_file, "r", newline="") as file:
        reader= csv.DictReader(file)
        self.data = list(reader)
    except FileNotFoundError:
      print("File not found")
      self.data= []

  def clean_data(self):
    for row in self.data:
      if not row["Name"] or not row["Email"] or not row["Age"]:
        continue

      cleaned_row= {
        "Name" : row["Name"].strip().title(),
        "Email": row["Email"].strip().lower(),
        "Age" : int(row["Age"])
      }
      self.cleaned_data.append(cleaned_row)

  def write_csv(self):
    with open(self.output_file,"w", newline="") as file:
      fieldnames= ["Name","Email","Age"]
      writer= csv.DictWriter(file, fieldnames=fieldnames)

      writer.writeheader()
      writer.writerows(self.cleaned_data)

  def run(self):
    self.read_csv()
    self.clean_data()
    self.write_csv()
    print("Data cleaning completed successfully.")

cleaner= CsvDataCleaner("raw_data.csv","cleaned_data.csv")
cleaner.run()