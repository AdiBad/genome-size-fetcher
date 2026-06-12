from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    
    #genomes_list = anvil.server.call('fetch_genome_data')
    #self.drop_down_1.items = [row['species'] for row in genomes_list]

    anvil.server.call('load_local_table_from_CSV')
    genomes_list = app_tables.genome_sizes.search()
    self.drop_down_1.items = [row['species'] for row in genomes_list]
    

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user_choice = self.drop_down_1.selected_value
    
    #detected_size = anvil.server.call('fetch_genome_size', user_choice)
    #self.text_box_1.text = detected_size['genome_size_mbp']

    genome_size = app_tables.genome_sizes.get(species=user_choice)
    self.text_box_1.text = genome_size['genome_size_mbp']
    
    
