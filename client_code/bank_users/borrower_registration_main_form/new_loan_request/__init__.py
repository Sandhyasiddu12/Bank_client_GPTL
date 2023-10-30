from ._anvil_designer import new_loan_requestTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class new_loan_request(new_loan_requestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_copy_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form.new_loan_request.loan_type')

  def button_1_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form')
