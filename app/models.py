"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_process():
    import seed.models.process as SeedModel
    return SeedModel.Process

def get_user():
    import seed.models.user as SeedModel
    return SeedModel.User

def get_file():
    import seed.models.file as SeedFile
    return SeedFile.File

Process = get_process()
User = get_user()
File = get_file()