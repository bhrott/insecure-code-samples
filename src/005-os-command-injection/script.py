#!/bin/python

import os

def generate_invoice_pdf(email, payment_data):
  os.system('my_pdf_tool %s %s' % (email, payment_data))  
