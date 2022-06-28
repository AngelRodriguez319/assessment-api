"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_process_serializer():
    import seed.serializers.process as SeedSerializer
    return SeedSerializer.ProcessSerializer

def get_user_serializer():
    import seed.serializers.user as SeedSerializer
    return SeedSerializer.UserSerializer

def get_file_serializer():
    import seed.serializers.file as SeedSerializer
    return SeedSerializer.FileSerializer

ProcessSerializer = get_process_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()