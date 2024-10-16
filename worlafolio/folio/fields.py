from django.db import models
from django.forms import CharField
from typing import List


# Custom comma separated tags field
class CustomTagsField(models.Field):
    description = "A custom field for storing a list of tags as a comma-separated-string."

    def _helper(self, value: str | list | None) -> list[str]:
        """A helper method to convert string or list to a list of stripped strings"""
        if isinstance(value, list):
            return [x.strip() for x in value]
        if value is None:
            return []
        return [x.strip() for x in value.split(',')]
    
    def from_db_value(self, value: str | None, expression, connection) -> list[str]:
        """Convert the database value to a Python list."""
        return self._helper(value)
    
    def to_python(self, value: str | list | None) -> list[str]:
        """Convert the input value to a Python list."""
        return self._helper(value)
    
    def get_prep_value(self, value: list[str] | None) -> str:
        """Prepare the value for storage in the database."""
        if value is None:
            return ''
        return ','.join(str(x) for x in value)
    
    def db_type(self, connection) -> str:
        """Specify the database type for this field."""
        if connection.settings_dict['ENGINE'] == 'django.db.backend.postgresql':
            return 'text'
        elif connection.settings_dict['ENGINE'] == 'django.db.backend.sqlite3':
            return 'text'
        return "char(%s)" % self.max_length
    
    def formfield(self, **kwargs):
        """Return a CharField for form use."""
        defaults = {'form_class': CharField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
    