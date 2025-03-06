# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# Defining a model for a simple CRUD system
class SimpleCRUD(models.Model):

    # Field to store the name of the registered item
    name_item = models.CharField(_("Name of register"), max_length=255, null=False)

    # Field to store the quantity of the registered item
    quantity_item = models.IntegerField(_("Quantity of register"), null=False)

    # Boolean field to indicate if the item is available in the register
    have_item = models.BooleanField(_("Have the item in the register?"), default=True)

    # String representation of the model instance
    def __str__(self):
        return self.name_item
    
    class Meta:
        # Defines the database table name for this model
        db_table = 'simple_crud'

        # Defines the application label for the model
        app_label = 'simple_crud'
