from kim import field
from .base import BaseMapper
from python_star_wars_api.models import Character

class CharacterMapper(BaseMapper):
	__type__ = Character
	name = field.String()