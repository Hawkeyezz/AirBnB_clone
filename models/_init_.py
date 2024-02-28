#!/usr/bin/python3
"""Creates a unique file storage instance for the application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
