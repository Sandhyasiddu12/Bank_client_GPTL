from ._anvil_designer import loan_typeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class loan_type(loan_typeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form.new_loan_request.k12_loan')

  def link_2_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form.new_loan_request.business_loan')

  def button_2_click(self, **event_args):
    open_form('bank_users.borrower_registration_main_form.new_loan_request')
