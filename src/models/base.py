from abc import ABC

class BaseEntity(ABC):
    """
    Base class for all entities in the application.
    This class can be extended to create specific entity types.
    """
    
    def __init__(self, entity_id: int):
        self.entity_id = entity_id    # Unique identifier for the entity
        
    
    @property
    def entity_id(self) -> int:
        """Get the unique identifier of the entity."""
        return self._entity_id
    
    @entity_id.setter
    def entity_id(self, value) :
        if value <=0 :
            raise ValueError("Entity ID must be a positive integer.")
        self.entity_id = value
        
    def __str__(self) :
        return f"{self.__class__.__name__}(ID: {self.entity_id})"