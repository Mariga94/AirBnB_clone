#!/usr/bin/python3
"""
Initialize models package
"""

from models.engine.file_storage import FileStorage
"""A variable storage which is an instance of FileStorage"""
storage = FileStorage()

storage.reload()
