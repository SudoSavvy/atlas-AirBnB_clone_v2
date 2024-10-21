#!/usr/bin/python3
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class BaseModel:
    """Defines all common attributes/methods for other classes."""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes a new model."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
        else:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.utcnow())
            self.updated_at = kwargs.get('updated_at', datetime.utcnow())
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """Updates `updated_at` and saves the model."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of the instance."""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in model_dict:
            del model_dict["_sa_instance_state"]
        return model_dict

    def delete(self):
        """Deletes the current instance from storage."""
        models.storage.delete(self)
