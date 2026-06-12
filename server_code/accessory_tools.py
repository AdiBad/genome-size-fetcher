import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
import pandas as pd

@anvil.server.callable
def fetch_genome_data()->list:
  genome_table = pd.read_csv(data_files['genome_sizes.csv'])
  return genome_table.to_dict('records')

@anvil.server.callable
def fetch_genome_size(species: str)->list:
  genome_table = pd.read_csv(data_files['genome_sizes.csv'], 
                             index_col=0)
  return genome_table.loc[species].to_dict()

@anvil.server.callable
def load_local_table_from_CSV():
  genome_table = pd.read_csv(data_files['genome_sizes.csv'])
  for idx, rec in genome_table.iterrows():
    app_tables.genome_sizes.add_row(
      species=rec['species'],
      genome_size_mbp=rec['genome_size_mbp'])